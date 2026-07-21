CREATE TABLE Restaurant(
    ID INT PRIMARY KEY,
    Name VARCHAR(50),
    Borough VARCHAR(30),
    Cuisine VARCHAR(30),
    Rating DECIMAL(3,1)
);

INSERT INTO Restaurant VALUES
(1,'Burger King','Manhattan','Fast Food',4.2),
(2,'Pizza Hut','Brooklyn','Italian',4.0),
(3,'Subway','Queens','Fast Food',3.9),
(4,'Dominos','Bronx','Pizza',4.5),
(5,'Taco Bell','Manhattan','Mexican',4.1);

SELECT * FROM Restaurant;

SELECT * FROM Restaurant
WHERE Borough='Manhattan';

SELECT * FROM Restaurant
WHERE Rating>4;

SELECT Cuisine,COUNT(*)
FROM Restaurant
GROUP BY Cuisine;

SELECT * FROM Restaurant
ORDER BY Rating DESC;