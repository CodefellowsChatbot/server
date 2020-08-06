#!/usr/bin/python
# coding: utf-8
from flask import Flask

app = Flask(__name__)

@app.route('/')
def entry_point():
    return 'Hello World!'


@app.route("/question")
def question_route():
    return "I don't have an answer for that question yet"

if __name__ == '__main__':
    app.run(debug=True)