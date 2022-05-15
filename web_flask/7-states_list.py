#!/usr/bin/python3
"""Module for web application of AirBnB Clone"""
#import os
#import sys
from flask import Flask, render_template
from models import storage


#sys.path.insert(1, os.path.join(sys.path[0], '..'))
app = Flask(__name__)


@app.teardown_appcontext
def tear_down():
    """Closing session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Shows a list of all the states"""
    slist = storage.all('State').values()
    tear_down()
    return render_template('7-states_list.html', states=slist)


if __name__ == '__main__':
    app.run()
