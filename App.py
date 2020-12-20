# Dependencies imports
from flask import Flask, render_template
from flask_mysqldb import MySQL

# Instance of Flask class
app = Flask(__name__)

# Conection to Data Base
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'jcjohan'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'flaskcontacts'


mysql = MySQL(app)

# Routes of the application
@app.route('/')
def Home():
    return render_template('index.html')

@app.route('/add-contact')
def addContact():
    return 'Add contact'

@app.route('/edit')
def editContact():
    return 'edit contact'

@app.route('/delete')
def deleteContact():
    return 'delete contact'

# Run server
if __name__ == '__main__':
    app.run(port = 4000, debug = True)

