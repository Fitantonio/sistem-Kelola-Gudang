import json
from datetime import datetime

class Barang:
    def __init__(self, nama, stock, harga):
        self.nama = nama
        self.stock = stock
        self.harga = harga
    


    def to_dict(self):
        return {
            "nama" : self.nama, 
            "stock" : self.stock,
            "harga" : self.harga
        }
    

    @staticmethod
    def from_dict(data):
        return Barang(data["nama"], data["stock"], data["harga"])
    


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
        self.history_list = []


    def save(self):
        data = {}
        for nama , barang in self.list.items():
            data[nama] = barang.to_dict()
        
        with open("gudang.json", "w") as files:
            json.dump(data, files, indent=4)

    
    def load(self):
        data = {}
        
        try:
            with open("gudang.json", "r") as files:
                data = json.load(files)
        
            for nama, barang in data.items():
                self.list[nama] = Barang.from_dict(barang)
        except(FileNotFoundError, json.JSONDecodeError):
            self.list = {}
    

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
            result +=  f"{i + 1}. {item}, stok : {self.list[item].stock}, harga : Rp. {self.list[item].harga} \n"
        return result
    


    def history(self, keterangan, date, key, value=None):
        data = None
        if keterangan == "barang-baru":
            data = f"[{date}], {keterangan} : {key}, stock awal : {value}"
        elif keterangan == "tambah-stock":
            data = f"[{date}], {keterangan} : {key}, tambah stock : {value}"
        elif keterangan == "kurang-stock":
            data = f"[{date}], {keterangan} : {key}, kurang stock : {value}"
        elif keterangan == "ubah-harga":
            data = f"[{date}], {keterangan} : {key}, harga baru : {value}"
        elif keterangan == "hapus-barang":
            data = f"[{date}], {keterangan} : {key}"
        else:
            return False
        
        self.history_list.append(data)

        with open("riwayat.json", "w") as files:
            json.dump(self.history_list, files, indent=4)

        return True


    def load_history(self):
        try:
            with open("riwayat.json", "r") as files:
                self.history_list = json.load(files)
        except (FileNotFoundError, json.JSONDecodeError):
            self.history_list = []










def main():
    g = Gudang()
    g.load()
    g.load_history()

    def time():
        temp = datetime.now()
        return(temp.strftime("%Y-%m-%d %H:%M:%S"))

    while True:
        print("Menu Halaman Utama")
        print("1. Cek Jenis Barang")
        print("2. Pilih Barang")
        print("3. Tambah jenis Barang")
        print("4. Hapus jenis Barang")
        print("5. Edit Info barang")
        print("6. lihat riwayat gudang")
        print("7. Keluar")
        print("")
        
        nomor = input("pilih menu : ")
        print("")
        
        if nomor == "7":
            print("Sampai Jumpa")
            print("")
            g.save() 
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
                    
                    g.history("barang-baru", time(), jenis, stockAwal)
                    
                else:
                    print("barang sudah ada")
            except ValueError:
                print("masukan harus berupa Angka")
            print("")
            
            
            g.save()
        

        
        elif nomor == "4":
            hapus = input("masukan nama barang yang ingin di hapus : ")
            if g.hapus_barang(hapus):
                print("barang berhasil di hapus")
                g.history("hapus-barang", time(), hapus)
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
                        g.history("tambah-stock", time(), pilih, tambah)
                        
                    except ValueError:
                        print("masukan harus berupa Angka")

                elif num == "2":
                    try:
                        kurang = int(input("masukan nominal pengurangan stock : "))
                        if g.list[pilih].kurang_stock(kurang):
                            print("barang berhasil di Kurangi")
                            g.history("kurang-stock", time(), pilih, kurang)
                        else:
                            print("nomimal melebihi banyak stock")

                    except ValueError:
                        print("masukan harus berupa Angka")

                
                    
                elif num == "3":
                    try:
                        ubah = int(input("masukan harga baru : "))
                        g.list[pilih].ubah_harga(ubah)
                        print("harga berhasil di rubah")
                        g.history("ubah-harga", time(), pilih, ubah)
                    except ValueError:
                        print("masukan harus berupa Angka")
                    
                elif num == "4":
                    print("Kembali Ke menu utama , silahkan Pilih jenis Barang")
                    break
                else:
                    print("angka tidak valid")

            print("")
        
        elif nomor == "6":
            if not g.history_list:
                print("belum ada riwayat")
            else:
                print("======== Riwayat ========")
                for items in g.history_list:
                    print(items)
                print("=========================")
            print("")

        else:
            print("angka tidak valid")  
        

          
            
        
main()