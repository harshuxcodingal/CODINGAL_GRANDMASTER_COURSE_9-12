CREATE TABLE Nobel(
    Year INT,
    Subject VARCHAR(30),
    Winner VARCHAR(50),
    Country VARCHAR(30)
);

INSERT INTO Nobel VALUES
(2020,'Physics','Roger Penrose','UK'),
(2020,'Chemistry','Jennifer Doudna','USA'),
(2021,'Physics','Syukuro Manabe','Japan'),
(2022,'Peace','Ales Bialiatski','Belarus'),
(2023,'Chemistry','Moungi Bawendi','USA');

SELECT * FROM Nobel;

SELECT Subject,COUNT(*) FROM Nobel
GROUP BY Subject;

SELECT Country,COUNT(*) FROM Nobel
GROUP BY Country;

SELECT Country,COUNT(*) FROM Nobel
GROUP BY Country
HAVING COUNT(*)>1;

SELECT * FROM Nobel
ORDER BY Year DESC;