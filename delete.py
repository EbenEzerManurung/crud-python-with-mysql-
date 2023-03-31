import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="cobapython1"
)

cursor = db.cursor()
sql = "DELETE FROM makanan WHERE nama = 'Nasi goreng'"
cursor.execute(sql)

db.commit()

print("{} data dihapus".format(cursor.rowcount))