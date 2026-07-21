import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Student(
id INTEGER PRIMARY KEY,
name TEXT,
age INTEGER,
marks INTEGER
)
""")

cursor.execute("INSERT INTO Student VALUES(1,'Amit',16,90)")
cursor.execute("INSERT INTO Student VALUES(2,'Neha',17,85)")
cursor.execute("INSERT INTO Student VALUES(3,'Rahul',16,75)")

conn.commit()

cursor.execute("SELECT * FROM Student")

for row in cursor.fetchall():
    print(row)

conn.close()