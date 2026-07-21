import sqlite3

conn=sqlite3.connect("company.db")
cursor=conn.cursor()

cursor.execute("""
SELECT name AS Employee_Name
FROM Employee
""")

for row in cursor.fetchall():
    print(row)

conn.close()