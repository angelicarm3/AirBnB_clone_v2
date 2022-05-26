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


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def text_python(text='is cool'):
    """The route of the domain /Python/text displays text"""
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """The route of the domain /Number/n displays text"""
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
