import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="cobapython1"
)

cursor = db.cursor()
sql = "INSERT INTO makanan (nama, jenis, harga) VALUES (%s, %s, %s)"
values = [
  ("Roti bakar", "bakar", 10000),
  ("Martabak keju", "goreng", 20000),
  ("Ayam goreng", "goreng", 15000),
  ("Mie soto", "rebus", 8000),
  ("Soto ayam", "rebus", 12000)
  
]

for val in values:
  cursor.execute(sql, val)
  db.commit()

print("{} data ditambahkan".format(len(values)))