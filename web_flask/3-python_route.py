#!/usr/bin/python3
"""Python flask web application"""
from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return('Hello HBNB!')


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return('HBNB')


@app.route('/c/<string:text>', strict_slashes=False)
def c_is(text):
    return('c is {}'.format(text.replace('_', ' ')))


@app.route('/python', strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def python_is(text='is cool'):
    return('Python {}'.format(text.replace('_', ' ')))


if __name__ == '__main__':
    app.run()
