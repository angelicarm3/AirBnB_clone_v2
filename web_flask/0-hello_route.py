#!/usr/bin/python3
"""Script that starts a Flask web application listening 0.0.0.0 port 5000:"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def domain():
    """The route of the domain / displays 'Hello HBNB!'"""
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
