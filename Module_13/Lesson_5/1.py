import sqlite3

conn=sqlite3.connect("company.db")
cursor=conn.cursor()

cursor.execute("""
CREATE TABLE Department(
dept_id INTEGER PRIMARY KEY,
dept_name TEXT
)
""")

cursor.execute("""
CREATE TABLE Employee(
emp_id INTEGER PRIMARY KEY,
name TEXT,
dept_id INTEGER
)
""")

cursor.execute("INSERT INTO Department VALUES(1,'HR')")
cursor.execute("INSERT INTO Department VALUES(2,'IT')")

cursor.execute("INSERT INTO Employee VALUES(101,'Amit',1)")
cursor.execute("INSERT INTO Employee VALUES(102,'Neha',2)")
cursor.execute("INSERT INTO Employee VALUES(103,'Rahul',1)")

conn.commit()

cursor.execute("""
SELECT Employee.name,Department.dept_name
FROM Employee
INNER JOIN Department
ON Employee.dept_id=Department.dept_id
""")

for row in cursor.fetchall():
    print(row)

conn.close()