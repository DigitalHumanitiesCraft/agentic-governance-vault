# /// script
# requires-python = ">=3.11"
# dependencies = ["openpyxl"]
# ///
"""Check every Northwind key figure against a reference from the Excel files.

Single-file script (PEP 723 regime). Data flow: reads the sheets Orders and
Order Details from eingang/bestellungen.xlsx and Products and Categories from
eingang/produkte.xlsx, computes the reference figures with its own code, and
compares them with dashboard/northwind/data.js (written by
scripts/northwind_umsatz.py --web) and with the figures stated in
protokolle/2026-11-05_northwind-anfrage.md. Prints every comparison that
fails and a summary, and exits 1 on any deviation above 0.01, on a missing
figure or on a broken key.

Design decisions:
- Independence: nothing is imported from northwind_umsatz.py. Columns are
  found by this script's own header lookup, amounts are summed as Decimal
  from the cell text, and the order and product lookups are rebuilt here, so
  a shared bug in float arithmetic or key resolution would show up as a
  deviation.
- data.js stores sums per month, delivery country and product rounded to
  cents, and the page adds these cells for every figure it shows. Each cell
  must therefore be whole cents and at most half a cent from the exact
  reference, so a systematic shift below 0.01 is caught. Every aggregate the
  page shows is compared, within 0.01, with the same sum built from the
  reference cells rounded to cents; the exact total is printed beside it.
- A broken key or a missing order date is counted as a failure, and the
  lines concerned are left out of the reference so the report still prints.
- Data minimisation: kunden.xlsx and mitarbeitende.xlsx are never opened, and
  of produkte.xlsx the sheet Suppliers is not read.
- The protocol is German prose; its figures are parsed from the two ranking
  tables and from fixed phrases. A phrase that is not found counts as a
  failure, so a rewritten protocol is noticed rather than skipped.

Usage: uv run scripts/northwind_check.py
"""

import json
import re
import sys
from collections import defaultdict
from datetime import date, datetime
from decimal import Decimal
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parents[1]
INBOX = ROOT / "eingang"
WEB = ROOT / "dashboard" / "northwind" / "data.js"
PROTOCOL = ROOT / "protokolle" / "2026-11-05_northwind-anfrage.md"
TOLERANCE = Decimal("0.01")
CENT = Decimal("0.01")
CELL_TOLERANCE = Decimal("0.005000001")

# The protocol names delivery countries in German, the data in English.
COUNTRY_DE = {
    "USA": "USA",
    "Deutschland": "Germany",
    "Österreich": "Austria",
    "Brasilien": "Brazil",
    "Frankreich": "France",
}
MONTH_DE = {
    "Januar": 1,
    "Februar": 2,
    "März": 3,
    "April": 4,
    "Mai": 5,
    "Juni": 6,
    "Juli": 7,
    "August": 8,
    "September": 9,
    "Oktober": 10,
    "November": 11,
    "Dezember": 12,
}


class Report:
    def __init__(self) -> None:
        self.passed = 0
        self.failures: list[str] = []

    def number(self, label: str, expected: Decimal, actual, tol=TOLERANCE) -> None:
        if actual is None:
            self.failures.append(f"{label}: missing, reference {expected}")
            return
        diff = abs(Decimal(str(actual)) - expected)
        if diff > tol:
            self.failures.append(
                f"{label}: {actual} vs reference {expected} (deviation {diff})"
            )
        else:
            self.passed += 1

    def equal(self, label: str, expected, actual) -> None:
        if expected != actual:
            self.failures.append(f"{label}: {actual!r} vs reference {expected!r}")
        else:
            self.passed += 1


def read_sheet(workbook, name: str, columns: tuple[str, ...]) -> list[tuple]:
    """Rows of one sheet as tuples in the order of `columns`."""
    rows = workbook[name].iter_rows(values_only=True)
    header = next(rows)
    positions = []
    for column in columns:
        hits = [i for i, cell in enumerate(header) if cell == column]
        if len(hits) != 1:
            sys.exit(f"Sheet {name!r}: column {column!r} found {len(hits)} times.")
        positions.append(hits[0])
    return [
        tuple(row[i] for i in positions)
        for row in rows
        if any(cell is not None for cell in row)
    ]


def open_workbook(name: str):
    path = INBOX / name
    if not path.exists():
        sys.exit(f"Missing eingang/{name}; place the exercise files in eingang/.")
    return openpyxl.load_workbook(path, read_only=True, data_only=True)


def dec(value) -> Decimal:
    # Via str, so 0.15 stays 0.15 instead of its binary approximation.
    return Decimal(str(value))


def reference(report: Report) -> dict:
    book = open_workbook("bestellungen.xlsx")
    try:
        orders = read_sheet(
            book, "Orders", ("OrderID", "OrderDate", "ShippedDate", "ShipCountry")
        )
        details = read_sheet(
            book,
            "Order Details",
            ("OrderID", "ProductID", "UnitPrice", "Quantity", "Discount"),
        )
    finally:
        book.close()
    book = open_workbook("produkte.xlsx")
    try:
        products = read_sheet(
            book, "Products", ("ProductID", "ProductName", "CategoryID")
        )
        categories = read_sheet(book, "Categories", ("CategoryID", "CategoryName"))
    finally:
        book.close()

    # Keys: OrderID, ProductID and CategoryID are unique, (OrderID, ProductID)
    # is unique in Order Details, and every foreign key resolves.
    for label, keys in (
        ("Orders.OrderID", [o[0] for o in orders]),
        ("Products.ProductID", [p[0] for p in products]),
        ("Categories.CategoryID", [c[0] for c in categories]),
        ("Order Details (OrderID, ProductID)", [(d[0], d[1]) for d in details]),
    ):
        report.equal(f"unique {label}", len(keys), len(set(keys)))
    order = {o[0]: o for o in orders}
    product = {p[0]: p for p in products}
    category = {c[0]: c[1] for c in categories}
    report.equal(
        "Order Details.OrderID resolves",
        0,
        sum(1 for d in details if d[0] not in order),
    )
    report.equal(
        "Order Details.ProductID resolves",
        0,
        sum(1 for d in details if d[1] not in product),
    )
    report.equal(
        "Products.CategoryID resolves",
        0,
        sum(1 for p in products if p[2] not in category),
    )
    report.equal("every order has a date", 0, sum(1 for o in orders if o[1] is None))

    # Lines whose order, product or date does not resolve are already counted
    # as failures above; they are skipped here so the report still prints.
    cells: dict[tuple[str, str, str], Decimal] = defaultdict(Decimal)
    for order_id, product_id, price, quantity, discount in details:
        if order_id not in order or product_id not in product:
            continue
        _, ordered, _, country = order[order_id]
        if ordered is None:
            continue
        amount = dec(price) * dec(quantity) * (1 - dec(discount))
        name = product[product_id][1]
        cells[(f"{ordered.year:04d}-{ordered.month:02d}", country, name)] += amount
    category_of = {p[1]: category.get(p[2]) for p in products}

    def total_by(key) -> dict[str, Decimal]:
        out: dict[str, Decimal] = defaultdict(Decimal)
        for k, v in cells.items():
            out[key(k)] += v
        return dict(out)

    dates = [
        o[1].date() if isinstance(o[1], datetime) else o[1]
        for o in orders
        if o[1] is not None
    ]
    return {
        "orders": len(orders),
        "lines": len(details),
        "unshipped": sum(1 for o in orders if o[2] is None),
        "first": min(dates),
        "last": max(dates),
        "cells": dict(cells),
        "total": sum(cells.values(), Decimal(0)),
        "month": total_by(lambda k: k[0]),
        "country": total_by(lambda k: k[1]),
        "product": total_by(lambda k: k[2]),
        "category": total_by(lambda k: category_of[k[2]]),
        "category_of": category_of,
    }


def check_web(ref: dict, report: Report) -> None:
    if not WEB.exists():
        report.failures.append("dashboard/northwind/data.js is missing")
        return
    text = WEB.read_text(encoding="utf-8")
    match = re.search(r"window\.NORTHWIND\s*=\s*(\{.*\});", text, re.DOTALL)
    if not match:
        report.failures.append("data.js holds no window.NORTHWIND object")
        return
    web = json.loads(match.group(1))

    for key in ("orders", "lines", "unshipped"):
        report.equal(f"page {key}", ref[key], web.get(key))
    report.equal("page first date", ref["first"].isoformat(), web.get("first"))
    report.equal("page last date", ref["last"].isoformat(), web.get("last"))
    report.number("page total field", ref["total"], web.get("total"))

    months, countries = web["months"], web["countries"]
    names = [p[0] for p in web["products"]]
    report.equal("page months", sorted(ref["month"]), months)
    report.equal("page countries", sorted(ref["country"]), countries)
    report.equal("page products", sorted(ref["product"]), sorted(names))
    report.equal(
        "page categories",
        sorted({c for c in ref["category_of"].values() if c is not None}),
        sorted(web["categories"]),
    )
    for name, cat in web["products"]:
        report.equal(
            f"page category of {name}",
            ref["category_of"].get(name),
            web["categories"][cat],
        )

    # Cell level: the finest grain on the page, each rounded to cents.
    web_cells = {
        (months[m], countries[c], names[p]): dec(v) for m, c, p, v in web["cells"]
    }
    # Only the differing keys are named, the full key lists run to thousands.
    report.equal(
        "page cell keys missing from the reference",
        [],
        sorted(web_cells.keys() - ref["cells"].keys())[:10],
    )
    # A page cell must be a correct rounding of the exact value to cents: whole
    # cents, and no further than half a cent from the exact sum. The slack
    # above half a cent only absorbs the float noise of the generator's sums;
    # a tie at exactly half a cent may round either way.
    for key, value in ref["cells"].items():
        shown = web_cells.get(key)
        if shown is not None and shown != shown.quantize(CENT):
            report.failures.append(f"page cell {key}: {shown} is not whole cents")
            continue
        report.number(f"page cell {key}", value, shown, CELL_TOLERANCE)

    # Aggregates as the page computes them, sums of the page cells, compared
    # with the same sums built from the reference cells rounded to cents. A
    # cell whose exact value lies on a half cent may legitimately be rounded
    # either way, so each such tie widens its aggregates by exactly one cent.
    def aggregates(cells: dict, category_name) -> dict[str, dict[str, Decimal]]:
        out: dict[str, dict[str, Decimal]] = {
            "month": defaultdict(Decimal),
            "country": defaultdict(Decimal),
            "product": defaultdict(Decimal),
            "category": defaultdict(Decimal),
            "total": defaultdict(Decimal),
        }
        for (m, c, p), v in cells.items():
            for dim, key in (
                ("month", m),
                ("country", c),
                ("product", p),
                ("category", category_name(p)),
                ("total", ""),
            ):
                out[dim][key] += v
        return out

    category_of = dict(web["products"])
    ref_category = ref["category_of"].get
    rounded = {k: v.quantize(CENT) for k, v in ref["cells"].items()}
    ties = {
        k: Decimal(abs(v - rounded[k]) == CENT / 2) for k, v in ref["cells"].items()
    }
    page = aggregates(web_cells, lambda p: web["categories"][category_of[p]])
    expected = aggregates(rounded, ref_category)
    tie_count = aggregates(ties, ref_category)
    for dim, values in expected.items():
        for key, value in values.items():
            bound = TOLERANCE + CENT * tie_count[dim][key]
            label = f"page {dim} {key}".rstrip()
            report.number(label, value, page[dim].get(key), bound)
    print(
        f"Page: total from cells {page['total']['']}, from rounded reference "
        f"cells {expected['total']['']}, exact reference "
        f"{ref['total'].quantize(CENT)}, {tie_count['total']['']} half-cent ties"
    )


def german_number(text: str) -> Decimal:
    return Decimal(text.replace(".", "").replace(",", "."))


def german_date(text: str) -> date:
    day, month, year = re.fullmatch(r"(\d+)\. (\w+) (\d{4})", text).groups()
    return date(int(year), MONTH_DE[month], int(day))


def table_rows(text: str, first_header: str) -> list[list[str]]:
    """Body rows of the Markdown table whose header starts with `first_header`."""
    lines = text.splitlines()
    for i, line in enumerate(lines):
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if cells and cells[0] == "Rang" and cells[1] == first_header:
            rows = []
            for body in lines[i + 2 :]:
                if not body.startswith("|"):
                    break
                rows.append([c.strip() for c in body.strip().strip("|").split("|")])
            return rows
    return []


def check_protocol(ref: dict, report: Report) -> None:
    text = PROTOCOL.read_text(encoding="utf-8")

    def phrase(label: str, pattern: str):
        match = re.search(pattern, text)
        if not match:
            report.failures.append(f"protocol: phrase for {label} not found")
        return match

    if m := phrase("orders and lines", r"(\d+) Bestellungen mit (\d+) Positionen"):
        report.equal("protocol orders", ref["orders"], int(m.group(1)))
        report.equal("protocol lines", ref["lines"], int(m.group(2)))
    if m := phrase("unshipped", r"(\d+) noch nicht versandte Bestellungen"):
        report.equal("protocol unshipped", ref["unshipped"], int(m.group(1)))
    if m := phrase("date range", r"vom (\d+\. \w+ \d{4}) bis (\d+\. \w+ \d{4})"):
        report.equal("protocol first date", ref["first"], german_date(m.group(1)))
        report.equal("protocol last date", ref["last"], german_date(m.group(2)))
    if m := phrase("total", r"Gesamtumsatz beträgt ([\d.]+,\d{2})"):
        report.number("protocol total", ref["total"], german_number(m.group(1)))

    for header, dim, rename in (
        ("Produkt", "product", lambda n: n),
        ("Lieferland", "country", lambda n: COUNTRY_DE.get(n, n)),
    ):
        rows = table_rows(text, header)
        report.equal(f"protocol {dim} table rows", 5, len(rows))
        ranking = sorted(ref[dim].items(), key=lambda kv: -kv[1])
        for rank, name, amount, share in rows:
            key = rename(name)
            expected_rank = next(
                (i for i, (k, _) in enumerate(ranking, 1) if k == key), None
            )
            report.equal(f"protocol rank of {name}", expected_rank, int(rank))
            report.number(
                f"protocol {dim} {name}",
                ref[dim].get(key, Decimal(0)),
                german_number(amount),
            )
            exact = (ref[dim].get(key, Decimal(0)) / ref["total"] * 100).quantize(
                Decimal("0.1")
            )
            report.equal(
                f"protocol share of {name}",
                exact,
                german_number(share.removesuffix(" %")).quantize(Decimal("0.1")),
            )


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    report = Report()
    ref = reference(report)
    print(
        f"Reference: {ref['orders']} orders, {ref['lines']} lines, "
        f"{ref['unshipped']} not shipped, {ref['first']} to {ref['last']}, "
        f"total {ref['total'].quantize(CENT)}"
    )
    print(
        f"Reference: {len(ref['product'])} products, {len(ref['country'])} countries, "
        f"{len(ref['category'])} categories, {len(ref['month'])} months, "
        f"{len(ref['cells'])} cells"
    )
    check_web(ref, report)
    check_protocol(ref, report)
    for failure in report.failures:
        print(f"FAIL {failure}")
    print(f"{report.passed} comparisons passed, {len(report.failures)} failed")
    return 1 if report.failures else 0


if __name__ == "__main__":
    sys.exit(main())
