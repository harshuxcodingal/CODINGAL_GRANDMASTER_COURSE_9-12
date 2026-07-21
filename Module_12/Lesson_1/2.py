CREATE TABLE Salesman(
    SalesmanID INT PRIMARY KEY,
    Name VARCHAR(50),
    City VARCHAR(30),
    Commission DECIMAL(4,2)
);

INSERT INTO Salesman VALUES
(5001,'James','New York',0.15),
(5002,'Nail','Paris',0.13),
(5003,'Pit Alex','London',0.11),
(5004,'Paul','Rome',0.12);

CREATE TABLE Orders(
    OrderNo INT PRIMARY KEY,
    PurchaseAmt DECIMAL(10,2),
    OrderDate DATE,
    CustomerID INT,
    SalesmanID INT
);

INSERT INTO Orders VALUES
(70001,150.50,'2024-01-10',3002,5002),
(70002,270.65,'2024-02-15',3005,5001),
(70003,65.26,'2024-03-18',3001,5003),
(70004,110.50,'2024-04-22',3004,5004);

SELECT * FROM Salesman;
SELECT * FROM Orders;