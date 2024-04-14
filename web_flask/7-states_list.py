#!/usr/bin/python3
"""script that starts flask web application"""


from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    return all the states
    """
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_appcontext(exception=None):
    """storage close"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
