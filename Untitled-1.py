import mysql.connector 
conn = mysql.connector.connect(host="localhost",port=3306,user="root",password="",database="menumasakan")
from datetime import datetime
from clear import Tampilan
cursor=conn.cursor()

class Akun :
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def updateData(self):
        username = input('masukkan username: ')
        email = input('masukkan email: ')
        alamat = input('masukkan alamat: ')
        nomorHp = input('masukkan nomer HP: ')
        password = input('masukkan password: ')
        query = "update registrasi set username='{}', password='{}', email='{}', alamat='{}', nomorHp={} where username='{}'".format(username, password, email, alamat, nomorHp, self.username)
        cursor.execute(query)
        conn.commit()

class Konsumen(Akun) :
    def __init__ (self):
        pass   
        
    def Registrasi(self):
        username = input('masukkan username: ')
        email = input('masukkan email: ')
        alamat = input('masukkan alamat: ')
        nomorHp = input('masukkan nomer HP: ')
        password = input('masukkan password: ')
        query = "insert into registrasi values('{}','{}','{}','{}',{})".format(username, password, email, alamat, nomorHp)
        cursor.execute(query)
        conn.commit()

    def tampilkanMasakan(self):
        query="SELECT * FROM tabelmenu"
        cursor.execute(query)
        data_masakan=cursor.fetchall()
        for data in data_masakan:
            print(data)
        
    def tambahPesanan(self):
        Nama_konsumen = input('masukkan nama anda :')
        JumlahPemesanan = int(input('masukkan jumlah pesanan: '))
        AlamatPengiriman = input('masukkan alamat pengiriman: ')
        waktuPesan = datetime.now()
        Nama_masakan = ""
        Level = ""
        jumlah = ""
        totalHarga = 0
        for x in range(JumlahPemesanan):
            masakan = str(input('masukkan masakan yang anda inginkan : '))
            harga_masakan = int(input('masukkan harga makanan : '))
            levelMasakan = input('masukkan level yang anda inginkan :')
            jumlahMasakan = int(input('jumlah pesanan : '))
            jumlahPesanan = input('jumlah makanan : ')
            jumlahHarga = harga_masakan*jumlahMasakan
            Nama_masakan = Nama_masakan+", " +masakan
            Level = Level+", " +levelMasakan
            jumlah = jumlah+", "+jumlahPesanan
            totalHarga += jumlahHarga
        Nama_masakan = Nama_masakan[2:]
        jumlah = jumlah[2:]
        Level = Level[2:]
        query = "insert into pemesanan values('{}','{}','{}','{}','{}','{}',{},'{}')".format(Nama_konsumen, AlamatPengiriman, Nama_masakan, Level, JumlahPemesanan, jumlah, totalHarga, waktuPesan)
        cursor.execute(query)
        conn.commit()

    def tampillkanRiwayatPemesanan(self):
        Nama_konsumen = input('masukkan nama anda :')
        query="SELECT * FROM pemesanan where Nama_konsumen='{}' ".format(Nama_konsumen)
        cursor.execute(query)
        data_masakan=cursor.fetchall()
        for data in data_masakan:
            print(data)

class Penjual(Akun):
    def __init__(self, Nama_masakan):
        self.Nama_masakan=Nama_masakan

    def updateMasakan(self):
        Nama_masakan = input('masukkan nama masakan : ')
        Harga = input('masukkan harga menu : ')
        Stok = input('Jumlah masakan : ')
        Level = input ('masukkan bos : ')
        Khasiat = input('masukkan khasiat makanannya : ')
        Keterangan = input('Keterangan mengenai makanan : ')
        query = "update tabelmenu set Nama_masakan='{}', Harga={}, Stok={}, Level='{}', Khasiat='{}', Keterangan='{}' where Nama_masakan='{}'".format(Nama_masakan, Harga, Stok, Level, Khasiat, Keterangan, self.Nama_masakan)
        cursor.execute(query)
        conn.commit()

class Penjual1(Penjual):
    def __init__(self):
        pass

    def tambahMasakan(self):  
        Nama_masakan = input('masukkan nama masakan : ')
        Harga = input('masukkan harga menu : ')
        Stok = input('Jumlah masakan : ')
        Level = input('Tambahkan level: ')
        Khasiat = input('Khasiat makanan : ')
        Keterangan = input('Keterangan mengenai makanan : ')
        query = "insert into tabelmenu values('{}',{},{},'{}','{}','{}')".format(Nama_masakan, Harga, Stok, Level, Khasiat, Keterangan)
        cursor.execute(query)
        conn.commit()

    def hapusMasakan(self):
        Nama_masakan = input('masukkan nama masakan yang ingin dihapus :')
        query="delete from tabelmenu where Nama_masakan='{}'".format(Nama_masakan)
        cursor.execute(query)
        conn.commit()

    def hapusAkun(self):
        username = input('masukkan username: ')
        query="delete from registrasi where username='{}'".format(username)
        cursor.execute(query)
        conn.commit()
 
    def tampilkanPesanan(self):
        query="SELECT * FROM pemesanan"
        cursor.execute(query)
        data_pesanan=cursor.fetchall()
        for data in data_pesanan:
            print(data)

def jalankanProgram():
    print("============================")
    print("""Pilihan Menu
    1. Penjual
    2. Konsumen
    3. Exit
    ============================""")   
    menu = int(input("input angka pilihan diatas : "))
    if menu == 1:
        penjualInput = int(input("\n1. Tambah Masakan \n2. Update Data \n3. Hapus Akun \n4. Update Masakan \n5. Hapus Masakan \n6. Tampikan Pesanan \ninput angka pilihan diatas : "))
        if penjualInput == 1:
            Penjual1().tambahMasakan()
            Tampilan.bersih()
            print("Masakan berhasil ditambahkan")
        elif penjualInput == 2 :
            Akun('as','as').updateData()
            Tampilan.bersih()
            print("Data berhasil diganti")
        elif penjualInput == 3 :
            Penjual1().hapusAkun()
            Tampilan.bersih()
            print("Data berhasil dihapus")
        elif penjualInput == 4 :
            Penjual('girengan').updateMasakan()
            Tampilan.bersih()
            print("Masakan berhasil diganti")
        elif penjualInput == 5 :
            Penjual1().hapusMasakan()
            Tampilan.bersih()
            print("Makanan berhasil dihapus")
        elif penjualInput == 6 :
            Penjual1().tampilkanPesanan()
    elif menu == 2:
        konsumenInput = int(input("\n1. Registrasi \n2. Tampilkan Masakan \n3. Tambah Pesanan \n4. Tampilkan Riwayat Pemesanan  \ninput angka pilihan diatas : "))
        if konsumenInput == 1:
            Konsumen().Registrasi()
            Tampilan.bersih()
            print("Data berhasil ditambahkan")
        elif konsumenInput == 2 :
            Konsumen().tampilkanMasakan()
        elif konsumenInput == 3 :
            Konsumen().tambahPesanan()
            Tampilan.bersih()
            print("Pesanan anda berhasil ditambahkan")
        elif konsumenInput == 4 :
            Konsumen().tampillkanRiwayatPemesanan()
    elif menu == 3 :
        exit("Selamat datang kembali")
        Tampilan.bersih()
    return jalankanProgram()
jalankanProgram()
   
conn.commit()
cursor.close()
conn.close()






