import sqlite3

conn = sqlite3.connect("db.sqlite3")

cur = conn.cursor()
cur.execute("UPDATE articles_lost_species SET species='코리안 숏헤어' where id=62")
conn.commit()
conn.close()
