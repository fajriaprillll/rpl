from db import Database
from prettytable import from_db_cursor
dbConnect = Database(host='localhost', user='root', passwd='', database='db_peternakan')
dbConnect.connect()

class Peternakan:
    def __init__(self, nama, kontak):
        self.nama = nama
        self.kontak = kontak

class Karyawan(Peternakan) :
    def __init__(self, nama, kontak, namaKaryawan, umur, alamat, jobdesk) :
        super().__init__(nama, kontak)
        self.namaKaryawan = namaKaryawan
        self.alamat = alamat
        self.umur = umur
        self.jobdesk = jobdesk

    def insertKaryawan(self) :
        self.namaKaryawan = str(input("Masukkan Nama Karyawan    : "))
        self.umur         = int(input("Masukkan Umur Karyawan    : "))
        self.alamat       = str(input("Masukkan Alamat Karyawan  : "))
        self.kontak       = str(input("Masukkan No.Telp Karyawan : "))
        self.jobdesk      = str(input("Masukkan Jobdesk Karyawan : "))
        data = {
            "nama_karyawan": self.namaKaryawan,
            "umur": self.umur,
            "alamat_karyawan": self.alamat,
            "no_telp": self.kontak,
            "jobdesk": self.jobdesk
        }
        dbConnect.insert('db_peternakan.karyawan', data)

    def editKaryawan(self, id_karyawan):
        # Mendapatkan data karyawan yang akan diubah
        dbConnect.connect()
        query = "SELECT * FROM db_peternakan.karyawan WHERE id_karyawan=%s"
        values = (id_karyawan,)
        dbConnect.cur.execute(query, values)
        karyawan_data = dbConnect.cur.fetchone()
        dbConnect.close()
        if karyawan_data is not None:
            # Menampilkan data karyawan sebelum diubah
            print("Data Karyawan Sebelum diubah:")
            print("ID         :", karyawan_data[0])
            print("Nama       :", karyawan_data[1])
            print("Umur       :", karyawan_data[2])
            print("Alamat     :", karyawan_data[3])
            print("No.Telp    :", karyawan_data[4])
            print("Jobdesk    :", karyawan_data[5])

            self.namaKaryawan = self.namaKaryawan or karyawan_data[1]
            self.umur    = int(input("Masukkan Umur Karyawan    : ") or karyawan_data[2])
            self.alamat  = str(input("Masukkan Alamat Karyawan  : ") or karyawan_data[3])
            self.kontak  = str(input("Masukkan Kontak Karyawan  : ") or karyawan_data[4])
            self.jobdesk = str(input("Masukkan Jobdesk Karyawan : ") or karyawan_data[5])
            data = {
                "nama_karyawan": self.namaKaryawan,
                "umur": self.umur,
                "alamat_karyawan": self.alamat,
                "no_telp": self.kontak,
                "jobdesk": self.jobdesk
            }
            condition = f"id_karyawan = {id_karyawan}"
            dbConnect.update('db_peternakan.karyawan', data, condition)
            dbConnect.connect()
            query = "SELECT * FROM db_peternakan.karyawan WHERE id_karyawan=%s"
            values = (id_karyawan,)
            dbConnect.cur.execute(query, values)
            karyawan_data = dbConnect.cur.fetchone()
            dbConnect.close()
            
            # Menampilkan data karyawan setelah diubah
            print("\nData Karyawan Setelah diubah:")
            print("ID        :", id_karyawan)
            print("Nama      :", self.namaKaryawan)
            print("Umur      :", self.umur)
            print("Alamat    :", self.alamat)
            print("No.Telp   :", self.kontak)
            print("Jobdesk   :", self.jobdesk)
            print('Data Karyawan Berhasil Di Ubah!')
        else:
            print("ID tidak terdaftar!")
    
    def hapusKaryawan(self, id_karyawan):
        dbConnect.connect()
        query = "SELECT * FROM db_peternakan.karyawan WHERE id_karyawan=%s"
        values = (id_karyawan,)
        dbConnect.cur.execute(query, values)
        karyawan_data = dbConnect.cur.fetchone()
        dbConnect.close()
        if karyawan_data is not None:
            # Menampilkan data karyawan sebelum dihapus
            print("Data Karyawan Sebelum dihapus:")
            print("ID        :", karyawan_data[0])
            print("Nama      :", karyawan_data[1])
            print("Umur      :", karyawan_data[2])
            print("Alamat    :", karyawan_data[3])
            print("No.Telp   :", karyawan_data[4])
            print("Jobdesk   :", karyawan_data[5])

            # Menghapus data karyawan
            condition = f"id_karyawan = {id_karyawan}"
            dbConnect.delete('db_peternakan.karyawan', condition)
            print('Data Karyawan Berhasil Dihapus!')
        else:
            print("ID tidak terdaftar!")

    def tampilkanDataKaryawan(self):
        # Menampilkan semua data karyawan
        query = "SELECT * FROM db_peternakan.karyawan"
        dbConnect.cur.execute(query)

        # Membuat objek PrettyTable
        table = from_db_cursor(dbConnect.cur)

        # Menampilkan PrettyTable
        print("\nData Semua Karyawan:")
        print(table)

class Distributor(Peternakan) :
    def __init__(self, nama, kontak, namaDistributor,  alamat) :
        super().__init__(nama, kontak)
        self.namaDistributor = namaDistributor
        self.alamat = alamat

    def insertDistributor(self) :
        self.namaDistributor = str(input("Masukkan Nama Distributor    : "))
        self.alamat          = str(input("Masukkan Alamat Distributor  : "))
        self.kontak          = str(input("Masukkan No.Telp Distributor : "))
        data = {
            "nama_distributor": self.namaDistributor,
            "alamat_distributor": self.alamat,
            "no_telp": self.kontak
        }
        dbConnect.insert('db_peternakan.distributor', data)

    def editDistributor(self, id_distributor):
        # Mendapatkan data distributor yang akan diubah
        dbConnect.connect()
        query = "SELECT * FROM db_peternakan.distributor WHERE id_distributor=%s"
        values = (id_distributor,)
        dbConnect.cur.execute(query, values)
        distributor_data = dbConnect.cur.fetchone()
        dbConnect.close()
        if distributor_data is not None:
            # Menampilkan data distributor sebelum diubah
            print("Data Distributor Sebelum diubah:")
            print("ID         :", distributor_data[0])
            print("Nama       :", distributor_data[1])
            print("Alamat     :", distributor_data[2])
            print("No.Telp    :", distributor_data[3])

            self.namaDistributor = self.namaDistributor or distributor_data[1]
            self.alamat = str(input("Masukkan Alamat Distributor  : ") or distributor_data[2])
            self.kontak = str(input("Masukkan No.Telp Distributor : ") or distributor_data[3])
            data = {
            "nama_distributor": self.namaDistributor,
            "alamat_distributor": self.alamat,
            "no_telp": self.kontak
            }
            condition = f"id_distributor = {id_distributor}"
            dbConnect.update('db_peternakan.distributor', data, condition)
            dbConnect.connect()
            query = "SELECT * FROM db_peternakan.distributor WHERE id_distributor=%s"
            values = (id_distributor,)
            dbConnect.cur.execute(query, values)
            distributor_data = dbConnect.cur.fetchone()
            dbConnect.close()
            
            # Menampilkan data distributor setelah diubah
            print("\nData Distributor Setelah diubah:")
            print("ID        :", id_distributor)
            print("Nama      :", self.namaDistributor)
            print("Alamat    :", self.alamat)
            print("No.Telp   :", self.kontak)
            print('Data Distributor Berhasil Di Ubah!')
        else:
            print("ID tidak terdaftar!")
    
    def hapusDistributor(self, id_distributor):
        dbConnect.connect()
        query = "SELECT * FROM db_peternakan.distributor WHERE id_distributor=%s"
        values = (id_distributor,)
        dbConnect.cur.execute(query, values)
        distributor_data = dbConnect.cur.fetchone()
        dbConnect.close()
        if distributor_data is not None:
            # Menampilkan data distributor sebelum dihapus
            print("Data Distributor Sebelum dihapus:")
            print("ID         :", distributor_data[0])
            print("Nama       :", distributor_data[1])
            print("Alamat     :", distributor_data[2])
            print("No.Telp    :", distributor_data[3])

            # Menghapus data distributor
            condition = f"id_distributor = {id_distributor}"
            dbConnect.delete('db_peternakan.distributor', condition)
            print('Data Distributor Berhasil Dihapus!')
        else:
            print("ID tidak terdaftar!")

    def tampilkanDataDistributor(self):
        # Menampilkan semua data distributor
        dbConnect.connect()
        query = "SELECT * FROM db_peternakan.distributor"
        dbConnect.cur.execute(query)
        dbConnect.close()

        # Membuat objek PrettyTable
        table = from_db_cursor(dbConnect.cur)

        # Menampilkan PrettyTable
        print("\nData Semua Distributor:")
        print(table)

    def cariDistributor(self, id_distributor):
        query = "SELECT * FROM db_peternakan.distributor WHERE id_distributor=%s"
        values = (id_distributor,)
        dbConnect.cur.execute(query, values)
        pt = from_db_cursor(dbConnect.cur)
        if dbConnect.cur.rowcount < 0 or dbConnect.cur.rowcount == 0:
            print(f"{'DATA TIDAK ADA':-^50}")
        else:
            print(f"{'DATA DITEMUKAN':-^50}")
            print(pt)

class StockBarang() :
    def __init__(self, jenis_produk, jumlah_stok, harga_per_kg) :
        self.jenis_produk = jenis_produk
        self.jumlah_stok = jumlah_stok
        self.harga = harga_per_kg

    def insertProduk(self) :
        self.jenis_produk = str(input("Masukkan Jenis Produk : "))
        self.jumlah_stok  = int(input("Masukkan Jumlah Stok  : "))
        self.harga        = int(input("Masukkan Harga/Kg     : "))
        data = {
            "jenis_produk": self.jenis_produk,
            "jumlah_stok": self.jumlah_stok,
            "harga_per_kg": self.harga
        }
        dbConnect.insert('db_peternakan.stok_barang', data)

    def editProduk(self, id_produk):
        # Mendapatkan data produk yang akan diubah
        dbConnect.connect()
        query = "SELECT * FROM db_peternakan.stok_barang WHERE id_produk=%s"
        values = (id_produk,)
        dbConnect.cur.execute(query, values)
        produk_data = dbConnect.cur.fetchone()
        dbConnect.close()
        if produk_data is not None:
            # Menampilkan data produk sebelum diubah
            print("Data Produk Sebelum diubah:")
            print("ID           :", produk_data[0])
            print("Jenis Produk :", produk_data[1])
            print("Jumlah Stok  :", produk_data[2])
            print("Harga/Kg     :", produk_data[3])

            self.jenis_produk = self.jenis_produk or produk_data[1]
            self.jumlah_stok = int(input("Masukkan Jumlah Stok Baru : ") or produk_data[2])
            self.harga       = int(input("Masukkan Harga/Kg Baru    : ") or produk_data[3])
            data = {
                "jenis_produk": self.jenis_produk,
                "jumlah_stok": self.jumlah_stok,
                "harga_per_kg": self.harga
            }
            condition = f"id_produk = {id_produk}"
            dbConnect.update('db_peternakan.stok_barang', data, condition)
            
            dbConnect.connect()
            query = "SELECT * FROM db_peternakan.stok_barang WHERE id_produk=%s"
            values = (id_produk,)
            dbConnect.cur.execute(query, values)
            produk_data = dbConnect.cur.fetchone()
            dbConnect.close()

            # Menampilkan data produk setelah diubah
            print("\nData Produk Setelah diubah:")
            print("ID           :", produk_data[0])
            print("Jenis Produk :", produk_data[1])
            print("Jumlah Stok  :", produk_data[2])
            print("Harga/Kg     :", produk_data[3])
            print('Data Produk Berhasil Di Update!')
        else:
            print("ID tidak terdaftar!")

    def updateStokBarang(self, pilih_id, stok_baru):
        query = "UPDATE db_peternakan.stok_barang SET jumlah_stok = %s WHERE id_produk = %s"
        stok_saat_ini = self.getStokBarang(pilih_id)

        if stok_saat_ini is not None:
            stok_saat_ini = stok_saat_ini[0]  # Ambil nilai stok dari hasil query

            stok = stok_saat_ini - stok_baru  # Hitung stok baru
            data = (stok, pilih_id)
            dbConnect.cur.execute(query, data)
            dbConnect.db.commit()
        else:
            print(f"Produk dengan ID {pilih_id} tidak ditemukan.")

    def getStokBarang(self, pilih_id):
        query = "SELECT jumlah_stok FROM db_peternakan.stok_barang WHERE id_produk = %s"
        values = (pilih_id,)
        dbConnect.cur.execute(query, values)
        stok = dbConnect.cur.fetchone()
        return stok


    def hapusProduk(self, id_produk):
        dbConnect.connect()
        query = "SELECT * FROM db_peternakan.stok_barang WHERE id_produk=%s"
        values = (id_produk,)
        dbConnect.cur.execute(query, values)
        produk_data = dbConnect.cur.fetchone()
        dbConnect.close()
        if produk_data is not None:
            # Menampilkan data produk sebelum dihapus
            print("Data Produk Sebelum dihapus:")
            print("ID           :", produk_data[0])
            print("Jenis Produk :", produk_data[1])
            print("Jumlah Stok  :", produk_data[2])
            print("Harga/Kg     :", produk_data[3])

            # Menghapus data produk
            condition = f"id_produk = {id_produk}"
            dbConnect.delete('db_peternakan.stok_barang', condition)
            print('Data Produk Berhasil Dihapus!')
        else:
            print("ID tidak terdaftar!")

    def tampilkanDataProduk(self):
        # Menampilkan semua data produk
        dbConnect.connect()
        query = "SELECT * FROM db_peternakan.stok_barang"
        dbConnect.cur.execute(query)
        dbConnect.close()
        # Membuat objek PrettyTable
        table = from_db_cursor(dbConnect.cur)

        # Menampilkan PrettyTable
        print("\nData Semua Produk:")
        print(table)

    def cariProduk(self, id_produk):
        dbConnect.connect()
        query = "SELECT * FROM db_peternakan.stok_barang WHERE id_produk=%s"
        values = (id_produk,)
        dbConnect.cur.execute(query, values)
        pt = from_db_cursor(dbConnect.cur)
        dbConnect.close()
        if dbConnect.cur.rowcount < 0 or dbConnect.cur.rowcount == 0:
            print(f"{'DATA TIDAK ADA':-^50}")
        else:
            print(f"{'DATA DITEMUKAN':-^50}")
            print(pt)
    
class Pesanan(StockBarang):
    def __init__(self, jenis_produk, jumlah_stok, harga_per_kg, jumlah_pesanan, harga_total):
        super().__init__(jenis_produk, jumlah_stok, harga_per_kg)
        self.jumlah_pesanan = jumlah_pesanan
        self.harga_total = harga_total 

    def buatPesanan(self):
        StockBarang.tampilkanDataProduk(self)
        dbConnect.connect()
        query = 'SELECT * FROM db_peternakan.stok_barang WHERE id_produk=%s'
        pilih_id = (int(input('ID Barang : ')),)
        dbConnect.cur.execute(query, pilih_id) 
        dataPesanan = dbConnect.cur.fetchone()
        dbConnect.close()
        if dataPesanan :
            self.jenis_produk   = dataPesanan[1]
            self.jumlah_pesanan = int(input("Masukkan Jumlah Pesanan : "))
            if self.jumlah_pesanan > dataPesanan[2] :
                print('Jumlah Pesanan Melebihi Stok Barang')
            else :
                dsb = Distributor('','','','')
                dsb.tampilkanDataDistributor()
                self.distributor_id = int(input("Masukkan ID Distributor : "))
                self.harga_total = self.jumlah_pesanan * dataPesanan[3]
                data = {
                    "jenis_produk": self.jenis_produk,
                    "jumlah_pesanan": self.jumlah_pesanan,
                    "harga_total": self.harga_total,
                    "id_distributor": self.distributor_id
                }
                dbConnect.insert('db_peternakan.pesanan', data) 
                print('Data Pesanan Berhasil Ditambahkan!')
                StockBarang.updateStokBarang(self, pilih_id[0], self.jumlah_pesanan)        

    def editPesanan(self, id_pesanan):
        # Mendapatkan data pesanan yang akan diubah
        dbConnect.connect()
        query = "SELECT * FROM db_peternakan.pesanan WHERE id_pesanan=%s"
        values = (id_pesanan,)
        dbConnect.cur.execute(query, values)
        pesanan_data = dbConnect.cur.fetchone()
        dbConnect.close()
        if pesanan_data is not None:
            # Menampilkan data pesanan sebelum diubah
            print("Data Pesanan Sebelum diubah:")
            print("ID             :", pesanan_data[0])
            print("Jenis Produk   :", pesanan_data[1])
            print("Jumlah Pesanan :", pesanan_data[2])
            print("Harga Total    :", pesanan_data[3])

            self.jenis_produk = self.jenis_produk or pesanan_data[1]
            self.jumlah_pesanan = int(input("Masukkan Jumlah Stok Baru : ") or pesanan_data[2])
            self.harga_total       = self.harga_total or pesanan_data[3]
            data = {
                "jenis_produk": self.jenis_produk,
                "jumlah_pesanan": self.jumlah_pesanan,
                "harga_total": self.harga_total
            }
            condition = f"id_pesanan = {id_pesanan}"
            dbConnect.update('db_peternakan.pesanan', data, condition)
            dbConnect.connect()
            query = "SELECT * FROM db_peternakan.pesanan WHERE id_pesanan=%s"
            values = (id_pesanan,)
            dbConnect.cur.execute(query, values)
            pesanan_data = dbConnect.cur.fetchone()
            dbConnect.close()
            
            # Menampilkan data pesanan setelah diubah
            print("\nData Pesanan Setelah diubah:")
            print("ID             :", pesanan_data[0])
            print("Jenis Produk   :", pesanan_data[1])
            print("Jumlah Pesanan :", pesanan_data[2])
            print("Harga Total    :", pesanan_data[3])
            print('Data Pesanan Berhasil Di Update!')
        else:
            print("ID tidak terdaftar!")

    def tampilkanDataPesanan(self):
        # Menampilkan semua data pesanan
        dbConnect.connect()
        query = "SELECT * FROM db_peternakan.pesanan"
        dbConnect.cur.execute(query)
        dbConnect.close()
        # Membuat objek PrettyTable
        table = from_db_cursor(dbConnect.cur)

        # Menampilkan PrettyTable
        print("\nData Semua Pesanan:")
        print(table)

    def cariPesanan(self, id_produk):
        dbConnect.connect()
        query = "SELECT * FROM db_peternakan.pesanan WHERE id_pesanan=%s"
        values = (id_produk,)
        dbConnect.cur.execute(query, values)
        pt = from_db_cursor(dbConnect.cur)
        dbConnect.close()
        if dbConnect.cur.rowcount < 0 or dbConnect.cur.rowcount == 0:
            print(f"{'DATA TIDAK ADA':-^50}")
        else:
            print(f"{'DATA DITEMUKAN':-^50}")
            print(pt)


        