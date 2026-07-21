CREATE TABLE Library(
    BookID INT PRIMARY KEY,
    BookName VARCHAR(50),
    Author VARCHAR(50),
    Price INT
);

INSERT INTO Library VALUES
(1,'Python Basics','Guido',450),
(2,'SQL Guide','Codd',500),
(3,'Java Programming','James',600),
(4,'HTML & CSS','John',300),
(5,'C++','Bjarne',550);

SELECT * FROM Library;

SELECT * FROM Library
WHERE Price>500;

SELECT AVG(Price) FROM Library;

SELECT MAX(Price) FROM Library;

SELECT * FROM Library
ORDER BY Price DESC;