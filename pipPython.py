import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    port="3306",
    database="klinik"
)
mycursor=mydb.cursor()
sql="SELECT * FROM obat"
mycursor.execute(sql)
myresult=mycursor.fetchall()

for x in myresult:
    print(x[2:3])

sql = "INSERT INTO obat (nama, jumlah, deskripsi) VALUES (%s, %s, %s)"
nama = input("Masukan nama obat : ")
jumlah = int(input("Masukan jumlah obat : "))
deskripsi = input("Masukan Deskripsi : ")
val = (nama, jumlah, deskripsi)
mycursor.execute(sql, val)
mydb.commit()

print(mycursor.rowcount,"Data sudah disimpan ke Database")
    
print(mydb)