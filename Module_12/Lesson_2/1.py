CREATE TABLE Student(
    RollNo INT PRIMARY KEY,
    Name VARCHAR(50),
    Age INT,
    Marks INT,
    City VARCHAR(30)
);

INSERT INTO Student VALUES
(1,'Amit',16,85,'Pune'),
(2,'Sneha',17,92,'Mumbai'),
(3,'Rahul',16,75,'Delhi'),
(4,'Neha',17,88,'Pune'),
(5,'Karan',16,65,'Nagpur');

SELECT * FROM Student;

SELECT * FROM Student WHERE Marks>80;

SELECT * FROM Student WHERE City='Pune';

SELECT * FROM Student WHERE Age=16;

SELECT * FROM Student WHERE Marks BETWEEN 70 AND 90;

SELECT * FROM Student WHERE Name LIKE 'A%';

SELECT * FROM Student ORDER BY Marks DESC;