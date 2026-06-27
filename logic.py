import sqlite3
from config import DATABASE

tabel = [ (_,) for _ in (['user', 'lowongan', 'informasi'])]

class DB_Manager:
    def __init__(self, database):
        self.database = database

    def create_tables(self):
        conn = sqlite3.connect(self.database)

        with conn:
            conn.execute('''CREATE TABLE users (
                            username,
                            nama,
                            pendidikan,
                            jurusan
                        )''')

            conn.execute('''CREATE TABLE lowongan (
                            id_loker,
                            posisi,
                            perusahaan,
                            lokasi,
                            kategori,
                            jurusan
                        )''')

            conn.execute('''CREATE TABLE information (
                            id_info,
                            jenis,
                            judul,
                            deskripsi
                        )''')
            
            conn.commit()

        print("Database berhasil dibuat!")

if __name__ == '__main__':
    manager = DB_Manager(DATABASE)
    manager.create_tables()