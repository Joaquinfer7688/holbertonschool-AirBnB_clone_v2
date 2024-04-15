#!/usr/bin/python3
"""Write a script that starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(exception=None):
    """storage close."""
    storage.close()


@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def states(id=None):
    """
    list of states
    """
    states = storage.all("State")
    if state_id is not None:
        state_id = 'State.' + state_id
    return render_template('9-states.html', states=states, state_id=state_id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
