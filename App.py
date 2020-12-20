# Dependencies imports
from flask import Flask

# Instance of Flask class
app = Flask(__name__)

# Routes of the application
@app.route('/')
def home():
    return "Hello World"

# Run server
if __name__ == '__main__':
    app.run(port = 4000, debug = True)

