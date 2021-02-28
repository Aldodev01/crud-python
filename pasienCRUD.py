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

def masukanPasien():
    mycursor = mydb.cursor()
    sql = "INSERT INTO pasien (nama, tanggal_masuk, tanggal_lahir, jenis_kelamin, alamat, no_telp) VALUES (%s, %s, %s, %s, %s, %s)"
    nama = input("Masukan Nama Pasien : ")
    print(" Format : Tahun-bulan-tanggal")
    tanggal_masuk = input("Masukan Tanggal Masuk : ")
    print(" Format : Tahun-bulan-tanggal")
    tanggal_lahir = input("Masukan Tanggal Lahir : ")


    laki = "Laki - laki"
    print(laki)
    perempuan = "Perempuan"
    print(perempuan)
    jenis_kelamin = input("Masukan jenis kelamin Pasien : ")
    if jenis_kelamin == laki:
        print(laki)
    else : 
        print(perempuan)

    alamat = input("Masukan Alamat Pasien : ")

    no_telp = input("Masukan No Telp Pasien : ")

    val = (nama, tanggal_masuk, tanggal_lahir, jenis_kelamin, alamat, no_telp)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Data Pasien telah diTambahkan")

def editPasien(id):
    mycursor = mydb.cursor()
    nama = input("Masukan nama Pasien : ")
    tanggal_masuk = input("Masukan tanggal masuk Pasien : ")
    tanggal_lahir = input("Masukan tanggal lahir Pasien : ")
    laki = "Laki - laki"
    print(laki)
    perempuan = "Perempuan"
    print(perempuan)
    jenis_kelamin = input("Masukan jenis kelamin Pasien : ")
    if jenis_kelamin == laki:
        print(laki)
    else : 
        print(perempuan)
    alamat = input("Masukan Alamat Pasien : ")
    no_telp = input("Masukan No telp Pasien : ")

    sql = "UPDATE pasien SET nama = %s, tanggal_masuk = %s, tanggal_lahir = %s, jenis_kelamin = %s, alamat = %s, no_telp = %s WHERE id = %s"
    val = (nama, tanggal_masuk, tanggal_lahir, jenis_kelamin, alamat, no_telp, id)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Data Pasien sudah diperbarui")


editPasien(3)

# masukanPasien()

getAllData("pasien")