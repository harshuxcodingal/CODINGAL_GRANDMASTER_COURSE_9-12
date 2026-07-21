CREATE DATABASE Codingal;
USE Codingal;

CREATE TABLE Supplier(
    SupplierID INT PRIMARY KEY,
    SupplierName VARCHAR(50),
    City VARCHAR(30),
    Country VARCHAR(30),
    Phone VARCHAR(15)
);

INSERT INTO Supplier VALUES
(101,'ABC Traders','Pune','India','9876543210'),
(102,'XYZ Suppliers','Mumbai','India','9876543211'),
(103,'Fresh Foods','Delhi','India','9876543212'),
(104,'Global Tech','Bangalore','India','9876543213'),
(105,'Quality Goods','Nagpur','India','9876543214');

SELECT * FROM Supplier;