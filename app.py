#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify
from rasa_core.interpreter import RasaNLUInterpreter
from messenger_send_api import verify_webhook, respond
import random

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World<h1/>'


def get_message():
    sample_responses = ["อู้หยังนิ", "บ่ฮู้เรื่อง", "อู้ไปเรื่อย", "สวัสดีเจ้า", "ต่อนยอน"]
    # return selected item to the user
    return random.choice(sample_responses)


@app.route("/webhook", methods=['GET', 'POST'])
def listen():
    """This is the main function flask uses to
    listen at the `/webhook` endpoint"""
    if request.method == 'GET':
        return verify_webhook(request)

    if request.method == 'POST':
        payload = request.get_json()
        output = request.get_json()
        for event in output['entry']:
            messaging = event['messaging']
            for message in messaging:
                if message.get('message'):
                    # Facebook Messenger ID for user so we know where to send response back to
                    recipient_id = message['sender']['id']
                    text = message['message'].get('text')
                    if text:
                        response_sent_text = get_message()
                        # send_message(recipient_id, response_sent_text)
                        respond(recipient_id, response_sent_text)
                    # if user sends us a GIF, photo,video, or any other non-text item
                    if message['message'].get('attachments'):
                        response_sent_nontext = get_message()
                        # send_message(recipient_id, response_sent_nontext)
                        respond(recipient_id, response_sent_nontext)


        return "ok"

@app.route('/bot')
def bot():
    message = request.args.get('message')
    interpreter = RasaNLUInterpreter("rasa/models/nlu/default/current")
    return jsonify(interpreter.parse(message))


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
