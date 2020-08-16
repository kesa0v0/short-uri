import sqlite3
from os.path import isfile


class DB:
    def __init__(self):
        is_already_exist = isfile("./uriDB.db")
        db = sqlite3.connect("./uriDB.db")
        cursor = db.cursor()

        print("is db already exist?", is_already_exist)
        if not is_already_exist:
            cursor.execute('CREATE TABLE db(num int, URI text, SHORTURI text)')

        self.size = len(cursor.execute('SELECT * FROM db').fetchall())
        print("current db size:", self.size)

        db.close()

    def insert(self):
        self.size += 1
        db = sqlite3.connect("./uriDB.db")
        cursor = db.cursor()

        cursor.execute('INSERT INTO db VALUES({}, ".", ".")'.format(self.size))

        db.commit()
        db.close()
        return self.size

    def update(self, num, uri, shorturi):
        db = sqlite3.connect("./uriDB.db")
        cursor = db.cursor()

        cursor.execute('UPDATE db SET URI=? WHERE num=?', (uri, num))
        cursor.execute('UPDATE db SET SHORTURI=? WHERE num=?', (shorturi, num))

        db.commit()
        db.close()

    def select(self, shorturi):
        db = sqlite3.connect("./uriDB.db")
        cursor = db.cursor()

        result = cursor.execute('SELECT * FROM db WHERE SHORTURI=?', (shorturi,)).fetchall()

        db.close()
        return result
