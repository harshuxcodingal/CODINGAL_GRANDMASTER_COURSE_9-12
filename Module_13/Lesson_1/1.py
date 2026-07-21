import sqlite3

conn = sqlite3.connect("school.db")

print("Database created successfully!")

conn.close()