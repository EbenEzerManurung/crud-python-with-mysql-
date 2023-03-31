import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="cobapython1"
)

cursor = db.cursor()
sql = "INSERT INTO makanan (nama, jenis, harga) VALUES (%s, %s, %s)"
val = ("Nasi goreng", "goreng", 12000)
cursor.execute(sql, val)

db.commit()

print("{} data ditambahkan".format(cursor.rowcount))