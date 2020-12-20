# Dependencies imports
from flask import Flask

# Instance of Flask class
app = Flask(__name__)

# Run server
if __name__ == '__main__':
    app.run(port = 4000, debug = True)

