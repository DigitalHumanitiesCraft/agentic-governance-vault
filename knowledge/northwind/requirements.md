---
title: Northwind revenue analysis, requirements
type: anforderungen
language: en
tags:
  - bereich/projekt
  - feld/projekte
related:
  - "[[2026-11-05_northwind-anfrage]]"
---
# Northwind revenue analysis, requirements

The analysis tool consists of the script `scripts/northwind_umsatz.py` and the revenue page `dashboard/northwind/`. It answers the question of the exercise inquiry in [the Northwind protocol](../../protokolle/2026-11-05_northwind-anfrage.md), which products and delivery countries bring the most revenue, from the exercise data described in [the data document](data.md). Each requirement below states what the tool fulfils, how the code meets it and how it is checked. `scripts/northwind_check.py` is the automated check, the other checks are reading the code or opening the page.

## R1 Data minimisation

The analysis reads only the data the revenue question needs. The script opens `bestellungen.xlsx` and `produkte.xlsx` and of them only the sheets Orders, Order Details, Products and Categories. Of each sheet it keeps only the named columns, of Orders `OrderID`, `OrderDate`, `ShippedDate` and `ShipCountry`. It never opens `kunden.xlsx` or `mitarbeitende.xlsx`, and it does not read the sheet Suppliers. The country of a sale is the delivery country of the order, so Customers is not needed.

Check: the calls of `_sheets` in `revenue()` name every workbook, sheet and column the script reads, and a search of the script for `kunden` and `mitarbeitende` finds them only in the docstring. `northwind_check.py` keeps to the same four sheets.

## R2 Local computation

All computation runs on the local machine, without an AI service or any network access. The script uses the standard library and `openpyxl` only, and the page loads its data from a local file.

Check: the imports of both scripts, and the absence of any URL other than the SVG namespace in `index.html` and `app.js`.

## R3 Sums only on the page

The page holds only aggregated revenue, never an order, a customer or a person. `--web` writes `dashboard/northwind/data.js` with the sums per month, delivery country and product, rounded to cents, together with the category of each product, the number of orders, lines and unshipped orders, the first and last order date and the total. Order IDs, customer IDs, employee IDs and addresses do not enter it.

Check: the keys of `window.NORTHWIND` in `data.js`, and the function `_write_web`, which builds the object from the aggregated cells only.

## R4 Correct and traceable figures

Revenue of an order line is `UnitPrice * Quantity * (1 - Discount)` with the price of the order line. Orders not yet shipped count as booked sales, and their number is shown so the reader can judge. A line whose order, product or date cannot be resolved is reported and left out of every sum, and the script then exits with status 1. The method is stated on the page under "Wie gerechnet wurde" and in the protocol.

Check: `northwind_check.py` recomputes every key figure with its own code in decimal arithmetic and compares it with `data.js` and with the figures in the protocol. It covers the total, the number of orders, lines and unshipped orders, the date range, every cell of month, country and product, the sums per product, country, category and month, and the five products and five countries in the protocol with rank, amount and share. It exits with status 1 on any deviation above 0.01, on a broken key or a missing order date, and still prints every failure in those cases. Each cell in `data.js` must be whole cents and a correct rounding of the exact value, at most half a cent away, so a systematic shift below a cent is caught at cell level. Aggregates on the page are sums of these cells; the check compares each with the same sum built from the reference cells rounded to cents, within 0.01 plus one cent for every cell whose exact value lies on a half cent and may therefore round either way.

## R5 Linked filters

One selection of delivery country, category and product filters every chart. A chart is not filtered by its own dimension, so its bars stay comparable and the selected bar is drawn in a darker step. Choosing a category limits the product list to that category and clears a selected product. The selection appears as removable chips, stays in the URL hash and survives a reload. Unknown values in the hash are dropped.

Check: in the browser, select a country, a category and a product in turn and compare the tiles and the other charts. Reload the page with the hash in place, and edit the hash to an unknown value.

## R6 Partial months shown as partial

The data begins on 4 July 1996 and ends on 6 May 1998, so the first and the last month are incomplete. The monthly line draws the last segment dashed and its end marker pale, and its tooltip says that the month is incomplete. A note above the chart names both partial months. Comparisons by calendar year are not offered, because 1996 and 1998 are incomplete.

Check: in the browser, the dashed last segment and the tooltip on May 1998. The month list in `data.js` is compared with the reference by `northwind_check.py`.

## R7 Accessibility

The page is usable by keyboard and screen reader. Every bar is a button with `aria-pressed` for the selected state, and after a click focus returns to the same control or to the filter bar. The filter bar is a live region. The monthly chart has an accessible name and a table view with the same values. Focus is visible through `:focus-visible`. All text is inserted with `textContent`, and the layout reflows to a single column on narrow screens. The page is German, declared with `lang="de"`.

Check: tab through the page and operate every filter by keyboard, open the table view, and narrow the window to phone width.

## R8 Use by double click

The page works when opened from the file system and when served over HTTP. `data.js` and `app.js` are classic scripts, and the data is a global object, so no `fetch` and no module loading is needed. No library is loaded from a CDN. Without `data.js` the page states how to build it.

Check: open `dashboard/northwind/index.html` by double click and over a local server, and confirm that both show the same figures.
