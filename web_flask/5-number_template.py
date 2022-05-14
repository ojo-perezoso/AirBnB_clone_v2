#!/usr/bin/python3
"""Python flask web application"""
from flask import Flask, render_template


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
    return('python is {}'.format(text.replace('_', ' ')))


@app.route('/number/<int:n>', strict_slashes=False)
def number_is(n):
    return('{} is a number'.format(n))


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', value=n)


if __name__ == '__main__':
    app.run()
