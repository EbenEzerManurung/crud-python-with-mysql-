import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="cobapython1"
)

cursor = db.cursor()
sql = "SELECT * FROM makanan"
cursor.execute(sql)

result = cursor.fetchone()
# result = cursor.fetchall() -> many

print(result)