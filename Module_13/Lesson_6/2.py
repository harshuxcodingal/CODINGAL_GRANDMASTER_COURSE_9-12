import sqlite3

conn=sqlite3.connect("company.db")
cursor=conn.cursor()

cursor.execute("""
SELECT name
FROM Employee
WHERE dept_id=
(
SELECT dept_id
FROM Department
WHERE dept_name='HR'
)
""")

for row in cursor.fetchall():
    print(row)

conn.close()