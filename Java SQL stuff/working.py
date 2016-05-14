# import the Flask class from the flask module
from flask import Flask, render_template
from flask import Flask, render_template, redirect, url_for, request
import sqlite3

# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/')
def home():
    return "Hello, World! How are you?"  # return a string

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template

# initialize database

# route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        conn = sqlite3.connect('example.db')
        c = conn.cursor()
        use = request.form['username']
        use = str(use)
        use = (use, )
        c.execute('SELECT * FROM stocks WHERE username=?', use)
        line = c.fetchone()
        try:
           username = line[0]
           password = line[1]
           if request.form['username'] != username or request.form['password'] != password:
              error = 'Invalid Credentials. Please try again.'
           else:
              return redirect(url_for('home'))
        except:
           error = 'Invalid Credentails. Please try again.'
    return render_template('login.html', error=error)

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
