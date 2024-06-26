#!/usr/bin/python3
"""
script that starts flask web application
"""
from flask import Flask, render_template


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


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """
    return display a HTML page only if n is an integer
    """
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """
     display a HTML page only if n is an integer
    """
    if n % 2 == 0:
        status = "even"
    else:
        status = "odd"
    return render_template('6-number_odd_or_even.html', n=n, status=status)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
