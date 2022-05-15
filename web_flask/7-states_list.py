#!/usr/bin/python3
"""Module for web application of AirBnB Clone"""
import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], '..'))

from flask import Flask, render_template
from models import storage

app = Flask(__name__)

@app.route('/states_list', strict_slashes=False)
def states_list():
    slist = storage.all('State').values()
    return render_template('7-states_list.html', states=slist)

if __name__ == '__main__':
    app.run()
