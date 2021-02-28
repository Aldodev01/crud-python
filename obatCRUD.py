import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    port="3306",
    database="klinik"
)

def getAllData(tabel):
    mycursor = mydb.cursor()
    sql="SELECT * FROM " + tabel
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

def masukinObat():
    mycursor = mydb.cursor()
    sql = "INSERT INTO obat (nama, jumlah, deskripsi) VALUES (%s, %s, %s)"
    nama = input("Masukan nama obat :")
    jumlah = int(input("Masukan Jumlah Obat :"))
    deskripsi = input("Masukan Deskripsi : ")
    val = (nama, jumlah, deskripsi)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Data Sudah Disimpan ke Database")

def editObat(id):
    mycursor = mydb.cursor()
    nama = input("Masukan Nama Obat Baru : ")
    jumlah = int(input("Masukan Jumlah Obat : "))
    sql = "UPDATE obat SET nama = %s, jumlah = %s WHERE id = %s"
    val = (nama, jumlah, id)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Baris yang terpengaruhi")

def hapusObat(id):
    mycursor = mydb.cursor()
    sql = "DELETE FROM obat WHERE id =" +str(id)
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "Data berhasil Dihapus")

def detailObat(id):
    mycursor = mydb.cursor()
    sql = "SELECT * FROM obat WHERE id =" +str(id)
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

detailObat(2)    

# hapusObat(1)

# getAllData("obat")

