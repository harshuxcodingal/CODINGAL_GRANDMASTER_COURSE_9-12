CREATE TABLE Employee(
    EmpID INT PRIMARY KEY,
    Name VARCHAR(40),
    Department VARCHAR(30),
    Salary INT
);

INSERT INTO Employee VALUES
(1,'Raj','IT',50000),
(2,'Neha','HR',45000),
(3,'Amit','IT',60000),
(4,'Riya','Sales',40000),
(5,'Karan','HR',47000);

SELECT Department,COUNT(*) AS Employees
FROM Employee
GROUP BY Department;

SELECT Department,AVG(Salary)
FROM Employee
GROUP BY Department;

SELECT Department,SUM(Salary)
FROM Employee
GROUP BY Department;

SELECT Department,AVG(Salary)
FROM Employee
GROUP BY Department
HAVING AVG(Salary)>45000;

SELECT * FROM Employee
ORDER BY Salary DESC;