# /// script
# requires-python = ">=3.11"
# dependencies = ["openpyxl"]
# ///
"""Revenue of Northwind Traders by product and by country.

Single-file script (PEP 723 regime). Data flow: reads the sheets Orders and
Order Details from eingang/bestellungen.xlsx and Products and Categories from
eingang/produkte.xlsx, computes the revenue of every order line as
UnitPrice * Quantity * (1 - Discount), and prints the ranking by product and
by delivery country, plus the totals and the date range. With --csv it also
writes both rankings to output/. With --web it writes dashboard/northwind/
data.js for the revenue page: sums per month, delivery country and product,
with the category of each product, nothing else.

Design decisions:
- Data minimisation: the question needs only orders, order lines and product
  names. kunden.xlsx and mitarbeitende.xlsx are never opened; the country is
  the delivery country ShipCountry of the order.
- Orders not yet shipped count as revenue, because they are booked sales;
  their number is reported so the reader can judge.
- The input files are third-party data; only the needed columns are read and
  nothing from them is executed. Each file is opened once and closed.
- A line whose order, product or date cannot be resolved is reported and left
  out of every sum, so totals and rankings stay consistent.

Usage: uv run scripts/northwind_umsatz.py [--top 10] [--csv] [--web]
"""

import argparse
import csv
import json
import sys
from collections import defaultdict
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parents[1]
INBOX = ROOT / "eingang"
OUT = ROOT / "output"
WEB = ROOT / "dashboard" / "northwind" / "data.js"


def _sheets(path: Path, wanted: dict[str, tuple[str, ...]]) -> dict[str, list[dict]]:
    """Rows of the named sheets of one workbook, restricted to their columns."""
    if not path.exists():
        sys.exit(
            f"Missing {path.relative_to(ROOT)}; place the attachments in eingang/ first."
        )
    workbook = openpyxl.load_workbook(path, read_only=True, data_only=True)
    try:
        result = {}
        for name, columns in wanted.items():
            if name not in workbook.sheetnames:
                sys.exit(f"{path.name} has no sheet {name!r}.")
            rows = workbook[name].iter_rows(values_only=True)
            header = list(next(rows))
            missing = [c for c in columns if c not in header]
            if missing:
                sys.exit(f"{path.name}/{name} lacks the columns {missing}.")
            index = {c: header.index(c) for c in columns}
            result[name] = [
                {c: row[i] for c, i in index.items()} for row in rows if any(row)
            ]
        return result
    finally:
        workbook.close()


def revenue() -> dict:
    sales = _sheets(
        INBOX / "bestellungen.xlsx",
        {
            "Orders": ("OrderID", "OrderDate", "ShippedDate", "ShipCountry"),
            "Order Details": (
                "OrderID",
                "ProductID",
                "UnitPrice",
                "Quantity",
                "Discount",
            ),
        },
    )
    catalogue = _sheets(
        INBOX / "produkte.xlsx",
        {
            "Products": ("ProductID", "ProductName", "CategoryID"),
            "Categories": ("CategoryID", "CategoryName"),
        },
    )
    orders, lines = sales["Orders"], sales["Order Details"]
    products, categories = catalogue["Products"], catalogue["Categories"]

    country_of = {o["OrderID"]: o["ShipCountry"] for o in orders}
    # Orders without a date have no month; their lines are reported below.
    month_of = {
        o["OrderID"]: f"{o['OrderDate']:%Y-%m}" for o in orders if o["OrderDate"]
    }
    name_of = {p["ProductID"]: p["ProductName"] for p in products}
    category_name = {c["CategoryID"]: c["CategoryName"] for c in categories}
    category_of = {
        p["ProductName"]: category_name.get(p["CategoryID"], "ohne Kategorie")
        for p in products
    }
    # Sums per month, delivery country and product: the finest grain the
    # revenue page needs, without any order, customer or person.
    cells: dict[tuple[str, str, str], float] = defaultdict(float)
    by_product: dict[str, float] = defaultdict(float)
    by_country: dict[str, float] = defaultdict(float)
    errors = []
    for line in lines:
        try:
            amount = (
                float(line["UnitPrice"])
                * int(line["Quantity"])
                * (1 - float(line["Discount"]))
            )
            # Resolve every key first, so a failing line adds to no sum.
            product = name_of[line["ProductID"]]
            country = country_of[line["OrderID"]]
            month = month_of[line["OrderID"]]
            by_product[product] += amount
            by_country[country] += amount
            cells[(month, country, product)] += amount
        except (KeyError, TypeError, ValueError) as exc:
            errors.append(
                f"order {line['OrderID']}, product {line['ProductID']}: {exc!r}"
            )
    dates = sorted(o["OrderDate"] for o in orders if o["OrderDate"])
    return {
        "by_product": sorted(by_product.items(), key=lambda kv: -kv[1]),
        "by_country": sorted(by_country.items(), key=lambda kv: -kv[1]),
        "total": sum(by_product.values()),
        "orders": len(orders),
        "lines": len(lines),
        "unshipped": sum(1 for o in orders if not o["ShippedDate"]),
        "first": dates[0],
        "last": dates[-1],
        "cells": cells,
        "category_of": category_of,
        "errors": errors,
    }


def _print_ranking(
    title: str, ranking: list[tuple[str, float]], total: float, top: int
) -> None:
    print(f"\n{title}")
    for rank, (name, amount) in enumerate(ranking[:top], start=1):
        print(f"{rank:>3}. {name:<34} {amount:>13,.2f}  {amount / total:6.1%}")


def _write_csv(path: Path, ranking: list[tuple[str, float]], label: str) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow([label, "revenue"])
        writer.writerows((name, f"{amount:.2f}") for name, amount in ranking)


def _write_web(result: dict) -> None:
    """Aggregated data for dashboard/northwind/, as a script for file:// use."""
    months = sorted({m for m, _, _ in result["cells"]})
    countries = sorted({c for _, c, _ in result["cells"]})
    products = sorted(result["category_of"])
    categories = sorted(set(result["category_of"].values()))
    index = {name: i for i, name in enumerate(products)}
    data = {
        "source": "Northwind sample database (Microsoft), exercise data",
        "first": f"{result['first']:%Y-%m-%d}",
        "last": f"{result['last']:%Y-%m-%d}",
        "orders": result["orders"],
        "lines": result["lines"],
        "unshipped": result["unshipped"],
        "total": round(result["total"], 2),
        "months": months,
        "countries": countries,
        "categories": categories,
        "products": [
            [name, categories.index(result["category_of"][name])] for name in products
        ],
        "cells": [
            [months.index(m), countries.index(c), index[p], round(v, 2)]
            for (m, c, p), v in sorted(result["cells"].items())
        ],
    }
    WEB.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    WEB.write_text(
        "// Generated by scripts/northwind_umsatz.py --web; do not edit.\n"
        f"window.NORTHWIND = {payload};\n",
        encoding="utf-8",
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--top", type=int, default=10, help="lines per ranking")
    parser.add_argument(
        "--csv", action="store_true", help="write both rankings to output/"
    )
    parser.add_argument(
        "--web", action="store_true", help="write data for dashboard/northwind/"
    )
    args = parser.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    result = revenue()
    print(
        f"{result['orders']} orders, {result['lines']} order lines, "
        f"{result['first']:%Y-%m-%d} to {result['last']:%Y-%m-%d}, "
        f"{result['unshipped']} not shipped"
    )
    print(f"Total revenue: {result['total']:,.2f}")
    _print_ranking(
        f"Top {args.top} products", result["by_product"], result["total"], args.top
    )
    _print_ranking(
        f"Top {args.top} delivery countries",
        result["by_country"],
        result["total"],
        args.top,
    )
    print(
        f"\n{len(result['by_product'])} products, {len(result['by_country'])} countries in total"
    )
    if args.csv:
        OUT.mkdir(exist_ok=True)
        _write_csv(
            OUT / "northwind_umsatz_produkte.csv", result["by_product"], "product"
        )
        _write_csv(
            OUT / "northwind_umsatz_laender.csv", result["by_country"], "country"
        )
        print("CSV written to output/")
    if args.web:
        _write_web(result)
        print(f"Web data written to {WEB.relative_to(ROOT)}")
    for error in result["errors"]:
        print(f"ERROR {error}")
    return 1 if result["errors"] else 0


if __name__ == "__main__":
    sys.exit(main())
