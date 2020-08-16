import sqlite3
from os.path import isfile


class DB:
    def __init__(self):
        is_already_exist = isfile("./uriDB.db")
        db = sqlite3.connect("./uriDB.db")
        cursor = db.cursor()

        print("is db already exist?", is_already_exist)
        if not is_already_exist:
            cursor.execute('create table db(num int, URI text, SHORTURI text)')

        self.size = len(cursor.execute('select * from db').fetchall())
        print(self.size)

        db.close()

    def insert(self):
        self.size += 1
        db = sqlite3.connect("./uriDB.db")
        cursor = db.cursor()

        cursor.execute(f'insert into db values({self.size}, ".", ".")')

        db.commit()
        db.close()
        return self.size

    def update(self, num, uri, shorturi):
        db = sqlite3.connect("./uriDB.db")
        cursor = db.cursor()

        cursor.execute(f'update db set URI=? where num=?', (uri, num))
        cursor.execute(f'update db set SHORTURI=? where num=?', (shorturi, num))

        db.commit()
        db.close()

    def select(self, shorturi):
        db = sqlite3.connect("./uriDB.db")
        cursor = db.cursor()

        result = cursor.execute('select * from db where SHORTURI=?', (shorturi,)).fetchall()

        db.close()
        return result
