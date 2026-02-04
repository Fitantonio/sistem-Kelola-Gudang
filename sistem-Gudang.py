class Barang:
    def __init__(self, nama, stock, harga):
        self.nama = nama
        self.stock = stock
        self.harga = harga
    

    def tambah_stock(self, jumlah):
        self.stock += jumlah
        

    
    def kurang_stock(self, jumlah):
        if jumlah > self.stock:
            return False
            
        else:
            self.stock -= jumlah
            return True
            
    

    def ubah_harga(self, Harga):
        self.harga = Harga


    
    def __str__(self):
        return f"{self.nama} - Stock: {self.stock}, Harga: {self.harga}"
        




class Gudang:
    def __init__(self):
        self.list = {}
        self.pilih = ""
    

    def tambah_barang(self, nama, stock, harga):
        if nama not in self.list:
            self.list[nama] = Barang(nama, stock, harga)
            return True
        else:
            return False


    def hapus_barang(self, nama):
        if len(self.list) == 0 or nama not in self.list:
            return False
        else:
            if self.pilih == nama:
                self.pilih = ""
            del self.list[nama]
            return True
    

    def pilih_barang(self, nama):
        if nama not in self.list:
            return False
        else:
            self.pilih = nama
            return True
            
        
    
    def __str__(self):
        result = ""
        if len(self.list) == 0:
            return "Gudang Kosong"
        for i, item in enumerate(self.list):
            result +=  f"{i + 1}. {item}, stok : {self.list[item].stock}, harga : {self.list[item].harga} \n"
        return result







def main():
    g = Gudang()

    while True:
        print("Menu Halaman Utama")
        print("1. Cek Jenis Barang")
        print("2. Pilih Barang")
        print("3. Tambah jenis Barang")
        print("4. Hapus jenis Barang")
        print("5. Edit Info barang")
        print("6. Keluar")
        print("")
        
        nomor = input("pilih menu : ")
        print("")
        
        if nomor == "6":
            print("Sampai Jumpa")
            print("")
            break
        


        elif nomor == "1":
            print(g.__str__())
            print("")
        


        elif nomor == "2":
            nama = input("masukan nama barang yang ingin di pilih : ")
            if g.pilih_barang(nama):
                print("barang berhasil di pilih")
            else:
                print("barang tidak di temukan")
            print("")
        


        elif nomor == "3":
            jenis = input("masukan nama Barang : ")
            try:
                stockAwal = int(input("masukan Stock Awal : "))
                harga = int(input("masukan Harga barang : "))

                if g.tambah_barang(jenis, stockAwal, harga):
                    print("barang berhasil ditambahkan")
                else:
                    print("barang sudah ada")
            except ValueError:
                print("masukan harus berupa Angka")
            print("")
        

        
        elif nomor == "4":
            hapus = input("masukan nama barang yang ingin di hapus : ")
            if g.hapus_barang(hapus):
                print("barang berhasil di hapus")
            else:
                print("Barang tidak di temukan")
            print("")

        

        elif nomor == "5":
            pilih = g.pilih
            if pilih == "":
                print("anda harus memilih barang terlebih dahulu")
                continue
            else:
                print("barang yang di pilih saat ini : " + pilih)
            
            while True:
                print("Menu Operasi :")
                print("1. Tambah Stock")
                print("2. Kurangi Stock")
                print("3. Ubah Harga")
                print("4. Kembali ke Menu Utama")

                num = input("masukan nomor yang ingin di pilih : ")
                print("")

                if num == "1":
                    try:
                        tambah = int(input("masukan tambahan stock : "))
                        g.list[pilih].tambah_stock(tambah)
                        print("barang berhasil di tambahkan")
                    except ValueError:
                        print("masukan harus berupa Angka")

                elif num == "2":
                    try:
                        kurang = int(input("masukan nominal pengurangan stock : "))
                        if g.list[pilih].kurang_stock(kurang):
                            print("barang berhasil di Kurangi")
                        else:
                            print("nomimal melebihi banyak stock")

                    except ValueError:
                        print("masukan harus berupa Angka")

                
                    
                elif num == "3":
                    try:
                        ubah = int(input("masukan harga baru : "))
                        g.list[pilih].ubah_harga(ubah)
                        print("harga berhasil di rubah")
                    except ValueError:
                        print("masukan harus berupa Angka")
                    
                elif num == "4":
                    print("Kembali Ke menu utama , silahkan Pilih jenis Barang")
                    break
                else:
                    print("angka tidak valid")

            print("")
        else:
            print("angka tidak valid")           
            
        
main()