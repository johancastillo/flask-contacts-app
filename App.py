# Dependencies imports
from flask import Flask

# Instance of Flask class
app = Flask(__name__)

# Routes of the application
@app.route('/')
def Home():
    return '<h1 style="text-align:center">Hello World</h1>'

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

