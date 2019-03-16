import sqlite3


class Songs:
    def __init__(self, db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS Songs (id NULL PRIMARY KEY, song TEXT, track_lenght INTEGER, art\
        ist TEXT, album TEXT, play-Count INTEGER, genre TEXT, rating BLOB, loved BLOB)''')
        self.conn.commit()

    def insert(self,id,song,artist,album,play_count,genre): #insert into each table
        self.cur.execute('INSERT into Songs VALUES (NULL,?,?,?,?,?)'\
                             , (song, artist, album, play_count, genre))
        self.conn.commit()
        
    def view(self):        # view all songs
        self.cur.execute("SELECT * FROM Songs")
        rows=self.cur.fetchall()
        return rows
    
    def delete(self,id):        # delete tables
        self.cur.execute('''DELETE * FROM Songs where id=?'''(id,))
        self.conn.commit()

    def update(self, id, song, artist, album, genre, mood, year):
        self.cur.execute('''UPDATE Artists SET Song=?,Artist=?,Album=?,Genre=?,Mood=?,Year=?''',\
                         (song, artist, album, genre, mood, year))
        self.conn.commit()

        # For the loved button that creates the favorites playlist
    def loved(loved):
        while loved != TRUE:
            return null
            loved = True
            print (u"\u2661")
        loved.cur.execute('''UPDATE Songs SET loved=?''', (id, loved))
        self.conn.commit()
        loved.cur.execute("SELECT * FROM Songs")
        rows = self.cur.fetchall()
        return rows

    def __del__(self):
        self.conn.close()


class Artists:
    def __init__(self, db):
        self.conn=sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS Artists (id NULL PRIMARY KEY, artist TEXT, song TEXT, album TEXT,\
        year TEXT, genre TEXT, loved BLOB)''')
        self.conn.commit()

    def insert(self, artist, song, album, year, genre, loved):  # insert into each table
        self.cur.execute('INSERT into artist VALUES (NULL,?,?,?,?,?)'(artist, song, album, year, genre,\
                                                                      loved))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM Artists")
        rows = self.cur.fetchall()
        return rows

    def delete(self, id):
        self.cur.execute('''DELETE * FROM Artists where id=?'''(id, ))
        self.conn.commit()

    def update(self, id, artist, song, album, year, play_count, genre, loved):
        self.cur.execute('''UPDATE Artists SET Artist=?,Song=?,Album=?,Year=?,Genre=?,Loved=? WHERE id=?''',\
                     (artist, song, album, year, genre, loved))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

 class Albums:
     def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS Albums (Album TEXT, art\
        ist TEXT, song TEXT, play-Count INTEGER, genre TEXT, rating BLOB, loved BLOB)''')
        self.conn.commit()

     def insert(self, album, artist, song, genre, year, loved):  # insert into each table
        self.cur.execute('INSERT into artist VALUES (NULL,?,?,?,?,?)'(album, artist, song, genre, year, loved))
        self.conn.commit()

     def view(self):
        self.cur.execute("SELECT * FROM Albums")
        rows = self.cur.fetchall()
        return rows

     def delete(self, id):
        self.cur.execute('''DELETE * FROM Albums where id=?'''(id, ))
        self.conn.commit()

     def update(self, id, album, artist, song, genre, year, loved):
        self.cur.execute('''UPDATE Artists SET Album=?,Artist=?,Song=?,Genre=?,Year=?,Loved=? WHERE id=?''', \
                                 (album, artist, song, genre, year, loved))
        self.conn.commit()

     def __del__(self):
        self.conn.close()


                         ### creates never before played playlist

class NeverBeforePlayed:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute\
            ('''CREATE TABLE IF NOT EXISTS Never Before Played (id INT PRIMARY KEY, song TEXT, track_length INTEGER\
            ,Artist TEXT, Album TEXT, Genre TEXT''')
        self.conn.commit()
        self.conn.close()
