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


if __name__ == '__main__':
    app.run()
