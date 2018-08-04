#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Flask server
from flask import Flask, request
# from celery import Celery  # Background tasks
# Messenger Platform
from messenger_send_api import verify_webhook
# Samoonprai Bot
import controllers
# Utilities
import logging

# Logging
logger = logging.getLogger('SAMOONPRAI')
logger.setLevel(logging.INFO)
formatter = logging.Formatter('[%(asctime)s][%(name)s][%(levelname)s] %(message)s')
file_handler = logging.FileHandler('server.log', encoding='utf-8')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Flask
app = Flask(__name__)


# @app.route('/')
# def index():
#     return '<h1>Samoonprai<h1/>'


@app.route("/webhook", methods=['GET', 'POST'])
def listen():
    """This is the main function flask uses to
    listen at the `/webhook` endpoint"""
    if request.method == 'GET':
        return verify_webhook(request)

    if request.method == 'POST':
        return "ok", 200
        # return "no", 403

@app.after_request
def process(response):
    payload = request.get_json()
    # print(payload)
    if payload['object'] == 'page':
        controllers.process_incoming_message(payload)
    return response



# @app.route('/bot')
# def bot():
#     message = request.args.get('message')
#     return message  # Echo message
#     # return jsonify(interpreter.parse(message))


# if __name__ == '__main__':
#     app.run(host='127.0.0.1', port=5000, debug=True)
