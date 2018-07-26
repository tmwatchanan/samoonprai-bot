#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Flask server
from flask import Flask, request, jsonify
# Rasa NLU
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.agent import Agent
from keras import backend as K
# Messenger Platform
from messenger_send_api import verify_webhook, respond, send_image
# from pymessenger.bot import Bot
# Utilities
import random
import os
import json

# Flask
app = Flask(__name__)

# Messenger Bot
# bot = Bot(os.environ['PAGE_ACCESS_TOKEN'])

# NLU

# Load herb data
herb_json_array = None
with open(os.path.join('herb_data', 'herb_data_labeled.json'), encoding="utf-8") as f:
    herb_json_array = json.load(f)


@app.route('/')
def index():
    return '<h1>Samoonprai<h1/>'


def get_random_message():
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
                    print(recipient_id)
                    image_url = "https://dwa5x7aod66zk.cloudfront.net/assets/pack/logo-digitalocean-3d328c1d6619d314d47aab1259c1235b1339c343e12df62a688076bf6ceac866.jpg"
                    # bot.send_image_url(recipient_id, image_url)
                    text = message['message'].get('text')
                    if text:
                        # Get Next action from input user message
                        print(text)
                        rasa_nlu_interpreter_path = os.path.join(os.getcwd(), "models", "nlu", "default", "current")
                        interpreter = RasaNLUInterpreter(rasa_nlu_interpreter_path)
                        rasa_nlu_dialogue_path = os.path.join(os.getcwd(), "models", "dialogue")
                        agent = Agent.load(rasa_nlu_dialogue_path, interpreter=interpreter)
                        next_action = agent.start_message_handling(text, sender_id=recipient_id)
                        # next_action = get_action(text, recipient_id)
                        # next_action = run()
                        print(next_action)
                        herb_name = ''
                        image_path = ''
                        while (next_action['next_action'] != "action_listen"):
                            if next_action['next_action'] == 'bot.action.name_to_photo':
                                print("bot.action.name_to_photo")
                                herb_name = next_action['tracker']['slots']['herb']
                                print(herb_name)
                                matched_herb_list = [x for x in herb_json_array if herb_name in set(x['thaiNameList'])]
                                if len(matched_herb_list) == 0:
                                    break
                                matched_herb = matched_herb_list[0]
                                # print(matched_herb)
                                image_directory_path = os.path.join('herb_data', 'herb_images_png', str(matched_herb['herbId']))
                                herb_file_list = os.listdir(image_directory_path)
                                randomed_file_number = random.randint(1, len(
                                    [name for name in os.listdir(image_directory_path) if
                                     os.path.isfile(os.path.join(image_directory_path, name))]) + 1)
                                selected_herb_file = herb_file_list[randomed_file_number]
                                image_path = os.path.join(image_directory_path, selected_herb_file)
                                image_path = os.path.abspath(image_path)
                            elif next_action['next_action'] == 'bot.utter.herb_photo':
                                print("bot.utter.herb_photo")
                                send_result = send_image(recipient_id, image_path)
                                print(send_result)
                            elif next_action['next_action'] == 'bot.validation.herb_photo':
                                print("bot.validation.herb_photo")
                                respond(recipient_id, "รูปนี้ใช่" + herb_name + "มั้ยครับ")
                            next_action = agent.continue_message_handling(
                                executed_action=next_action['next_action'],
                                sender_id=next_action['tracker']['sender_id'],
                                events=[])
                            print(next_action)
                        # respond(recipient_id, "อยากถามอะไรอีกมั้ยฮะ")
                    # if user sends us a GIF, photo,video, or any other non-text item
                    if message['message'].get('attachments'):
                        response_sent_nontext = get_random_message()
                        respond(recipient_id, response_sent_nontext)
        return "ok"


@app.route('/bot')
def bot():
    message = request.args.get('message')
    return message
    # return jsonify(interpreter.parse(message))


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
