import sqlite3

conn = sqlite3.connect('shop')
cursor = conn.cursor()

query = "SELECT title FROM products WHERE id=?"

cursor.execute(query, [1])

print(cursor.fetchall())

conn.close()