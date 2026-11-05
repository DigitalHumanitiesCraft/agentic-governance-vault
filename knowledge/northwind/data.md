---
title: Northwind exercise data
type: daten
language: en
tags:
  - bereich/projekt
  - feld/projekte
  - thema/datenschutz
related:
  - "[[2026-11-05_northwind-anfrage]]"
---
# Northwind exercise data

The four workbooks in `eingang/` are Excel exports of the Northwind sample database by Microsoft, a fictional wholesaler of fine food and beverages with orders from 4 July 1996 to 6 May 1998. They arrived as attachments of the exercise inquiry recorded in [the Northwind protocol](../../protokolle/2026-11-05_northwind-anfrage.md). Column names and values are unchanged from the sample database, and its licence lies beside them as `eingang/LICENSE-northwind.txt`. Every person and company in the data is fictional, and the exercise treats the files as if they were real.

The data is fixed, so the row counts below describe the dataset and do not change as the work proceeds. They count rows below the header row that hold at least one value. For `kunden.xlsx`, `mitarbeitende.xlsx` and the sheet Suppliers only header rows and row counts were read, never values, so the types of their columns are inferred from the column names and from the published Northwind schema.

## Workbooks and sheets

| Workbook | Sheet | Rows | Content |
| --- | --- | --- | --- |
| `bestellungen.xlsx` | Orders | 830 | One row per order with dates, carrier, freight and delivery address |
| `bestellungen.xlsx` | Order Details | 2155 | One row per order line with price, quantity and discount |
| `produkte.xlsx` | Products | 77 | Product catalogue with category, supplier, list price and stock |
| `produkte.xlsx` | Categories | 8 | Product categories with a description |
| `produkte.xlsx` | Suppliers | 29 | Supplier companies with a contact person |
| `kunden.xlsx` | Customers | 91 | Customer companies with a contact person |
| `kunden.xlsx` | Shippers | 3 | Carriers with a telephone number |
| `mitarbeitende.xlsx` | Employees | 9 | Staff records with personal details and reporting line |

## Columns

Types for Orders, Order Details, Products and Categories were read from the cell values. Integer stands for whole numbers, decimal for numbers that Excel stores as integer or floating point depending on the value, and date for Excel date cells.

### Orders

| Column | Type | Meaning |
| --- | --- | --- |
| `OrderID` | integer | Primary key of the order |
| `CustomerID` | text, five letters | Foreign key to Customers |
| `EmployeeID` | integer | Foreign key to Employees, the person who handled the order |
| `OrderDate` | date | Date of the order, present in every row |
| `RequiredDate` | date | Delivery date the customer asked for |
| `ShippedDate` | date, empty in 21 rows | Shipping date, empty for orders not yet shipped |
| `ShipVia` | integer | Foreign key to Shippers |
| `Freight` | decimal | Freight charge |
| `ShipName` | text | Name of the receiving company |
| `ShipAddress` | text | Street address of delivery |
| `ShipCity` | text | City of delivery |
| `ShipRegion` | text, often empty | Region or state of delivery |
| `ShipPostalCode` | text, sometimes empty | Postal code of delivery |
| `ShipCountry` | text | Delivery country, in English |

### Order Details

| Column | Type | Meaning |
| --- | --- | --- |
| `OrderID` | integer | Foreign key to Orders, part of the primary key |
| `ProductID` | integer | Foreign key to Products, part of the primary key |
| `UnitPrice` | decimal | Price per unit at the time of the order, which may differ from the list price in Products |
| `Quantity` | integer | Number of units |
| `Discount` | decimal between 0 and 1 | Discount as a fraction of the line amount |

### Products

| Column | Type | Meaning |
| --- | --- | --- |
| `ProductID` | integer | Primary key |
| `ProductName` | text | Name of the product, unique |
| `SupplierID` | integer | Foreign key to Suppliers |
| `CategoryID` | integer | Foreign key to Categories |
| `QuantityPerUnit` | text | Packaging unit, such as a number of bottles |
| `UnitPrice` | decimal | Current list price |
| `UnitsInStock` | integer | Units in stock |
| `UnitsOnOrder` | integer | Units ordered from the supplier |
| `ReorderLevel` | integer | Stock level that triggers a reorder |
| `Discontinued` | integer, 0 or 1 | Whether the product is discontinued |

### Categories

| Column | Type | Meaning |
| --- | --- | --- |
| `CategoryID` | integer | Primary key |
| `CategoryName` | text | Name of the category |
| `Description` | text | Short description of the category |

### Suppliers

| Column | Type | Meaning |
| --- | --- | --- |
| `SupplierID` | integer | Primary key |
| `CompanyName` | text | Supplier company |
| `ContactName` | text | Contact person at the supplier |
| `ContactTitle` | text | Job title of the contact person |
| `Address`, `City`, `Region`, `PostalCode`, `Country` | text | Business address |
| `Phone`, `Fax` | text | Business telephone and fax numbers |
| `HomePage` | text | Website of the supplier |

### Customers

| Column | Type | Meaning |
| --- | --- | --- |
| `CustomerID` | text | Primary key, referenced by Orders |
| `CompanyName` | text | Customer company |
| `ContactName` | text | Contact person at the customer |
| `ContactTitle` | text | Job title of the contact person |
| `Address`, `City`, `Region`, `PostalCode`, `Country` | text | Business address |
| `Phone`, `Fax` | text | Telephone and fax numbers |

### Shippers

| Column | Type | Meaning |
| --- | --- | --- |
| `ShipperID` | integer | Primary key, referenced by `Orders.ShipVia` |
| `CompanyName` | text | Carrier company |
| `Phone` | text | Telephone number of the carrier |

### Employees

| Column | Type | Meaning |
| --- | --- | --- |
| `EmployeeID` | integer | Primary key, referenced by Orders |
| `LastName`, `FirstName` | text | Name of the employee |
| `Title`, `TitleOfCourtesy` | text | Job title and form of address |
| `BirthDate` | date | Date of birth |
| `HireDate` | date | Date of hiring |
| `Address`, `City`, `Region`, `PostalCode`, `Country` | text | Private address |
| `HomePhone` | text | Private telephone number |
| `Extension` | text | Internal telephone extension |
| `Notes` | text | Free-text notes on the person |
| `ReportsTo` | integer | Foreign key to Employees, the line manager |

## Keys and relations

The relations below follow from the column names and the published Northwind schema. For the four sheets the revenue analysis reads, `scripts/northwind_check.py` confirms that the primary keys are unique, that the pair of `OrderID` and `ProductID` is unique in Order Details, and that every foreign key among these four sheets resolves. The keys into Customers, Employees, Shippers and Suppliers were not checked, because that would require reading their values.

| From | To | Cardinality |
| --- | --- | --- |
| `Order Details.OrderID` | `Orders.OrderID` | many lines per order |
| `Order Details.ProductID` | `Products.ProductID` | many lines per product |
| `Products.CategoryID` | `Categories.CategoryID` | many products per category |
| `Products.SupplierID` | `Suppliers.SupplierID` | many products per supplier |
| `Orders.CustomerID` | `Customers.CustomerID` | many orders per customer |
| `Orders.EmployeeID` | `Employees.EmployeeID` | many orders per employee |
| `Orders.ShipVia` | `Shippers.ShipperID` | many orders per carrier |
| `Employees.ReportsTo` | `Employees.EmployeeID` | many employees per manager |

Orders carries the delivery address and the delivery country itself, so the country of a sale is available without reading Customers. Order Details carries its own unit price, so revenue needs no price from Products.

## Personal data

The data is fictional, but the exercise classifies it as if it were real, following the data class of personal data in the [governance draft](../governance-entwurf.md).

| Sheet | Columns with personal data | Kind |
| --- | --- | --- |
| Employees | `LastName`, `FirstName`, `Title`, `TitleOfCourtesy`, `BirthDate`, `HireDate`, `Address`, `City`, `Region`, `PostalCode`, `Country`, `HomePhone`, `Extension`, `Notes`, `ReportsTo` | Staff records including date of birth, private address, private telephone and free-text notes, the most sensitive sheet of the set |
| Customers | `ContactName`, `ContactTitle`, `Phone`, `Fax` | Named contact persons with job title and telephone numbers |
| Suppliers | `ContactName`, `ContactTitle`, `Phone`, `Fax` | Named contact persons with job title and telephone numbers |
| Orders | `EmployeeID`, `CustomerID` and the delivery address columns | Pseudonymous link to an employee and to a customer whose contact person is named in Customers. A delivery address can identify a sole trader |

Company names, addresses of companies and the carriers in Shippers are business data. Products, Categories and Order Details hold no personal data. The revenue analysis therefore reads only Orders, Order Details, Products and Categories, and of Orders only `OrderID`, `OrderDate`, `ShippedDate` and `ShipCountry`.

## Questions the data can answer

Questions answerable from Orders, Order Details, Products and Categories alone, without personal data:

- Revenue in total, per product, per category, per delivery country and per month, with revenue per line as `UnitPrice * Quantity * (1 - Discount)`. These figures are on the [revenue page](../../dashboard/northwind/index.html) and are checked by `scripts/northwind_check.py`.
- Quantities sold per product and category, average discount, and the share of lines with a discount.
- Price changes over time, by comparing the order price in Order Details with the list price in Products.
- Order volume and number of lines per month, the number of unshipped orders, delays between order, required and shipping date, and freight per delivery country.
- Stock situation and discontinued products from Products.

Questions that need personal data or the excluded sheets, and therefore a legal basis and, for an external processor, a data processing agreement:

- Revenue per customer, customer ranking, repeat purchases and customer churn, which need `CustomerID` and Customers.
- Revenue and performance per employee, which need `EmployeeID` and Employees.
- Revenue per supplier and contact lists of suppliers, which need Suppliers.

The data cannot answer questions about currency, costs, margins or profit, because it states neither a currency nor purchase prices. Comparisons by calendar year are skewed, because 1996 starts in July and 1998 ends on 6 May.
