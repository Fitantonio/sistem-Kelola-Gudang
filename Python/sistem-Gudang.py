from gudang import Gudang
from database import Database


def main():
    db = Database()
    g = Gudang(db)
    pilih = ""
    

    while True:
        print("Menu Halaman Utama")
        print("1. Cek Jenis Barang")
        print("2. Pilih Barang")
        print("3. Tambah jenis Barang")
        print("4. Hapus jenis Barang")
        print("5. Edit Info barang")
        print("6. lihat riwayat gudang")
        print("7. Hapus riwayat gudang")
        print("8. Cari Barang")
        print("9. Keluar")
        print("")
        
        nomor = input("pilih menu : ")
        print("")
        
        if nomor == "9":
            print("Sampai Jumpa")
            print("")
            db.close()
            break
        


        elif nomor == "1":
            data = g.tampilkan()
            if not data :
                print("gudang kosong")
            else:
                result = []
                for nama, stock, harga in data:
                    result.append(f"{nama} | stock: {stock} | harga: {harga}")
                
                for item in result:
                    print(item)
            print("")
        


        elif nomor == "2":
            nama = input("masukan nama barang yang ingin di pilih : ").lower()
            if g.pilih_barang(nama):
                print("barang berhasil di pilih")
                pilih = nama
            else:
                print("barang tidak di temukan")
            print("")
        


        elif nomor == "3":
            jenis = input("masukan nama Barang : ").lower()
            p = g.validate_string(jenis)
            if p == True:
                try:
                    stockAwal = int(input("masukan Stock Awal : "))
                    harga = int(input("masukan Harga barang : "))

                    if (g.validate_number(stockAwal) != True ):
                        print(g.validate_number(stockAwal))
                    elif(g.validate_number(harga) != True ):
                        print(g.validate_number(harga))
                    else:
                        if g.tambah_barang(jenis, stockAwal, harga):
                            print("barang berhasil ditambahkan")
                            g.update_history("tambah-barang(values = stock awal)", jenis, stockAwal)
                        else:
                            print("barang sudah ada")
                except ValueError:
                    print("masukan harus berupa Angka")
            else:
                print(p)
            print("")
            
        

        
        elif nomor == "4":
            hapus = input("masukan nama barang yang ingin di hapus : ").lower()
            if hapus == pilih:
                pilih = ""
            if g.hapus_barang(hapus):
                print("barang berhasil di hapus")
                g.update_history("hapus-barang", hapus)
            else:
                print("Barang tidak di temukan")
            print("")


        

        elif nomor == "5":
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
                        if g.validate_number(tambah) != True:
                            print(g.validate_number(tambah))
                        else:
                            if g.tambah_stock(pilih, tambah):
                                print("barang berhasil di tambahkan")
                                g.update_history("tambah-stock-barang(values = nominal tambahan)", pilih, tambah)
                            else:
                                print("barang tidak ditemukan")
                        
                    except ValueError:
                        print("masukan harus berupa Angka")

                elif num == "2":
                    try:
                        kurang = int(input("masukan nominal pengurangan stock : "))
                        if g.validate_number(kurang) != True:
                            print(g.validate_number(kurang))
                        else:
                            if g.kurang_stock(pilih, kurang):
                                print("barang berhasil di Kurangi")
                                g.update_history("kurang-stock-barang(values = nomial pengurangan)", pilih, kurang)
                            else:  
                                print("nomimal melebihi banyak stock")

                    except ValueError:
                        print("masukan harus berupa Angka")

                
                    
                elif num == "3":
                    try:
                        ubah = int(input("masukan harga baru : "))
                        if g.validate_number(ubah) != True:
                            print(g.validate_number(ubah))
                        else:
                            if g.update_harga(pilih, ubah):
                                print("harga berhasil di rubah")
                                g.update_history("ubah-harga(values = harga baru)", pilih, ubah)
                            else:
                                print("barang tidak ditemukan")
                    except ValueError:
                        print("masukan harus berupa Angka")
                    
                elif num == "4":
                    print("Kembali Ke menu utama , silahkan Pilih jenis Barang")
                    pilih = ""
                    break

                else:
                    print("angka tidak valid")

            print("")
        

        elif nomor == "6":
            data = g.tampilkan_history()
            if not data:
                print("history masih kosong")
            else:
                result = []
                for time, kategori, nama, value in data:
                    result.append(f"{time} | nama:  {nama} | kategori: {kategori} | values: {value}")

                for i in result:
                    print(i)
            
            print("")

        
        elif nomor == "7":
            data = input("apakah anda yakin (y/n) : ").lower()
            if data == "y" or data == "Y":
                if g.delete_history():
                    print("data riwayat berhasil di hapus")
                else:
                    print("error")
            else:
                print("operasi di batalkan, kembali ke menu utama")

            print("")


        elif nomor == "8":
            data = input("masukan nama barang yang ingin di cari : ").lower()
            result = g.cari_barang(data)

            print("")
            if result:
                for nama, stock, harga in result:
                    print(f"{nama} | stock: {stock} | harga: {harga}")
            else:
                print("barang tidak di temukan")
            print("")


        else:
            print("angka tidak valid")  
            print("")
                 
        
main()