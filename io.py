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
        
    def view(self):        # view songs
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
        
    def __del__(self):
        self.conn.close()


class Artists:
    def __init__(self, db):
        self.conn=sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS Artists (id NULL PRIMARY KEY, song TEXT, track_length INTEGER, art\
        ist TEXT, album TEXT, play-Count INTEGER, genre TEXT, rating BLOB, loved)''')
        self.conn.commit()


def insert(self, song, artist, album, play_count, genre):  # insert into each table
    self.cur.execute('INSERT into artist VALUES (NULL,?,?,?,?,?)'(song, artist, album, play_count, genre))
    self.conn.commit()


def view(self):
    self.cur.execute("SELECT * FROM Songs")
    rows = self.cur.fetchall()
    return rows


def delete(self, id):
    self.cur.execute('''DELETE * FROM Songs where id=?'''(id, ))
    self.conn.commit()


def update(self, id, song, artist, album, genre, mood, year):
    self.cur.execute('''UPDATE Artists SET Song=?,Artist=?,Album=?,Genre=?,Mood=?,Year=? WHERE id=?''',\
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


class NeverBeforePlayed:                          ### creates never before played playlist
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        elf.cur = self.conn.cursor()
        self.cur.execute\
            ('''CREATE TABLE IF NOT EXISTS Never Before Played (id INT PRIMARY KEY, song TEXT, track_length INTEGER\
            ,Artist TEXT, Album TEXT, Genre TEXT''')
        self.conn.commit()
        self.conn.close()
        
        
