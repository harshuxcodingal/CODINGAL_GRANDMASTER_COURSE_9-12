CREATE TABLE Product(
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(50),
    Price INT,
    Category VARCHAR(30)
);

INSERT INTO Product VALUES
(101,'Laptop',65000,'Electronics'),
(102,'Mouse',800,'Electronics'),
(103,'Shoes',2500,'Fashion'),
(104,'Mobile',22000,'Electronics'),
(105,'Watch',3000,'Accessories');

SELECT * FROM Product;

SELECT * FROM Product WHERE Price>2000;

SELECT * FROM Product WHERE Category='Electronics';

SELECT * FROM Product WHERE Price<5000;

SELECT * FROM Product ORDER BY Price DESC;