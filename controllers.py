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
import requests

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
BOT_NAME = "ลูกไพร"
HERB_NOT_FOUND, IMAGE_NOT_FOUND, *_ = range(100)


def process_incoming_message(payload):
    for event in payload['entry']:
        messaging = event['messaging']
        for message in messaging:
            if message.get('message'):
                # Facebook Messenger ID for user so we know where to send response back to
                recipient_id = message['sender']['id']
                """ https://developers.facebook.com/docs/messenger-platform/webhook#response
                Required 200 OK Response or Sender Actions to notify that the message has been received
                """
                messenger_send_api.send_sender_action(recipient_id, 'mark_seen')
                text = message['message'].get('text')
                user_info = messenger_send_api.get_user_info(recipient_id, ['first_name', 'last_name'])
                user_name = user_info['first_name'] if user_info else ''
                print(user_info)
                if text:
                    # messenger_send_api.send_response(recipient, )
                    # Get Next action from input user message
                    messenger_send_api.send_sender_action(recipient_id, 'typing_on')
                    logger.info(recipient_id + " sends " + "\"" + text + "\"")
                    agent, next_action = nlu_start(recipient_id, text)
                    # messenger_send_api.debug_respond(recipient_id, next_action['next_action'])
                    herb_name = next_action['tracker']['slots']['herb']
                    herb_object = None
                    if herb_name is None:
                        herb_name = ''
                        herb_object = HERB_NOT_FOUND
                    logger.debug("(" + recipient_id + ")(" + text + "): %s", next_action)
                    while next_action['next_action'] != 'action_listen':
                        if next_action['next_action'] == 'bot.utter.greeting':
                            greeting_text = random_greeting_text(user_name)
                            messenger_send_api.respond(recipient_id, greeting_text)
                        elif next_action['next_action'] == 'bot.action.name_to_photo':
                            if herb_object == HERB_NOT_FOUND:
                                messenger_send_api.respond(recipient_id, "ขออภัยครับ ตอนนี้ลูกสมุนไพรไม่รู้จักสมุนไพรชื่อ" + herb_name + "ครับ")
                                break
                            else:
                                herb_object = get_herb_info_from_database(herb_name)
                                searching_image_text = random_searching_image_text(user_name, herb_name)
                                messenger_send_api.respond(recipient_id, searching_image_text)
                        elif next_action['next_action'] == 'bot.utter.herb_photo':
                            image_path = get_image_path_from_herb(herb_object)
                            if image_path == IMAGE_NOT_FOUND:
                                image_not_found_text =  random_image_not_found_text(user_name, herb_name)
                                messenger_send_api.respond(recipient_id, image_not_found_text)
                                break
                            else:
                                image_found_text =  random_image_found_text(user_name, herb_name)
                                messenger_send_api.respond(recipient_id, image_found_text)
                                send_api_response = messenger_send_api.send_image(recipient_id, image_path)
                        elif next_action['next_action'] == 'bot.validation.herb_photo':
                            quick_replies = []
                            quick_reply = {
                                'content_type': 'text',
                                'title': 'ใช่',
                                "payload": "correct"
                            }
                            quick_replies.append(quick_reply)
                            quick_reply = {
                                'content_type': 'text',
                                'title': 'ไม่ใช่',
                                "payload": "wrong"
                            }
                            quick_replies.append(quick_reply)
                            image_validation_text = random_image_validation_text(user_name, herb_name)
                            messenger_send_api.send_quick_replies(recipient_id, image_validation_text, quick_replies)
                        elif next_action['next_action'] == 'bot.validation.get_data.herb_photo':
                            user_label_herb_name = next_action['tracker']['slots']['herb']
                            thx_label_text = random_thx_label_text(user_name, herb_name)
                            messenger_send_api.respond(recipient_id, thx_label_text)
                        elif next_action['next_action'] == 'bot.utter.thankyou':
                            messenger_send_api.respond(recipient_id, "ขอบคุณครับ ถ้ามีอะไรให้" + BOT_NAME + "ช่วยอีกก็บอกได้เลยนะครับ")
                        else:
                            logger.debug("Action %s is unknown")
                            messenger_send_api.respond(recipient_id, "ตอนนี้" + BOT_NAME + "งงไปหมดแล้วว่าต้องทำอะไร")
                            break
                        next_action = nlu_continue(agent, next_action)
                        # messenger_send_api.debug_respond(recipient_id, next_action['next_action'])
                        logger.debug("(" + recipient_id + ")(" + text + "): %s", next_action)
                    # messenger_send_api.respond(recipient_id, "คุณตอบว่า " + text)
                    # messenger_send_api.respond(recipient_id, "อยากถามอะไรอีกมั้ยฮะ")
                    messenger_send_api.send_sender_action(recipient_id, 'typing_off')
                # if user sends us a GIF, photo,video, or any other non-text item
                if message['message'].get('attachments'):
                    logger.info(recipient_id + " sends " + "\"" + "attachment" + "\"")
                    # response_sent_nontext = "ตอนนี้ลูกสมุนไพรสนใจแต่ข้อความนะครับ"
                    data = {
                        'url': message['message']['attachments'][0]['payload']['url']
                    }
                    try:
                        response = requests.post(
                            "http://localhost:5001/classify/url",
                            json=data,
                        )
                        response_json = response.json()
                        predicted_herb_tmp_name = response_json['results'][0]['label']
                        map_herb_name = {
                            'kokchang': 'กกช้าง',
                            'kokrungka': 'กกลังกา',
                            'krajeabdang': 'กระเจี๊ยบแดง',
                            'kwawkruekaw': 'กวาวเครือขาว',
                            'kangfang': 'แก่นฝาง',
                            'kaminchun': 'ขมิ้นชัน',
                            'chakeaw': 'ชาเขียว',
                            'tungchao': 'ถั่งเช่า',
                            'borapet': 'บอระเพ็ด',
                            'plalhaipruek': 'ปลาไหลเผือก',
                            'fang': 'ฝาง',
                            'plukaow': 'พลูคาว',
                            'yahnang': 'ย่านาง',
                            'rangjued': 'รางจืด',
                            'looktaibai': 'ลูกใต้ใบ',
                            'wanhang': 'ว่านหางจระเข้',
                            'somkorea': 'โสมเกาหลี',
                            'obchei': 'อบเชย'
                        }
                        predicted_herb_name = map_herb_name[predicted_herb_tmp_name]
                        messenger_send_api.respond(recipient_id, "ถ้า" + BOT_NAME + "เดาไม่ผิด รูปนี้น่าจะเป็น" + predicted_herb_name + "นะครับ")
                    except requests.exceptions.RequestException as e:
                        logger.error(e)
                        messenger_send_api.respond(recipient_id, "ขออภัยครับ ตอนนี้" + BOT_NAME + "คิดไม่ออกว่ารูปนี้คือสมุนไพรรูปอะไร ไว้ลองใหม่นะครับ")


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
    selected_herb_file = random.SystemRandom().choice(herb_file_list)
    image_path = os.path.join(image_directory_path, selected_herb_file)
    image_path = os.path.abspath(image_path)
    return image_path


def random_greeting_text(user_name):
    greeting_text_list = [
        "สวัสดีครับ ผม" + BOT_NAME + " เด็กรอบรู้เรื่องสมุนไพรไทย ยินดีให้คำปรึกษาครับ\nวันนี้พี่" + user_name + " มีอะไรสงสัยถาม" + BOT_NAME + "ได้เลยครับ",
        "สวัสดีคร้าบ " + BOT_NAME + "พร้อมให้คำปรึกษาพี่ " + user_name + " เรื่องสมุนไพรแล้วครับ",
        BOT_NAME + "เองครับ พี่ " + user_name + " อยากจะถามอะไรผม ว่ามาได้เลยครับ"
    ]
    return random.SystemRandom().choice(greeting_text_list)


def random_searching_image_text(user_name, herb_name):
    searching_image_text_list = [
        "เดี๋ยว" + BOT_NAME + "ขอเวลาค้นหารูป" + herb_name + "สักครู่นะครับ",
        "รอสักครู่คร้าบ " + BOT_NAME + "กำลังหารูปของ" + herb_name + "ให้ครับ",
        "พี่ " + user_name + " รอแป๊บนึงนะ " + BOT_NAME + "กำลังหารูป" + herb_name + "อยู่ครับผม"
    ]
    return random.SystemRandom().choice(searching_image_text_list)


def random_image_not_found_text(user_name, herb_name):
    image_not_found_text_list = [
        "นี่ ๆ " + BOT_NAME + "หารูปของ" + herb_name + "ไม่เจอแฮะครับ",
        "พี่ " + user_name + " จ๋า ขออภัยนะ น้องหารูป" + herb_name + "ไม่ได้ครับ",
        BOT_NAME + "หารูป" + herb_name + "ไม่เจอ ขอโทษด้วยนะครับ",
        "ขออภัยครับ ตอนนนี้" + BOT_NAME + "ยังไม่มีรูป" + herb_name + "ครับ"
    ]
    return random.SystemRandom().choice(image_not_found_text_list)


def random_image_found_text(user_name, herb_name):
    image_found_text_list = [
        "นี่ ๆ " + BOT_NAME + "หารูปของ" + herb_name + "เสร็จแล้วครับ",
        "พี่ " + user_name + " นี่ไง รูปของ" + herb_name + "อะครับ",
        BOT_NAME + "หารูป" + herb_name + "มาให้แล้วน้า",
        "ขออภัยที่ให้รอครับ " + BOT_NAME + "เอารูป" + herb_name + "มาให้แล้วครับ"
    ]
    return random.SystemRandom().choice(image_found_text_list)


def random_image_validation_text(user_name, herb_name):
    image_validation_text_list = [
        "พี่ช่วยบอก" + BOT_NAME + "หน่อยได้มั้ยครับว่ารูปนี้ใช่รูปของ" + herb_name + "มั้ยครับ",
        "พี่ " + user_name + " ช่วยบอก" + BOT_NAME + "หน่อยได้มั้ยครับว่ารูปนี้ใช่รูปของ" + herb_name + "มั้ยครับ",
        "รูปนี้ใช่" + herb_name + "มั้ยครับ ช่วย" + BOT_NAME + "ยืนยันหน่อยน้า"
    ]
    return random.SystemRandom().choice(image_validation_text_list)


def random_thx_label_text(user_name, herb_name):
    thx_label_text_list = [
        "ขอบคุณสำหรับข้อมูลนะครับ " + BOT_NAME + "จะนำไปพัฒนาให้ตัวเองเก่งขึ้นครับ"
    ]
    return random.SystemRandom().choice(thx_label_text_list)
