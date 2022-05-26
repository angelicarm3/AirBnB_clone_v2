#!/usr/bin/python3
""" Script that starts a Flask web application listening 0.0.0.0 port 5000:"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def domain():
    """The route of the domain / displays 'Hello HBNB!'"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """The route of the domain /hbhb displays 'HBNB'"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def text_c(text):
    """The route of the domain /C/text displays text"""
    return "C {}".format(text.replace("_", " "))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
