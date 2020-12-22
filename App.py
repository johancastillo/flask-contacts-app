# Dependencies imports
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

# Instance of Flask class
app = Flask(__name__)

# Conection to Data Base MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'jcjohan'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'flaskcontacts'

mysql = MySQL(app)

# Settings for sessions
app.secret_key = 'mysecretkey'

# Route root
@app.route('/')
def Home():
    return render_template('index.html')

# Receive data with the method POST from the route root
@app.route('/add-contact', methods=['POST'])
def AddContact():
    if request.method == 'POST':
        fullname = request.form['fullname'] 
        phone = request.form['phone'] 
        email = request.form['email'] 
        
        # Get connection
        cursor = mysql.connection.cursor()

        # Write sentence
        cursor.execute('INSERT INTO contacts (fullname, phone, email) VALUES (%s, %s, %s)', 
        (fullname, phone, email))

        # Execute 
        mysql.connection.commit()
        
        flash('Contact Added Successfully')
        return redirect(url_for('Home'))

@app.route('/edit')
def editContact():
    return 'edit contact'

@app.route('/delete')
def deleteContact():
    return 'delete contact'

# Run server
if __name__ == '__main__':
    app.run(port = 4000, debug = True)

