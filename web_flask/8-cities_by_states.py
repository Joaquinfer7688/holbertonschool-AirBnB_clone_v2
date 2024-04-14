#!/usr/bin/python3
"""script that starts flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(exception=None):
    """storage close"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """return cities"""
    states = storage.all(State)
    return render_template("8-cities_by_states.html", states=states)