import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute('''CREATE TABLE stocks 
               (username text, password text)''')
c.execute("INSERT INTO stocks VALUES ('alex', 'password')")
conn.commit()
conn.close()
