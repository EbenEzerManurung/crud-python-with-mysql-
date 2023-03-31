import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="cobapython1"
)

cursor = db.cursor()

# sql = "UPDATE makanan SET nama = 'Mie goreng telor' WHERE nama = 'Nasi goreng'"

sql = "UPDATE makanan SET nama= 'Lontongs sayur', harga=8000 WHERE nama = 'Lontong sayur'"


cursor.execute(sql)

db.commit()

print("{} data berhasil telah diubah".format(cursor.rowcount))