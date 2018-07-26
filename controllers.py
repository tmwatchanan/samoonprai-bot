#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Messenger Platform
import messenger_send_api
# Rasa NLU
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.agent import Agent
# Utilities
import random
import os
import json
import logging

# Disable warning messages
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn
warnings.filterwarnings(action='ignore', category=DeprecationWarning)

# Logging
logger = logging.getLogger('SAMOONPRAI')

# Load herb data
herb_json_array = None
with open(os.path.join('herb_data', 'herb_data_labeled.json'), encoding="utf-8") as f:
    herb_json_array = json.load(f)

# DEFINE CONSTANTS
BOT_NAME = "ลูกสมุนไพร"
HERB_NOT_FOUND, IMAGE_NOT_FOUND, *_ = range(100)


def process_incoming_message(payload):
    for event in payload['entry']:
        messaging = event['messaging']
        for message in messaging:
            if message.get('message'):
                # Facebook Messenger ID for user so we know where to send response back to
                recipient_id = message['sender']['id']
                text = message['message'].get('text')
                user_info = messenger_send_api.get_user_info(recipient_id, ['first_name', 'last_name'])
                user_name = user_info['first_name'] if user_info else ''
                print(user_info)
                if text:
                    # Get Next action from input user message
                    logger.info(recipient_id + " sends " + "\"" + text + "\"")
                    agent, next_action = nlu_start(recipient_id, text)
                    messenger_send_api.debug_respond(recipient_id, next_action['next_action'])
                    herb_name = next_action['tracker']['slots']['herb']
                    herb_object = None
                    if herb_name is None:
                        herb_name = ''
                        herb_object = HERB_NOT_FOUND
                    logger.debug("(" + recipient_id + ")(" + text + "): %s", next_action)
                    while (next_action['next_action'] != 'action_listen'):
                        if next_action['next_action'] == 'bot.utter.greeting':
                            messenger_send_api.respond(recipient_id, "สวัสดีครับ " + user_name + " มีอะไรให้ลูกสมุนไพรช่วยมั้ยฮะ")
                        elif next_action['next_action'] == 'bot.action.name_to_photo':
                            if herb_object == HERB_NOT_FOUND:
                                messenger_send_api.respond(recipient_id, "ขออภัยครับ ตอนนี้ลูกสมุนไพรไม่รู้จักสมุนไพรชื่อ" + herb_name + "ครับ")
                                break
                            else:
                                herb_object = get_herb_info_from_database(herb_name)
                                messenger_send_api.respond(recipient_id, "รอสักครู่คร้าบ ลูกสมุนไพรกำลังหารูปของ" + herb_name + "ให้ครับ")
                        elif next_action['next_action'] == 'bot.utter.herb_photo':
                            image_path = get_image_path_from_herb(herb_object)
                            if image_path == IMAGE_NOT_FOUND:
                                messenger_send_api.respond(recipient_id, "ขออภัยครับ ตอนนี้ลูกสมุนไพรยังไม่มีรูป" + herb_name + "ครับ")
                                break
                            else:
                                messenger_send_api.respond(recipient_id, "นี่ครับ รูป" + herb_name)
                                send_api_response = messenger_send_api.send_image(recipient_id, image_path)
                        elif next_action['next_action'] == 'bot.validation.herb_photo':
                            # messenger_send_api.respond(recipient_id, "รูปนี้ใช่" + herb_name + "มั้ยครับ ช่วยลูกสมุนไพรยืนยันหน่อยน้า")
                            buttons = []
                            button = {
                                'type': 'postback',
                                'title': 'ใช่',
                                'payload': 'corrent'
                            }
                            buttons.append(button)
                            button = {
                                'type': 'postback',
                                'title': 'ไม่ใช่',
                                'payload': 'wrong'
                            }
                            buttons.append(button)
                            text = "รูปนี้ใช่" + herb_name + "มั้ยครับ ช่วยลูกสมุนไพรยืนยันหน่อยน้า"
                            messenger_send_api.send_button(recipient_id, text, buttons)
                        elif next_action['next_action'] == 'bot.validation.get_data.herb_photo':
                            user_label_herb_name = next_action['tracker']['slots']['herb']
                        elif next_action['next_action'] == 'bot.utter.thankyou':
                            messenger_send_api.respond(recipient_id, "ขอบคุณครับ ถ้ามีอะไรให้ลูกสมุนไพรช่วยอีกก็บอกได้เลยนะครับ")
                        else:
                            logger.debug("Action %s is unknown")
                            messenger_send_api.respond(recipient_id, "ตอนนี้ลูกสมุนไพรงงไปหมดแล้วว่าต้องทำอะไร")
                            break
                        next_action = nlu_continue(agent, next_action)
                        messenger_send_api.debug_respond(recipient_id, next_action['next_action'])
                        logger.debug("(" + recipient_id + ")(" + text + "): %s", next_action)
                    # messenger_send_api.respond(recipient_id, "คุณตอบว่า " + text)
                    # messenger_send_api.respond(recipient_id, "อยากถามอะไรอีกมั้ยฮะ")
                # if user sends us a GIF, photo,video, or any other non-text item
                if message['message'].get('attachments'):
                    logger.info(recipient_id + " sends " + "\"" + "attachment" + "\"")
                    response_sent_nontext = "ตอนนี้ลูกสมุนไพรสนใจแต่ข้อความนะครับ"
                    messenger_send_api.respond(recipient_id, response_sent_nontext)


def nlu_continue(agent, next_action):
    next_action = agent.continue_message_handling(executed_action=next_action['next_action'],
                                                  sender_id=next_action['tracker']['sender_id'],
                                                  events=[])
    return next_action


def nlu_start(recipient_id, text):
    rasa_nlu_interpreter_path = os.path.join(os.getcwd(), "rasa", "models", "nlu", "default", "current")
    interpreter = RasaNLUInterpreter(rasa_nlu_interpreter_path)
    rasa_nlu_dialogue_path = os.path.join(os.getcwd(), "rasa", "models", "dialogue")
    agent = Agent.load(rasa_nlu_dialogue_path, interpreter=interpreter)
    next_action = agent.start_message_handling(text, sender_id=recipient_id)
    return agent, next_action


def get_random_message():
    sample_responses = ["อู้หยังนิ", "บ่ฮู้เรื่อง", "อู้ไปเรื่อย", "สวัสดีเจ้า", "ต่อนยอน"]
    return random.choice(sample_responses)


def get_herb_info_from_database(herb_name):
    matched_herb_list = [x for x in herb_json_array if herb_name in set(x['thaiNameList'])]
    if len(matched_herb_list) == 0:
        return HERB_NOT_FOUND
    return matched_herb_list[0]

def get_image_path_from_herb(matched_herb):
    if not matched_herb:
        return IMAGE_NOT_FOUND
    image_directory_path = os.path.join('herb_data', 'herb_images_png', str(matched_herb['herbId']))
    logger.debug("(" + str(matched_herb['herbId']) + ") " + ','.join(matched_herb['thaiNameList']))
    if not os.path.isdir(image_directory_path):
        return IMAGE_NOT_FOUND
    herb_file_list = os.listdir(image_directory_path)
    randomed_file_number = random.randint(0, len(
        [name for name in os.listdir(image_directory_path) if
         os.path.isfile(os.path.join(image_directory_path, name))]))
    selected_herb_file = herb_file_list[randomed_file_number]
    image_path = os.path.join(image_directory_path, selected_herb_file)
    image_path = os.path.abspath(image_path)
    return image_path
