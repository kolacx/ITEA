import sqlite3

conn = sqlite3.connect('shop')
cursor = conn.cursor()
result = cursor.execute("SELECT * FROM products")

print(result)


# for i in result:
#     print(i)

print(result.fetchone())
print(result.fetchone()) # po odnomy

print(result.fetchall()) # spisok iz kortegey

conn.close()