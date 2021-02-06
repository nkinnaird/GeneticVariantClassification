# Part 1: W3Schools SQL Lab 

*Introductory level SQL*

--

This challenge uses the [W3Schools SQL playground](http://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all). Please add solutions to this markdown file and submit.

1. Which customers are from the UK?

`SELECT Customers.CustomerName FROM Customers WHERE Customers.Country = "UK";`

**Around the Horn, B's Beverages, Consolidated Holdings, Eastern Connection, Island Trading, North/South, Seven Seas Imports**

2. What is the name of the customer who has the most orders?

`SELECT Customers.CustomerName, COUNT(Orders.OrderID) AS NumberOfOrders FROM Customers LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID GROUP BY CustomerName ORDER BY NumberOfOrders DESC;`

**Ernst Handel**

3. Which supplier has the highest average product price?

`SELECT Suppliers.SupplierName, AVG(Products.Price) AS AvgPrice FROM Suppliers LEFT JOIN Products ON Suppliers.SupplierID = Products.SupplierID GROUP BY SupplierName ORDER BY AvgPrice DESC;`

**Aux joyeux ecclésiastiques**

4. How many different countries are all the customers from? (*Hint:* consider [DISTINCT](http://www.w3schools.com/sql/sql_distinct.asp).)

`SELECT DISTINCT(Country) FROM Customers;`

**21**

5. What category appears in the most orders?

```
SELECT Categories.CategoryID, CategoryName, COUNT(Categories.CategoryID) AS NumCatAppearances
FROM OrderDetails
JOIN Products
	On OrderDetails.ProductID = Products.ProductID
JOIN Categories
	On Products.CategoryID = Categories.CategoryID
GROUP BY Categories.CategoryID
ORDER BY NumCatAppearances DESC;
```

**Dairy Products**


6. What was the total cost for each order?

```
SELECT Orders.OrderID, SUM(Quantity*Price) AS TotalOrderPrice
FROM Orders
JOIN OrderDetails
	On Orders.OrderID = OrderDetails.OrderID
JOIN Products
	On OrderDetails.ProductID = Products.ProductID
GROUP BY Orders.OrderID;
```


|OrderID | TotalOrderPrice |
| -- | -- |
| 10248 | 566 |
| 10249 | 2329.25 |
| 10250 | 2267.25 |
**and so on**



7. Which employee made the most sales (by total price)?

```
SELECT Orders.EmployeeID, Employees.FirstName, Employees.LastName, SUM(Quantity*Price) AS TotalSales
FROM Orders
JOIN Employees
	ON Orders.EmployeeID = Employees.EmployeeID
JOIN OrderDetails
	On Orders.OrderID = OrderDetails.OrderID
JOIN Products
	On OrderDetails.ProductID = Products.ProductID
GROUP BY Orders.EmployeeID
ORDER BY TotalSales DESC;
```

**Margaret Peacock**


8. Which employees have BS degrees? (*Hint:* look at the [LIKE](http://www.w3schools.com/sql/sql_like.asp) operator.)

`SELECT FirstName, LastName FROM Employees WHERE Notes LIKE '%BS%';`

**Janet Leverling, Steven Buchanan**

9. Which supplier of three or more products has the highest average product price? (*Hint:* look at the [HAVING](http://www.w3schools.com/sql/sql_having.asp) operator.)

```
SELECT Suppliers.SupplierID, Suppliers.SupplierName, COUNT(Products.ProductID) as NumProducts, AVG(Price) as AvgPrice
FROM Suppliers
JOIN Products
	ON Suppliers.SupplierID = Products.SupplierID
GROUP BY Suppliers.SupplierID
HAVING COUNT(Products.ProductID) > 2
ORDER BY AvgPrice DESC;
```

**Tokyo Traders**


