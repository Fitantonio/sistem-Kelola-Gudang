import sqlite3


class Database:
    def __init__(self): 
        self.conn = sqlite3.connect('gudang.db')
        self.cursor = self.conn.cursor()
        self.create_table_barang()
        self.create_table_history()


    def create_table_barang(self) :
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS barang(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                waktu TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                nama TEXT NOT NULL UNIQUE,
                stock INTEGER CHECK (stock >= 0),
                harga INTEGER        
            )
            ''')
        self.conn.commit()



    def create_table_history(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS history(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                time DATETIME DEFAULT (DATETIME('now', 'localtime')),
                kategori TEXT NOT NULL,
                nama TEXT NOT NULL,
                value INTEGER                         
            )
            ''')
        self.conn.commit()




    def execute(self, sql, param=()):
        self.cursor.execute(sql, param)
        self.conn.commit()
        return self.cursor.rowcount
        


    def fetchone(self, sql, param=()):
        self.cursor.execute(sql, param)
        return self.cursor.fetchone()
    


    def fetchall(self, sql, param=()):
        self.cursor.execute(sql, param)
        return self.cursor.fetchall()


    def close(self):
        self.conn.close()




