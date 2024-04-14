#!/usr/bin/python3
"""
script that starts flask web application
"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def HBNB():
    """
    return Hello HBNB
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    return hbnb
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def C(text):
    """
    return C followed by the value of the text variable
    """
    return "C " + text.replace("_", " ")


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """
    return Python by the value of the text variable
    """
    return "Python " + text.replace("_", " ")


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """
    return n is a number” only if n is an integer
    """
    return f"{n} is a number"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
