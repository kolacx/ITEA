import sqlite3

class Connection_db():

    def __enter__(self):
        self._conn = sqlite3.connect('shop')
        cursore = self._conn.cursor()
        return cursore

    def __exit__(self, *args):
        self._conn.commit()
        self._conn.close()

with Connection_db() as db:
    print(db)