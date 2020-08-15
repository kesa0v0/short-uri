import sqlite3
from os.path import isfile

class link:
    def __init__(self):
        self.uri = ""
        self.short_uri = ""


class DB:
    def __init__(self):
        self.is_already_exist = isfile("./uriDB.db")
        self.db = sqlite3.connect("./uriDB.db")
        self.cursor = self.db.cursor()

        print(self.is_already_exist)
        if not self.is_already_exist:
            self.cursor.execute('create table db(num int, URI text, SHORTURI text)')

        self.size = self.size = len(self.cursor.fetchall())
        print(self.size)

    def insert(self):
        self.cursor.execute(f'insert into db values({self.size+1}, ".", ".")')
        self.db.commit()
        return self.size+1

    def update(self, num, uri, shorturi):
        self.cursor.execute(f'update db set URI=? where num=?', (uri, num))
        self.cursor.execute(f'update db set SHORTURI=? where num=?', (shorturi, num))
        self.db.commit()

    def select(self, short_uri):
        pass

    def close(self):
        self.db.close()
