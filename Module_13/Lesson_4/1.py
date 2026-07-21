import sqlite3

conn=sqlite3.connect("employee.db")
cursor=conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Employee(
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
salary INTEGER CHECK(salary>0),
email TEXT UNIQUE
)
""")

print("Table Created")

conn.commit()
conn.close()