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
    sql = "SELECT * FROM " + tabel
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

def masukanDokter():
    mycursor = mydb.cursor()
    sql = "INSERT INTO dokter (nama, specialist, alamat, no_telp, jenis_kelamin) VALUES (%s, %s, %s, %s, %s)"
    nama = input("Masukan Nama Dokter : ")
    specialist = input("Masukan Specialist Dokter : ")
    alamat = input("Masukan Alamat Dokter : ")
    no_telp = int(input("Masukan No Telp Dokter : "))

    laki = "Laki - laki"
    print(laki)
    perempuan = "Perempuan"
    print(perempuan)
    jenis_kelamin = input("Masukan jenis kelamin Dokter : ")
    if jenis_kelamin == laki:
        print(laki)
    else : 
        print(perempuan)
    
    val = (nama, specialist, alamat, no_telp, jenis_kelamin)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Data Dokter telah Ditambahkan")

def editDokter(id):
    mycursor = mydb.cursor()
    nama = input("Masukan Nama Dokter : ")
    specialist = input("Masukan Specialist Dokter : ")
    alamat = input("Masukan Alamat Dokter : ")
    no_telp = int(input("Masukan No Telp Dokter : "))

    laki = "Laki - laki"
    print(laki)
    perempuan = "Perempuan"
    print(perempuan)
    jenis_kelamin = input("Masukan jenis kelamin Dokter : ")
    if jenis_kelamin == laki:
        print(laki)
    else : 
        print(perempuan)

    sql = "UPDATE dokter SET nama = %s, specialist = %s, alamat = %s, no_telp = %s, jenis_kelamin = %s WHERE id = %s"
    val = (nama, specialist, alamat, no_telp, jenis_kelamin, id)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Data Dokter sudah diperbarui")

def hapusDokter(id):
    mycursor = mydb.cursor()
    sql = "DELETE FROM dokter WHERE id =" + str(id)
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "Data Dokter sudah Dihapus")

def detailDokter(id): 
    mycursor = mydb.cursor()
    sql = "SELECT * FROM dokter WHERE id =" + str(id)
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult: 
        print(x)

detailDokter(3)

# getAllData("dokter")