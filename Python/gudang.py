import sqlite3


class Gudang:
    def __init__(self, db):
        self.db = db


    

    def tambah_barang(self, nama, stock, harga):
        try:
            sql = '''
            INSERT INTO barang(nama, stock, harga)
            VALUES(?,?,?)'''

            self.db.execute(sql, (nama, stock, harga))
            return True
        except sqlite3.IntegrityError:
            return False




    def hapus_barang(self, nama):
        sql = 'DELETE FROM barang WHERE nama = ?'
        affected = self.db.execute(sql, (nama,)) 
        return affected > 0
    
        
    

    def pilih_barang(self, nama):
        sql = 'SELECT nama FROM barang WHERE nama = ?'
        data = self.db.fetchone(sql, (nama,))    

        if data :
            return True
        else:
            return False
            


    def tambah_stock(self, nama, nilai):
        sql = 'UPDATE barang SET stock = stock + ? WHERE nama = ?'
        affected = self.db.execute(sql, (nilai, nama))
        return affected > 0


    
    def kurang_stock(self, nama, nilai):
        sql = 'UPDATE barang SET stock = stock - ? WHERE nama = ? AND stock >= ?'
        affected = self.db.execute(sql, (nilai, nama, nilai))
        return affected > 0



    
    def update_harga(self, nama, nilai):
        sql = 'UPDATE barang SET harga = ? WHERE nama = ?'
        affected = self.db.execute(sql, (nilai, nama))
        return affected > 0



    def tampilkan(self):
       sql = 'SELECT nama, stock, harga FROM barang'
       return self.db.fetchall(sql)    

    


    def update_history(self, kategori, nama, value=None):
        sql = 'INSERT INTO history(kategori, nama, value) VALUES(?,?,?)'
        affected = self.db.execute(sql, (kategori, nama, value))
        return affected > 0
    


    def tampilkan_history(self):
        sql = 'SELECT time, kategori, nama, value FROM history ORDER BY time DESC'
        return self.db.fetchall(sql)
    

    def delete_history(self):
        sql = 'DELETE FROM history'
        affected = self.db.execute(sql)
        return affected






