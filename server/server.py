#!/usr/bin/python
# coding: utf-8
from flask import Flask, request, jsonify
from chat_bot.chat import ChatBot
from intents_producer.etl import main as create_intents
from chat_bot.train import main as train_chatbot
import os, sys

create_intents()
train_chatbot()
chatbot = ChatBot()

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from resources.links import Links



app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))


@app.route("/")
def entry_point():
    return "Hello World!"


@app.route("/question",methods=["GET", "POST"])
def question_route():
    try:
        content = request.json
        text = content["text"]
        output = chatbot.respond(text)
        print(f"Incoming request with string: {text}")
        return jsonify({"text": output, "success": True})
    except:
        return jsonify({"text": "Sorry That didn't work", "success": False})


@app.route("/proof_of_life", methods=["GET", "POST"])
def handle_proof_of_life():
    try:
        content = request.json
        text = content["text"]
        print(f"Incoming request with string: {text}")
        return jsonify({"text": text, "success": True})
    except:
        return jsonify({"text": "Sorry That didn't work", "success": False})



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=port)
