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

conn.commit()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

print(cursor.fetchall())

conn.close()