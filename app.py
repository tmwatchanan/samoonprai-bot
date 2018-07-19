#!/usr/bin/env python
from flask import Flask, request, jsonify
from rasa_core.interpreter import RasaNLUInterpreter

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello World<h1/>'


@app.route('/bot')
def bot():
    message = request.args.get('message')
    interpreter = RasaNLUInterpreter("rasa/models/nlu/default/current")
    return jsonify(interpreter.parse(message))

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
