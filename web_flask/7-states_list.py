#!/usr/bin/python3
"""Module for web application of AirBnB Clone"""
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def tear_down(exception):
    """Closing session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Shows a list of all the states"""
    slist = storage.all('State').values()
    return render_template('7-states_list.html', states=slist)


if __name__ == '__main__':
    app.run()
