CREATE TABLE Products(
    ID INT PRIMARY KEY,
    ProductName VARCHAR(40),
    Price INT
);

INSERT INTO Products VALUES
(1,'Pen',20),
(2,'Book',150),
(3,'Bag',900),
(4,'Laptop',60000),
(5,'Mouse',700);

SELECT COUNT(*) FROM Products;

SELECT SUM(Price) FROM Products;

SELECT AVG(Price) FROM Products;

SELECT MAX(Price) FROM Products;

SELECT MIN(Price) FROM Products;