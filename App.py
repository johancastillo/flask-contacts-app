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
    # Consulte to the data base
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM contacts')
    data = cursor.fetchall()

    # View
    return render_template('index.html', contacts = data)

# Receive data with the method POST from the route root
@app.route('/add-contact', methods = ['POST'])
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

# Edit data
@app.route('/edit/<id>')
def GetContact(id):
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM contacts WHERE id = %s', (id))
    data = cursor.fetchall()
    
    return render_template('edit-contact.html', contact = data[0])

@app.route('/update/<id>', methods = ['POST'])
def UpdateContact(id):
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']

        cursor = mysql.connection.cursor()
        cursor.execute(""" 
            UPDATE contacts
            SET fullname = %s,
                phone = %s,
                email = %s
            WHERE id = %s
        """, (fullname, phone, email, id))

        mysql.connection.commit()

        flash('Contact Updated Successfully')

        return redirect(url_for('Home'))

# Delete data
@app.route('/delete/<string:id>')
def deleteContact(id):
    cursor = mysql.connection.cursor()
    cursor.execute('DELETE FROM contacts WHERE id = {0}'.format(id))
    mysql.connection.commit()

    # Message
    flash('Contact Removed Successfully')

    return redirect(url_for('Home'))

# Run server
if __name__ == '__main__':
    app.run(port = 4000, debug = True)

