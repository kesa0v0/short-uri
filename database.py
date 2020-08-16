import sqlite3
from os.path import isfile


class DB:
    def __init__(self):
        self.is_already_exist = isfile("./uriDB.db")
        self.db = sqlite3.connect("./uriDB.db")
        self.cursor = self.db.cursor()

        print(self.is_already_exist)
        if not self.is_already_exist:
            self.cursor.execute('create table db(num int, URI text, SHORTURI text)')

        self.size = len(self.cursor.execute('select * from db').fetchall())
        print(self.size)

    def insert(self):
        self.size += 1
        self.cursor.execute(f'insert into db values({self.size}, ".", ".")')
        self.db.commit()
        return self.size

    def update(self, num, uri, shorturi):
        self.cursor.execute(f'update db set URI=? where num=?', (uri, num))
        self.cursor.execute(f'update db set SHORTURI=? where num=?', (shorturi, num))
        self.db.commit()

    def select(self, shorturi):
        return self.cursor.execute('select * from db where SHORTURI=?', (shorturi,)).fetchall()

    def close(self):
        self.db.close()
