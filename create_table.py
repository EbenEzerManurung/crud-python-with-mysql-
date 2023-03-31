import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="cobapython1"
)

cursor = db.cursor()
sql = """CREATE TABLE makanan (
  customer_id INT AUTO_INCREMENT PRIMARY KEY,
  nama VARCHAR(255),
  jenis Varchar(255),
  harga Integer(30)
)
"""
cursor.execute(sql)

print("Tabel customers berhasil dibuat!")