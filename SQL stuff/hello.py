from flask import Flask
import sqlite3
from flask import g

Database = 'database.db'

def get_db():
   db = getattr(g, '_database', None)
   if db if None:
      db = g._database = connect_to_database()
   return db

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.debug = True
    app.run()
