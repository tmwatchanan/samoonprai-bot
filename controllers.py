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
IMAGE_API_URI = 'http://localhost:5001'
BOT_NAME = 'ลูกไพร'
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
                r = messenger_send_api.send_sender_action(recipient_id, 'mark_seen')
                user_info = messenger_send_api.get_user_info(recipient_id, ['first_name', 'last_name'])
                user_name = user_info['first_name'] if user_info else ''
                # print(user_info)
                text = message['message'].get('text')
                # if message['message'].get('attachments')[0].get('type') == 'image':
                image_url = None
                if message['message'].get('attachments'):
                    image_url = message['message']['attachments'][0].get('payload').get('url')
                agent = None
                next_action = None
                if image_url:
                    agent, next_action = nlu_start(recipient_id, "ส่งรูปภาพ")
                    logger.info(recipient_id + " sends " + "\"" + "an image in attachment" + "\"")
                if text:
                    agent, next_action = nlu_start(recipient_id, text)
                    # logger.info(recipient_id + " sends " + "\"" + text.encode('utf-8') + "\"")
                    # messenger_send_api.debug_respond(recipient_id, next_action['next_action'])
                herb_name = next_action.get('tracker').get('slots').get('herb')
                print(herb_name)
                logger.debug("(" + recipient_id + ")(" + text + "): %s", next_action)
                predicted_herb_name = None
                print(next_action)
                while next_action['next_action'] != 'action_listen':
                    messenger_send_api.send_sender_action(recipient_id, 'typing_on')
                    now_action = next_action['next_action']
                    next_action = agent.continue_message_handling(executed_action=next_action['next_action'],
                                                                  sender_id=next_action['tracker']['sender_id'],
                                                                  events=[])
                    # next_action = run_action(now_action,next_action)
                    next_action = run_action(agent, herb_name, image_url, now_action, next_action, recipient_id,
                                             user_name)
                    print(next_action)
                    # next_action = nlu_continue(agent, next_action)
                    # print("next")
                    # print(next_action)
                    # messenger_send_api.debug_respond(recipient_id, next_action['next_action'])
                    # logger.debug("(%s)(%s): %s", recipient_id, text, next_action)
                    messenger_send_api.send_sender_action(recipient_id, 'typing_off')

                # if user sends us a GIF, photo,video, or any other non-text item
                # messenger_send_api.respond(recipient_id, "OK")
                # response_sent_nontext = "ตอนนี้ลูกสมุนไพรสนใจแต่ข้อความนะครับ"
                # if message['message'].get('attachments')[0].get('type') == 'image':
                #     # messenger_send_api.debug_respond(recipient_id, next_action['next_action'])
                #     logger.debug("(%s)(%s): %s", recipient_id, text, next_action)


def run_action(agent, herb_name, image_url, now_action, next_action, recipient_id, user_name):
    if now_action == 'bot.utter.greeting':
        greeting_text = random_greeting_text(user_name)
        messenger_send_api.respond(recipient_id, greeting_text)
        carousel_elements = [
            {
                'title': "ค้นหาชื่อสมุนไพรจากรูปภาพ",
                'subtitle': "ค้นหาสมุนไพรจากรูป",
                # 'image_url': 'https://raw.githubusercontent.com/fbsamples/messenger-platform-samples/master/images/messenger_banner.png',
                'buttons': [
                    {
                        'type': 'postback',
                        'title': "ค้นหาชื่อสมุนไพร",
                        'payload': "ค้นหาสมุนไพรจากรูป"
                    }
                ]
            },
            {
                'title': "ค้นหารูปภาพของสมุนไพรจากชื่อ",
                'subtitle': "รายละเอียดค้นหารูปภาพ",
                # 'image_url': 'https://raw.githubusercontent.com/fbsamples/messenger-platform-samples/master/images/messenger_banner.png',
                'buttons': [
                    {
                        'type': 'postback',
                        'title': "ค้นหารูปสมุนไพร",
                        'payload': "ดูรูปสมุนไพร"
                    }
                ]
            },
            {
                'title': "ค้นหาข้อมูลทั่วไปของสมุนไพรจากชื่อ",
                'subtitle': "รายละเอียด...",
                # 'image_url': 'https://raw.githubusercontent.com/fbsamples/messenger-platform-samples/master/images/messenger_banner.png',
                'buttons': [
                    {
                        'type': 'postback',
                        'title': "ค้นหาข้อมูลทั่วไป",
                        'payload': "ดูข้อมูลทั่วไป"
                    }
                ]
            },
            {
                'title': "ค้นหาสรรพคุณของสมุนไพรจากชื่อ",
                'subtitle': "รายละเอียด...",
                # 'image_url': 'https://raw.githubusercontent.com/fbsamples/messenger-platform-samples/master/images/messenger_banner.png',
                'buttons': [
                    {
                        'type': 'postback',
                        'title': "ค้นหาสรรพคุณ",
                        'payload': "สรรพคุณสมุนไพร"
                    }
                ]
            },
            {
                'title': "ช่วยแนะนำสมุนไพรจากสรรพคุณ",
                'subtitle': "รายละเอียด...",
                # 'image_url': 'https://raw.githubusercontent.com/fbsamples/messenger-platform-samples/master/images/messenger_banner.png',
                'buttons': [
                    {
                        'type': 'postback',
                        'title': "หาสมุนไพร",
                        'payload': "หาสมุนไพรจากสรรพคุณ"
                    }
                ]
            }
        ]
        carousel_result = messenger_send_api.send_generic_template(recipient_id, carousel_elements)
    elif now_action == 'bot.ask.photo':
        ask_photo_text = random_ask_photo_text(user_name)
        response_result = messenger_send_api.respond(recipient_id, ask_photo_text)
    elif now_action == 'bot.ask.name_to_photo.herb_name':
        ask_name_to_photo_herb_name_text = random_ask_name_to_photo_herb_name_text(user_name)
        response_result = messenger_send_api.respond(recipient_id, ask_name_to_photo_herb_name_text)
    elif now_action == 'bot.ask.get_data':
        messenger_send_api.respond(recipient_id, "ช่วยบอกน้อง" + BOT_NAME + "หน่อยได้ไหมครับ ว่าจริง ๆ แล้วมันสมุนไพรอะไร (เช่น \"มันคือมะนาว\")")
    elif now_action == 'bot.ask.name_to_benefit.herb_name':
        ask_name_to_benefit_herb_name_text = random_ask_name_to_benefit_herb_name_text
        response_result = messenger_send_api.respond(recipient_id, ask_name_to_benefit_herb_name_text)
    elif now_action == 'bot.action.name_to_photo':
        herb_object = get_herb_info_from_database(herb_name)
        if herb_object == HERB_NOT_FOUND:
            next_action = nlu_trigger(agent, recipient_id, "ไม่พบสมุนไพร")
            # messenger_send_api.respond(recipient_id, "ขออภัยครับ ตอนนี้ลูกสมุนไพรไม่รู้จักสมุนไพรชื่อ" + herb_name + "ครับ")
            # break
        else:
            next_action = nlu_trigger(agent, recipient_id, "พบสมุนไพร")
            searching_image_text = random_searching_image_text(user_name, herb_name)
            response_result = messenger_send_api.respond(recipient_id, searching_image_text)
    elif now_action == 'bot.action.photo_to_name':
        searching_herb_name_text = random_searching_herb_name_text(user_name)
        messenger_send_api.respond(recipient_id, searching_herb_name_text)
        print("BEFORE CALL_HERB_CLASSIFICATION")
        predicted_herb_name = call_herb_classification(image_url)
        print("CALL_HERB_CLASSIFICATION HERE!")
        print(predicted_herb_name)
        if predicted_herb_name:
            next_action = nlu_trigger(agent, recipient_id, 'พบสมุนไพร')
            print("พบสมุนไพร")
        else:
            next_action = nlu_trigger(agent, recipient_id, 'ไม่พบสมุนไพร')
            print("ไม่พบสมุนไพร")
    elif now_action == 'bot.action.name_to_benefit':
        name_to_benefit_text = random_name_to_benefit_text(user_name, herb_name)
        response_result = messenger_send_api.respond(recipient_id, name_to_benefit_text)
    elif now_action == 'bot.action.name_to_detail':
        name_to_detail_text = random_name_to_detail_text(user_name, herb_name)
        response_result = messenger_send_api.respond(recipient_id, name_to_detail_text)
    elif now_action == 'bot.utter.herb_photo':
        herb_object = get_herb_info_from_database(herb_name)
        image_path = get_image_path_from_herb(herb_object)
        if image_path == IMAGE_NOT_FOUND:
            image_not_found_text = random_image_not_found_text(user_name, herb_name)
            messenger_send_api.respond(recipient_id, image_not_found_text)
        else:
            image_found_text = random_image_found_text(user_name, herb_name)
            messenger_send_api.respond(recipient_id, image_found_text)
            send_api_response = messenger_send_api.send_image(recipient_id, image_path)
            print(send_api_response)
    elif now_action == 'bot.utter.thankyou':
        messenger_send_api.respond(recipient_id, "ขอบคุณครับ ถ้ามีอะไรให้" + BOT_NAME + "ช่วยอีกก็บอกได้เลยนะครับ")
    elif now_action == 'bot.utter.herb_name':
        found_herb_name_text = random_found_herb_name_text(user_name, herb_name)
        messenger_send_api.respond(recipient_id, found_herb_name_text)
    elif now_action == 'bot.utter.herb_name.not_found':
        not_found_herb_name_text = random_not_found_herb_name_text(user_name)
        messenger_send_api.respond(recipient_id, not_found_herb_name_text)
    elif now_action == 'bot.validation.herb_photo':
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
        quick_reply = {
            'content_type': 'text',
            'title': 'ไม่แน่ใจ',
            "payload": "unsure"
        }
        quick_replies.append(quick_reply)
        image_validation_text = random_image_validation_text(user_name, herb_name)
        messenger_send_api.send_quick_replies(recipient_id, image_validation_text, quick_replies)
    elif now_action == 'bot.validation.herb_name':
        validate_herb_name_text = random_validate_herb_name_text(user_name, herb_name)
        messenger_send_api.respond(recipient_id, validate_herb_name_text)
    elif now_action == 'bot.validation.get_data.herb_name':
        user_label_herb_name = next_action.get('tracker').get('slots').get('herb')
        thx_label_text = random_thx_label_text(user_name, herb_name)
        messenger_send_api.respond(recipient_id, thx_label_text)
    elif now_action == 'bot.validation.get_data.herb_photo':
        user_label_herb_name = next_action.get('tracker').get('slots').get('herb')
        thx_label_text = random_thx_label_text(user_name, herb_name)
        messenger_send_api.respond(recipient_id, thx_label_text)
    else:
        logger.debug("Action %s is unknown")
        messenger_send_api.respond(recipient_id, "ตอนนี้" + BOT_NAME + "งงไปหมดแล้วว่าต้องทำอะไร")
    return next_action


def call_herb_classification(image_url):
    data = {
        'url': image_url
    }
    try:
        response = requests.post(
            IMAGE_API_URI + "/classify/url",
            json=data,
        )
        response_json = response.json()
        print(response_json)
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
        return predicted_herb_name
    except requests.exceptions.RequestException as e:
        logger.error(e)
        # messenger_send_api.respond(recipient_id, "ขออภัยครับ ตอนนี้" + BOT_NAME + "คิดไม่ออกว่ารูปนี้คือสมุนไพรรูปอะไร ไว้ลองใหม่นะครับ")
    return None


def nlu_continue(agent, next_action):
    next_action = agent.continue_message_handling(executed_action=next_action['next_action'],
                                                  sender_id=next_action['tracker']['sender_id'],
                                                  events=[])
    return next_action


def nlu_trigger(agent, recipient_id, text):
    next_action = agent.start_message_handling(text, sender_id=recipient_id)
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
        "สวัสดีครับ ผม" + BOT_NAME + " เด็กรอบรู้เรื่องสมุนไพรไทย ยินดีให้คำปรึกษาครับ\nวันนี้พี่ " + user_name + " มีอะไรสงสัยถาม" + BOT_NAME + "ได้เลยครับ",
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


def random_searching_herb_name_text(user_name):
    searching_herb_name_list = [
        BOT_NAME + "เห็นรูปแล้ว เดี๋ยวช่วยค้นให้นะครับว่าเป็นสมุนไพรชื่ออะไร รอสักครู่ครับ",
        "รอแป๊บนึงนะครับพี่ " + user_name + " เดี่ยว" + BOT_NAME + "หาให้นี่ว่าเป็นสมุนไพรอะไร"
    ]
    return random.SystemRandom().choice(searching_herb_name_list)


def random_found_herb_name_text(user_name, herb_name):
    found_herb_name_list = [
        BOT_NAME + "เจอแล้ว รูปนี้เป็นรูปของ" + herb_name,
        "รูปนี้คือ" + herb_name + "ไง " + BOT_NAME + "ว่านะ"
    ]
    return random.SystemRandom().choice(found_herb_name_list)


def random_not_found_herb_name_text(user_name):
    not_found_herb_name_list = [
        BOT_NAME + "ขอโทษด้วยนะครับ " + BOT_NAME + "ไม่รู้ว่ามันคืออะไร ช่วยบอกหน่อยได้ไหมครับ"
    ]
    return random.SystemRandom().choice(not_found_herb_name_list)


def random_validate_herb_name_text(user_name, herb_name):
    validate_herb_name_text_list = [
        "พี่" + user_name + " ช่วยยืนยันได้ไหมครับว่ารูปที่ส่งมาคือ" + herb_name + "หรือเปล่า"
    ]
    return random.SystemRandom().choice(validate_herb_name_text_list)


def random_ask_photo_text(user_name):
    ask_photo_text_list = [
        "พี่" + user_name + " รบกวนช่วยส่งรูปของสมุนไพรให้น้อง" + BOT_NAME + "หน่อยครับ",
        BOT_NAME + "ต้องให้พี่ " + user_name + " ส่งรูปสมุนไพรให้หน่อยครับ"
    ]
    return random.SystemRandom().choice(ask_photo_text_list)


def random_ask_name_to_photo_herb_name_text(user_name):
    ask_name_to_photo_herb_name_text_list = [
        "พี่" + user_name + " รบกวนช่วยบอกชื่อสมุนไพรให้น้อง" + BOT_NAME + "หน่อยครับ",
        BOT_NAME + "ต้องให้พี่ " + user_name + " บอกชื่อสมุนไพรที่อยากดูรูปครับ",
        "ช่วยบอกน้อง" + BOT_NAME + "หน่อยครับว่าอยากดูรูปของสมุนไพรชื่ออะไร"
    ]
    return random.SystemRandom().choice(ask_name_to_photo_herb_name_text_list)


def random_name_to_benefit_text(user_name, herb_name):
    random_name_to_benefit_text_list = [
        "รอสักครู่ครับ เดี๋ยว" + BOT_NAME + "ช่วยค้นสรรพคุณของ" + herb_name + "ให้ครับ",
        "รอแป๊บนึงนะครับพี่ " + user_name + " เดี่ยว" + BOT_NAME + "หาสรรพคุณของ" + herb_name + "ให้นะครับ"
    ]
    return random.SystemRandom().choice(random_name_to_benefit_text_list)


def random_name_to_detail_text(user_name, herb_name):
    random_name_to_detail_text_list = [
        "รอสักครู่ครับ เดี๋ยว" + BOT_NAME + "ช่วยค้นข้อมูลทั่วไปของ" + herb_name + "ให้ครับ",
        "รอแป๊บนึงนะครับพี่ " + user_name + " เดี่ยว" + BOT_NAME + "หาข้อมูลทั่วไปของ" + herb_name + "ให้นะครับ"
    ]
    return random.SystemRandom().choice(random_name_to_detail_text_list)


def random_ask_name_to_benefit_herb_name_text(user_name):
    ask_name_to_benefit_herb_name_text_list = [
        "พี่" + user_name + " รบกวนช่วยบอกชื่อสมุนไพรให้น้อง" + BOT_NAME + "หน่อยครับ",
        BOT_NAME + "ต้องให้พี่ " + user_name + " บอกชื่อสมุนไพรที่อยากรู้สรรพคุณให้หน่อยครับ",
        "ช่วยบอกน้อง" + BOT_NAME + "หน่อยครับว่าอยากดูสรรพคุณของสมุนไพรชื่ออะไร"
    ]
    return random.SystemRandom().choice(ask_name_to_benefit_herb_name_text_list)
