#!/usr/bin/python
# coding: utf-8
from flask import Flask
import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from resources.links import Links

print(Links.javascript[401])


app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))


@app.route("/")
def entry_point():
    return "Hello World!"


@app.route("/question")
def question_route():
    return "I don't have an answer for that question yet"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=port)
