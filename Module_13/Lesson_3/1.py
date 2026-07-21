import sqlite3

conn=sqlite3.connect("school.db")
cursor=conn.cursor()

cursor.execute("UPDATE Student SET marks=95 WHERE id=1")

cursor.execute("DELETE FROM Student WHERE id=3")

conn.commit()

cursor.execute("SELECT * FROM Student")

for row in cursor.fetchall():
    print(row)

conn.close()