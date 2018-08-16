#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Messenger Platform
from datetime import date

import messenger_send_api
import sheets_api
# Utilities
import random
import os
import json
import logging
import requests
from fuzzywuzzy import fuzz
from numpy import asarray

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
herb_feature_json_array = None
with open(os.path.join('herb_data', 'herb_features.json'), encoding="utf-8") as f:
    herb_feature_json_array = json.load(f)
source_website_json_array = None
with open(os.path.join('herb_data', 'source_websites.json'), encoding="utf-8") as f:
    source_website_json_array = json.load(f)


def expand_herb_json_array(herb_json_array):
    expanded_herb_json_array = []
    for herb_json in herb_json_array:
        for thaiName in herb_json['thaiNameList']:
            expanded_herb_json_array.append({
                'herbId': herb_json['herbId'],
                'thaiName': thaiName
            })
    return expanded_herb_json_array


expanded_herb_json_array = expand_herb_json_array(herb_json_array)


# DEFINE CONSTANTS
IMAGE_API_URI = 'http://localhost:5001'
RASA_SERVER_API_URI = 'http://localhost:5005'
BOT_NAME = 'ลูกไพร'
HERB_NOT_FOUND, IMAGE_NOT_FOUND, *_ = range(100)


def process_incoming_message(payload):
    for event in payload['entry']:
        messaging = event['messaging']
        for message in messaging:
            if message.get('message') or message.get('postback'):
                recipient_id = message['sender']['id']
                messenger_send_api.send_sender_action(recipient_id, 'mark_seen')
                user_info = messenger_send_api.get_user_info(recipient_id, ['first_name', 'last_name'])
                user_name = user_info['first_name'] if user_info else ''
                text = image_url = None
                if message.get('postback'):
                    text = message['postback']['payload']
                elif message.get('message'):
                    text = message['message'].get('text')
                    if message['message'].get('attachments'):
                        image_url = message['message']['attachments'][0].get('payload').get('url')
                next_action = None
                if text:
                    # if text ==
                    next_action = rasa_api_start(recipient_id, text)
                    # logger.info(recipient_id + " sends " + "\"" + text + "\"")
                if image_url:
                    next_action = rasa_api_start(recipient_id, "ส่งรูปภาพ")
                    logger.info(recipient_id + " sends " + "\"" + "an image in attachment" + "\"")
                herb_name = next_action.get('tracker').get('slots').get('herb')
                entities = next_action.get('tracker').get('latest_message').get('entities')
                feature_list = get_feature_list_from_entities(entities)
                data_payload = {
                    'user': {
                        'id': recipient_id,
                        'name': user_name
                    },
                    'userChatHerbName': herb_name,
                    'userChatImageUrl': image_url,
                    'userChatFeatureList': feature_list
                }
                # messenger_send_api.debug_respond(recipient_id, recipient_id + " " + next_action['next_action'])
                while next_action['next_action'] != 'action_listen':
                    now_action = next_action['next_action']
                    if now_action != 'action_slot_reset':
                        messenger_send_api.send_sender_action(recipient_id, 'typing_on')
                    next_action = run_action(next_action, data_payload)
                    # messenger_send_api.debug_respond(recipient_id, data_payload['user']['id'] + " " + next_action['next_action'])
                    if now_action != 'bot.action.photo_to_name':
                        messenger_send_api.send_sender_action(recipient_id, 'typing_off')

                # if user sends us a GIF, photo,video, or any other non-text item
                # if message['message'].get('attachments')[0].get('type') == 'image':


def run_action(now_action, data_payload):
    action = now_action['next_action']
    next_action = None
    logger.info(data_payload['user']['id'] + " has action " + action)

    if action == 'bot.utter.greeting':
        next_action = action_bot_utter_greeting(now_action, data_payload)
    elif action == 'bot.ask.photo':
        next_action = action_bot_ask_photo(now_action, data_payload)
    elif action == 'bot.ask.name_to_photo.herb_name':
        next_action = action_bot_ask_name_to_photo_herb_name(now_action, data_payload)
    elif action == 'bot.ask.get_data':
        next_action = rasa_api_continue(now_action, events=[])
        action_bot_ask_get_data(data_payload)
    elif action == 'bot.ask.name_to_benefit.herb_name':
        next_action = rasa_api_continue(now_action, events=[])
        action_ask_name_to_benefit_herb_name(data_payload)
    elif action == 'bot.ask.name_to_detail.herb_name':
        next_action = rasa_api_continue(now_action, events=[])
        action_ask_name_to_detail_herb_name(data_payload)
    elif action == 'bot.ask.validate.herb':
        next_action = action_ask_validate_herb(now_action, data_payload)
    elif action == 'bot.ask.feature_to_herb.feature':
        next_action = rasa_api_continue(now_action, events=[])
        action_ask_feature_to_herb_feature(data_payload)
    elif action == 'bot.action.validate.herb':
        next_action = action_action_validate_herb(now_action, data_payload)
    elif action == 'bot.action.name_to_photo':
        next_action = action_action_name_to_photo(now_action, data_payload)
    elif action == 'bot.action.photo_to_name':
        next_action = action_action_photo_name(now_action, data_payload)
    elif action == 'bot.action.name_to_benefit':
        next_action = action_action_name_to_benefit(now_action, data_payload)
    elif action == 'bot.action.name_to_detail':
        next_action = action_action_name_to_detail(now_action, data_payload)
    elif action == 'bot.action.feature_to_herb':
        next_action = action_action_feature_to_herb(now_action, data_payload)
    elif action == 'bot.utter.herb_photo':
        next_action = action_utter_herb_photo(now_action, data_payload)
    elif action == 'bot.utter.herb_photo.not_found':
        next_action = rasa_api_continue(now_action, events=[])
        action_utter_herb_photo_not_found(data_payload)
    elif action == 'bot.utter.thankyou':
        next_action = rasa_api_continue(now_action, events=[])
        action_utter_thankyou(data_payload)
    elif action == 'bot.utter.herb_name':
        next_action = action_utter_herb_name(now_action, data_payload)
    elif action == 'bot.utter.herb_name.not_found':
        next_action = rasa_api_continue(now_action, events=[])
        action_utter_herb_name_not_found(data_payload)
    elif action == 'bot.utter.benefit':
        next_action = rasa_api_continue(now_action, events=get_event_slot(herb_name=data_payload['userChatHerbName']))
        action_utter_benefit(data_payload)
    elif action == 'bot.utter.benefit.not_found':
        next_action = rasa_api_continue(now_action, events=[])
        action_utter_benefit_not_found(data_payload)
    elif action == 'bot.utter.detail':
        next_action = rasa_api_continue(now_action, events=get_event_slot(herb_name=data_payload['userChatHerbName']))
        action_utter_detail(data_payload)
    elif action == 'bot.utter.detail.not_found':
        next_action = action_utter_detail_not_found(data_payload)
    elif action == 'bot.utter.herb_feature':
        next_action = action_utter_herb_feature(now_action, data_payload)
    elif action == 'bot.utter.herb_feature.not_found':
        next_action = rasa_api_continue(now_action, events=[])
        action_utter_herb_feature_not_found(data_payload)
    elif action == 'bot.validation.herb_photo':
        next_action = action_validation_herb_photo(now_action, data_payload)
    elif action == 'bot.validation.herb_name':
        next_action = action_validation_herb_name(now_action, data_payload)
    elif action == 'bot.validation.get_data.herb_name':
        next_action = action_validation_get_data_herb_name(now_action, data_payload)
    elif action == 'bot.validation.get_data.herb_photo':
        next_action = action_validation_get_data_herb_photo(action, data_payload)
    elif action == 'bot.default.ask_more':
        next_action = rasa_api_continue(now_action, events=[])
        action_default_ask_more(data_payload)
    elif action == 'bot.utter.default.about_bot':
        next_action = rasa_api_continue(now_action, events=[])
        action_utter_default_about_bot(data_payload)
    elif action == 'action_slot_reset':
        next_action = rasa_api_continue(now_action, events=get_event_slot_reset())
    else:
        logger.debug("Action %s is unknown")
        messenger_send_api.respond(data_payload['user']['id'], "ตอนนี้" + BOT_NAME + "งงไปหมดแล้วว่าต้องทำอะไร")
    return next_action


def action_utter_default_about_bot(data_payload):
    about_bot_text = BOT_NAME + " ผู้ช่วยอัจฉริยะที่รอบรู้เรื่องสมุนไพรไทย ที่จะทำให้คนไทยเข้าใกล้และรู้จักสมุนไพรไทยมากยิ่งขึ้น ไม่ว่าจะให้ข้อมูลสมุนไพร ค้นหาสมุนไพร หรือต้องการให้แนะนำสมุนไพรเพื่อช่วยรักษาบรรเทาโรคก็สามารถบอก" + BOT_NAME + "มาได้เลย และยิ่งไปกว่านั้น" + BOT_NAME + "ยังสามารถจดจำรูปภาพของสมุนไพรไทยได้อีกด้วย"
    messenger_send_api.respond(data_payload['user']['id'], about_bot_text)


def action_default_ask_more(data_payload):
    ask_more_text = random_ask_more_text(data_payload['user']['name'])
    messenger_send_api.respond(data_payload['user']['id'], ask_more_text)


def action_utter_herb_feature_not_found(data_payload):
    herb_feature_not_found_text = random_herb_feature_not_found_text(data_payload['user']['name'],
                                                       data_payload.get('userChatFeatureList'))
    messenger_send_api.respond(data_payload['user']['id'], herb_feature_not_found_text)



def action_utter_herb_photo_not_found(data_payload):
    image_not_found_text = random_image_not_found_text(data_payload['user']['name'],
                                                       data_payload.get('userChatHerbName'))
    messenger_send_api.respond(data_payload['user']['id'], image_not_found_text)


def action_utter_herb_feature(now_action, data_payload):
    herb_name = get_value_from_slot(now_action, 'herb')
    herb_object = get_herb_object_from_herb_name(herb_name)
    text = herb_object['thaiNameList'][0]
    if len(herb_object['thaiNameList']) > 1:
        text = text + "(" + ', '.join(herb_object['thaiNameList'][1:]) + ") "
    text = text + "เป็นสมุนไพรที่มีสรรพคุณดังนี้" + "\n"
    feature_list = get_value_from_slot(now_action, 'featureList')
    print(herb_name)
    print(feature_list)
    if not feature_list:
        return rasa_api_continue(now_action, events=[])
    feature_detail_list = []
    for herb_feature in herb_object['benefitList']:
        for user_feature in feature_list:
            if user_feature in herb_feature:
                feature_detail_list.append(herb_feature)
                break
    for herb_feature in herb_object['propertyList']:
        for user_feature in feature_list:
            if user_feature in herb_feature:
                feature_detail_list.append(herb_feature)
                break
    num_feature = 2
    random_feature_list = random.sample(feature_detail_list, num_feature if len(feature_detail_list) >= num_feature else len(feature_detail_list))
    for feature in random_feature_list:
        text = text + "• " + feature + "\n"
    buttons = [
        {
            'type': 'web_url',
            'title': "ดูเพิ่มเติม",
            'url': herb_object['sourceUrl']
        }
    ]
    messenger_send_api.send_button(data_payload['user']['id'], text, buttons)
    return rasa_api_continue(now_action, events=[])


def action_action_feature_to_herb(now_action, data_payload):
    finding_feature_to_herb_text = random_finding_feature_to_herb_text(data_payload['user']['name'], data_payload.get('userChatFeatureList'))
    messenger_send_api.respond(data_payload['user']['id'], finding_feature_to_herb_text)
    feature_count_list = [0] * len(herb_json_array)
    selected_feature_list = []
    for feature in data_payload['userChatFeatureList']:
        selected_feature_list.append(find_most_similar_feature(feature))
    if len(selected_feature_list) == 0:
        next_action = rasa_api_continue(now_action, events=[])
        next_action = rasa_api_start(data_payload['user']['id'], "ไม่พบสมุนไพร")
        return next_action
    messenger_send_api.respond(data_payload['user']['id'], "พี่น่าจะหมายถึงสรรพคุณเกี่ยวกับ" + ', '.join(selected_feature_list) + " หรือเปล่าครับ")
    for feature in selected_feature_list:
        for idx, herb_object in enumerate(herb_json_array):
            for benefit in herb_object['benefitList']:
                if feature in benefit:
                    feature_count_list[idx] = feature_count_list[idx] + 1
            for property in herb_object['propertyList']:
                if feature in property:
                    feature_count_list[idx] = feature_count_list[idx] + 1
    m = max(feature_count_list)
    argmax = [i for i,j in enumerate(feature_count_list) if j == m]
    herb_object = HERB_NOT_FOUND
    if max(argmax) > 0:
        random_argmax = random.SystemRandom().choice(argmax)
        herb_object = herb_json_array[random_argmax]
    next_action = None
    if herb_object == HERB_NOT_FOUND:
        next_action = rasa_api_continue(now_action, events=[])
        next_action = rasa_api_start(data_payload['user']['id'], "ไม่พบสมุนไพร")
    else:
        herb_name = herb_object['thaiNameList'][0]
        next_action = rasa_api_continue(now_action, events=get_event_slot(herb_name=herb_name, feature_list=selected_feature_list))
        next_action = rasa_api_start(data_payload['user']['id'], "พบสมุนไพร")
    return next_action


def action_ask_feature_to_herb_feature(data_payload):
    ask_feature_to_herb_text = random_ask_feature_to_herb_text(data_payload['user']['name'])
    messenger_send_api.respond(data_payload['user']['id'], ask_feature_to_herb_text)


def action_utter_detail_not_found(now_action, data_payload):
    detail_not_found_text = random_info_not_found_text(data_payload['user']['name'],
                                                       get_value_from_slot(now_action, 'herb'), info='ข้อมูล')
    messenger_send_api.respond(data_payload['user']['id'], detail_not_found_text)
    return rasa_api_continue(now_action, events=[])


def action_validation_get_data_herb_photo(now_action, data_payload):
    thx_label_text = random_thx_label_text(data_payload['user']['name'])
    messenger_send_api.respond(data_payload['user']['id'], thx_label_text)
    user_label_herb_name = get_value_from_slot(now_action, 'herb')
    file_path = get_value_from_slot(now_action, 'filePath')
    sheets_api.append_image_label(file_path, user_label_herb_name)
    return rasa_api_continue(now_action, events=[])


def action_validation_get_data_herb_name(now_action, data_payload):
    thx_label_text = random_thx_label_text(data_payload['user']['name'])
    messenger_send_api.respond(data_payload['user']['id'], thx_label_text)
    return rasa_api_continue(now_action, events=[])


def action_validation_herb_name(now_action, data_payload):
    quick_replies = [create_reply('ใช่'), create_reply('ไม่ใช่'), create_reply('ไม่แน่ใจ')]
    validation_herb_name_text = random_validation_herb_name_text(data_payload['user']['name'],
                                                                 get_value_from_slot(now_action, 'herb'))
    messenger_send_api.send_quick_replies(data_payload['user']['id'], validation_herb_name_text, quick_replies)
    return rasa_api_continue(now_action, events=[])


def action_validation_herb_photo(now_action, data_payload):
    quick_replies = [create_reply('ใช่'), create_reply('ไม่ใช่'), create_reply('ไม่แน่ใจ')]
    validation_herb_photo_text = random_validation_herb_photo_text(data_payload['user']['name'],
                                                                   get_value_from_slot(now_action, 'herb'))
    messenger_send_api.send_quick_replies(data_payload['user']['id'], validation_herb_photo_text, quick_replies)
    return rasa_api_continue(now_action, events=[])


def action_utter_detail(data_payload):
    herb_name = data_payload.get('userChatHerbName')
    herb_object = get_herb_object_from_herb_name(herb_name)
    brief_info = herb_object['briefInformation']
    # detail_header_text = "ข้อมูลทั่วไปของ" + herb_name + "ได้แก่" + '\n'
    # if len(herb_object['propertyList']) > 1:
    #     details = random.sample(herb_object['propertyList'], 2)
    #     detail_header_text = detail_header_text + \
    #                          '• ' + details[0] + '\n' + \
    #                          '• ' + details[1]
    messenger_send_api.respond(data_payload['user']['id'], brief_info)


def action_utter_benefit_not_found(data_payload):
    benefit_not_found_text = random_info_not_found_text(data_payload['user']['name'],
                                                        data_payload.get('userChatHerbName'), info='สรรพคุณ')
    messenger_send_api.respond(data_payload['user']['id'], benefit_not_found_text)


def action_utter_benefit(data_payload):
    herb_name = data_payload.get('userChatHerbName')
    herb_object = get_herb_object_from_herb_name(herb_name)
    benefit_header_text = "สรรพคุณของ" + herb_name + "ได้แก่" + '\n'
    benefits = random.sample(herb_object['benefitList'], 2)
    if len(herb_object) > 1:
        benefit_header_text = benefit_header_text + \
                              '• ' + benefits[0] + '\n' + \
                              '• ' + benefits[1]
    messenger_send_api.respond(data_payload['user']['id'], benefit_header_text)


def action_utter_herb_name_not_found(data_payload):
    not_found_herb_name_text = random_not_found_herb_name_text(data_payload['user']['name'])
    messenger_send_api.respond(data_payload['user']['id'], not_found_herb_name_text)


def action_utter_thankyou(data_payload):
    messenger_send_api.respond(data_payload['user']['id'],
                               "ขอบคุณครับ ถ้ามีอะไรให้" + BOT_NAME + "ช่วยอีกก็บอกได้เลยนะครับ")


def action_utter_herb_name(now_action, data_payload):
    found_herb_name_text = random_found_herb_name_text(data_payload['user']['name'], get_value_from_slot(now_action, 'herb'))
    messenger_send_api.respond(data_payload['user']['id'], found_herb_name_text)
    return rasa_api_continue(now_action, events=[])


def action_utter_herb_photo(now_action, data_payload):
    herb_name = get_value_from_slot(now_action, 'herb')
    herb_object = get_herb_object_from_herb_name(herb_name)
    image_path = get_image_path_from_herb(herb_object)
    image_found_text = random_image_found_text(data_payload['user']['name'], data_payload.get('userChatHerbName'))
    messenger_send_api.respond(data_payload['user']['id'], image_found_text)
    messenger_send_api.send_image(data_payload['user']['id'], image_path)
    file_path_for_label = image_path.split(os.sep)[:-2]
    file_path_for_label = os.sep.join(file_path_for_label)
    return rasa_api_continue(now_action, events=get_event_slot(file_path=file_path_for_label))


def action_action_name_to_detail(now_action, data_payload):
    info = 'ข้อมูลทั่วไป'
    name_to_info_text = random_name_to_info_text(data_payload['user']['name'], data_payload.get('userChatHerbName'),
                                                 info=info)
    messenger_send_api.respond(data_payload['user']['id'], name_to_info_text)
    herb_object = get_herb_object_from_herb_name(data_payload.get('userChatHerbName'))
    next_action = None
    if not herb_object == HERB_NOT_FOUND:
        brief_info = herb_object.get('briefInformation')
        if brief_info:
            next_action = rasa_api_continue(now_action, events=get_event_slot(herb_name=data_payload.get('userChatHerbName')))
            next_action = rasa_api_start(data_payload['user']['id'], "พบสมุนไพร")
        else:
            next_action = rasa_api_continue(now_action, events=[])
            next_action = rasa_api_start(data_payload['user']['id'], "ไม่พบสมุนไพร")
    return next_action


def action_action_name_to_benefit(now_action, data_payload):
    info = 'สรรพคุณ'
    name_to_info_text = random_name_to_info_text(data_payload['user']['name'], data_payload.get('userChatHerbName'),
                                                 info=info)
    messenger_send_api.respond(data_payload['user']['id'], name_to_info_text)
    herb_object = get_herb_object_from_herb_name(data_payload.get('userChatHerbName'))
    next_action = None
    if herb_object == HERB_NOT_FOUND:
        next_action = rasa_api_continue(now_action, events=[])
        next_action = rasa_api_start(data_payload['user']['id'], "ไม่พบสมุนไพร")
    else:
        next_action = rasa_api_continue(now_action, events=get_event_slot(herb_name=data_payload.get('userChatHerbName')))
        next_action = rasa_api_start(data_payload['user']['id'], "พบสมุนไพร")
    return next_action


def action_action_photo_name(now_action, data_payload):
    searching_herb_name_text = random_searching_herb_name_text(data_payload['user']['name'])
    messenger_send_api.respond(data_payload['user']['id'], searching_herb_name_text)
    predicted_herb_name = call_herb_classification(data_payload.get('userChatImageUrl'))
    next_action = None
    if predicted_herb_name:
        next_action = rasa_api_continue(now_action, events=get_event_slot(herb_name=predicted_herb_name))
        next_action = rasa_api_start(data_payload['user']['id'], "พบสมุนไพร")
    else:
        next_action = rasa_api_continue(now_action, events=[])
        next_action = rasa_api_start(data_payload['user']['id'], "ไม่พบสมุนไพร")
    return next_action


def action_action_name_to_photo(now_action, data_payload):
    herb_in_slot = get_value_from_slot(now_action, 'herb')
    herb_object = get_herb_object_from_herb_name(herb_in_slot)
    image_path = get_image_path_from_herb(herb_object)
    # image_path = get_image_path_from_herb(get_herb_info_from_database(data_payload['suggestedHerbName']))
    next_action = None
    if image_path == IMAGE_NOT_FOUND:
        next_action = rasa_api_continue(now_action, events=[])
        next_action = rasa_api_start(data_payload['user']['id'], "ไม่พบสมุนไพร")
    else:
        searching_image_text = random_searching_image_text(data_payload['user']['name'],
                                                           data_payload.get('userChatHerbName'))
        messenger_send_api.respond(data_payload['user']['id'], searching_image_text)
        next_action = rasa_api_continue(now_action, events=get_event_slot(herb_name=data_payload.get('userChatHerbName')))
        next_action = rasa_api_start(data_payload['user']['id'], "พบสมุนไพร")
    return next_action


def action_action_validate_herb(now_action, data_payload):
    herb_name = data_payload['userChatHerbName']
    herb_object = get_herb_object_from_herb_name(herb_name)
    if herb_object == HERB_NOT_FOUND:
        next_action = rasa_api_continue(now_action, events=[])
        next_action = rasa_api_start(data_payload['user']['id'], "ไม่พบสมุนไพร")
    else:
        next_action = rasa_api_continue(now_action, events=get_event_slot(herb_name=herb_name))
        next_action = rasa_api_start(data_payload['user']['id'], "พบสมุนไพร")
    return next_action


def action_ask_validate_herb(now_action, data_payload):
    idx_ex = find_most_similar_herb_index_from_expanded_list(data_payload.get('userChatHerbName'))
    suggested_herb_name = expanded_herb_json_array[idx_ex]['thaiName']
    suggest_herb_name_text = "พี่หมายถึง" + suggested_herb_name + "หรือเปล่าครับ"
    quick_replies = [create_reply('ใช่'), create_reply('ไม่ใช่')]
    messenger_send_api.send_quick_replies(data_payload['user']['id'], suggest_herb_name_text, quick_replies)
    return rasa_api_continue(now_action, events=get_event_slot(herb_name=suggested_herb_name))


def action_ask_name_to_detail_herb_name(data_payload):
    info = 'ข้อมูลทั่วไป'
    ask_name_to_info_herb_name_text = random_ask_name_to_info_herb_name_text(data_payload['user']['name'], info=info)
    messenger_send_api.respond(data_payload['user']['id'], ask_name_to_info_herb_name_text)


def action_ask_name_to_benefit_herb_name(data_payload):
    info = 'สรรพคุณ'
    ask_name_to_info_herb_name_text = random_ask_name_to_info_herb_name_text(data_payload['user']['name'], info=info)
    messenger_send_api.respond(data_payload['user']['id'], ask_name_to_info_herb_name_text)


def action_bot_ask_get_data(data_payload):
    messenger_send_api.respond(data_payload['user']['id'],
                               "ช่วยบอกน้อง" + BOT_NAME + "หน่อยได้ไหมครับ ว่าจริง ๆ แล้วมันสมุนไพรอะไร (เช่น \"มันคือมะนาว\")")


def action_bot_ask_name_to_photo_herb_name(now_action, data_payload):
    ask_name_to_photo_herb_name_text = random_ask_name_to_photo_herb_name_text(data_payload['user']['name'])
    messenger_send_api.respond(data_payload['user']['id'], ask_name_to_photo_herb_name_text)
    return rasa_api_continue(now_action, events=[])


def action_bot_ask_photo(now_action, data_payload):
    ask_photo_text = random_ask_photo_text(data_payload['user']['name'])
    messenger_send_api.respond(data_payload['user']['id'], ask_photo_text)
    return rasa_api_continue(now_action, events=[])


def action_bot_utter_greeting(now_action, data_payload):
    greeting_text = random_greeting_text(data_payload['user']['name'])
    messenger_send_api.respond(data_payload['user']['id'], greeting_text)
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
                    'payload': "ดูข้อมูลทั่วไปของสมุนไพร"
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
    messenger_send_api.send_generic_template(data_payload['user']['id'], carousel_elements)
    return rasa_api_continue(now_action, events=[])


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
        predicted_herb_id_string = response_json['results'][0]['label']
        predicted_herb_id = int(predicted_herb_id_string)
        # map_herb_name = {
        #     'kokchang': 'กกช้าง',
        #     'kokrungka': 'กกลังกา',
        #     'krajeabdang': 'กระเจี๊ยบแดง',
        #     'kwawkruekaw': 'กวาวเครือขาว',
        #     'kangfang': 'แก่นฝาง',
        #     'kaminchun': 'ขมิ้นชัน',
        #     'chakeaw': 'ชาเขียว',
        #     'tungchao': 'ถั่งเช่า',
        #     'borapet': 'บอระเพ็ด',
        #     'plalhaipruek': 'ปลาไหลเผือก',
        #     'fang': 'ฝาง',
        #     'plukaow': 'พลูคาว',
        #     'yahnang': 'ย่านาง',
        #     'rangjued': 'รางจืด',
        #     'looktaibai': 'ลูกใต้ใบ',
        #     'wanhang': 'ว่านหางจระเข้',
        #     'somkorea': 'โสมเกาหลี',
        #     'obchei': 'อบเชย'
        # }
        # predicted_herb_name = map_herb_name[predicted_herb_tmp_name]
        predicted_herb_object = get_herb_object_from_herb_id(predicted_herb_id)
        predicted_herb_name = predicted_herb_object['thaiNameList'][0]
        return predicted_herb_name
    except requests.exceptions.RequestException as e:
        logger.error(e)
        # messenger_send_api.respond(recipient_id, "ขออภัยครับ ตอนนี้" + BOT_NAME + "คิดไม่ออกว่ารูปนี้คือสมุนไพรรูปอะไร ไว้ลองใหม่นะครับ")
    return None


def request_rasa_server(endpoint, recipient_id, body):
    api_url = RASA_SERVER_API_URI + "/conversations/" + recipient_id + "/" + endpoint
    try:
        response = requests.post(api_url,
                                 json=body
        )
        res = response.content
        next_action_json = json.loads(res)
        return next_action_json
    except requests.exceptions.RequestException as e:
        logger.error(e)
        return None


def rasa_api_start(recipient_id, text):
    body = {'query': text}
    next_action = request_rasa_server(endpoint='parse', recipient_id=recipient_id, body=body)
    return next_action


def rasa_api_continue(next_action, events=[]):
    body = {
        'executed_action': next_action['next_action'],
        'events': events
    }
    recipient_id = next_action['tracker']['sender_id']
    next_action = request_rasa_server(endpoint='continue', recipient_id=recipient_id, body=body)
    return next_action


def get_event_slot(herb_name=None, feature_list=None, file_path=None):
    # evts = events.deserialise_events([{"event": "slot", "name": "herb", "value": herb_name}])
    evts = []
    if herb_name:
        evts.append({"event": "slot", "name": "herb", "value": herb_name})
    if feature_list:
        evts.append({"event": "slot", "name": "featureList", "value": feature_list})
    if file_path:
        evts.append({"event": "slot", "name": "filePath", "value": file_path})
    return evts



def get_event_slot_reset():
    # evts = events.deserialise_events([{"event": "reset_slots"}])
    evts = [{"event": "reset_slots"}]
    return evts


# def nlu_start(recipient_id, text):
    # # rasa nlu
    # rasa_nlu_interpreter_path = os.path.join(os.getcwd(), "rasa", "models", "nlu", "default", "current")
    # interpreter = RasaNLUInterpreter(rasa_nlu_interpreter_path)
    # rasa_nlu_dialogue_path = os.path.join(os.getcwd(), "rasa", "models", "dialogue")
    # agent = Agent.load(rasa_nlu_dialogue_path, interpreter=interpreter)
    # next_action = agent.start_message_handling(text, sender_id=recipient_id)
    # return next_action


def get_random_message():
    sample_responses = ["อู้หยังนิ", "บ่ฮู้เรื่อง", "อู้ไปเรื่อย", "สวัสดีเจ้า", "ต่อนยอน"]
    return random.choice(sample_responses)


def get_value_from_slot(now_action, value):
    return now_action.get('tracker').get('slots').get(value)


def get_herb_object_from_herb_name(herb_name):
    matched_herb_list = [x for x in herb_json_array if herb_name in set(x['thaiNameList'])]
    if len(matched_herb_list) == 0:
        return HERB_NOT_FOUND
    return matched_herb_list[0]


def get_herb_object_from_herb_id(herb_id):
    matched_herb_list = [x for x in herb_json_array if herb_id == x['herbId']]
    if len(matched_herb_list) == 0:
        return HERB_NOT_FOUND
    return matched_herb_list[0]


def find_most_similar_herb_index_from_expanded_list(herb_name):
    similarity_list = []
    for herb_json in expanded_herb_json_array:
        similarity_list.append(fuzz.ratio(herb_name, herb_json['thaiName']))
    similarity_array = asarray(similarity_list)
    argsort_similarity_list = similarity_array.argsort()[-1:]
    return argsort_similarity_list[0]


def find_most_similar_feature(text):
    similarity_list = []
    for feature in herb_feature_json_array:
        similarity_list.append(fuzz.ratio(text, feature))
    similarity_array = asarray(similarity_list)
    argsort_similarity_list = similarity_array.argsort()[-1:]
    return herb_feature_json_array[argsort_similarity_list[0]]


def get_image_path_from_herb(matched_herb):
    if not matched_herb:
        return IMAGE_NOT_FOUND
    image_directory_path = os.path.join('herb_data', 'herb_images_png', str(matched_herb['herbId']))
    # logger.debug("(" + str(matched_herb['herbId']) + ") " + ','.join(matched_herb['thaiNameList']))
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
        "พี่ครับ " + BOT_NAME + "ยังไม่มีรูปของ" + herb_name + "แฮะครับ",
        "พี่ " + user_name + " จ๋า ขออภัยนะ น้องหารูป" + herb_name + "ไม่ได้ครับ",
        BOT_NAME + "หารูป" + herb_name + "ไม่เจอ ขอโทษด้วยนะครับ",
        "ขออภัยครับ ตอนนี้" + BOT_NAME + "ยังไม่มีรูป" + herb_name + "ครับ"
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


def random_validation_herb_photo_text(user_name, herb_name):
    image_validation_herb_photo_text_list = [
        "พี่ช่วยบอก" + BOT_NAME + "หน่อยได้มั้ยครับว่ารูปนี้ใช่รูปของ" + herb_name + "มั้ยครับ",
        "พี่ " + user_name + " ช่วยบอก" + BOT_NAME + "หน่อยได้มั้ยครับว่ารูปนี้ใช่รูปของ" + herb_name + "มั้ยครับ",
        "รูปนี้ใช่" + herb_name + "มั้ยครับ ช่วย" + BOT_NAME + "ยืนยันหน่อยน้า"
    ]
    return random.SystemRandom().choice(image_validation_herb_photo_text_list)


def random_validation_herb_name_text(user_name, herb_name):
    image_validation_herb_name_text_list = [
        "พี่ช่วยบอก" + BOT_NAME + "หน่อยได้มั้ยครับ สมุนไพรในรูปนี้ใช่ " + herb_name + " มั้ยครับ",
        "พี่ " + user_name + " ช่วยบอก" + BOT_NAME + "หน่อยได้มั้ยครับว่านี่คือ " + herb_name + " มั้ยครับ",
        "สมุนไพรนี้คือ " + herb_name + " หรือเปล่าครับ ช่วย" + BOT_NAME + "ยืนยันหน่อยน้า"
    ]
    return random.SystemRandom().choice(image_validation_herb_name_text_list)


def random_thx_label_text(user_name):
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
        "พี่ " + user_name + " ช่วยยืนยันได้ไหมครับว่ารูปที่ส่งมาคือ" + herb_name + "หรือเปล่า"
    ]
    return random.SystemRandom().choice(validate_herb_name_text_list)


def random_ask_photo_text(user_name):
    ask_photo_text_list = [
        "พี่ " + user_name + " รบกวนช่วยส่งรูปของสมุนไพรให้น้อง" + BOT_NAME + "หน่อยครับ",
        BOT_NAME + "ต้องให้พี่ " + user_name + " ส่งรูปสมุนไพรให้หน่อยครับ"
    ]
    return random.SystemRandom().choice(ask_photo_text_list)


def random_ask_name_to_photo_herb_name_text(user_name):
    ask_name_to_photo_herb_name_text_list = [
        "พี่ " + user_name + " รบกวนช่วยบอกชื่อสมุนไพรให้น้อง" + BOT_NAME + "หน่อยครับ",
        BOT_NAME + "ต้องให้พี่ " + user_name + " บอกชื่อสมุนไพรที่อยากดูรูปครับ",
        "ช่วยบอกน้อง" + BOT_NAME + "หน่อยครับว่าอยากดูรูปของสมุนไพรชื่ออะไร"
    ]
    return random.SystemRandom().choice(ask_name_to_photo_herb_name_text_list)


def random_name_to_info_text(user_name, herb_name, info):
    random_name_to_info_text_list = [
        "รอสักครู่ครับ เดี๋ยว" + BOT_NAME + "ช่วยค้น" + info + "ของ" + herb_name + "ให้ครับ",
        "รอแป๊บนึงนะครับพี่ " + user_name + " เดี่ยว" + BOT_NAME + "หา" + info + "ของ" + herb_name + "ให้นะครับ"
    ]
    return random.SystemRandom().choice(random_name_to_info_text_list)


def random_ask_name_to_info_herb_name_text(user_name, info):
    ask_name_to_info_herb_name_text_list = [
        "พี่ " + user_name + " รบกวนช่วยบอกชื่อสมุนไพรให้น้อง" + BOT_NAME + "หน่อยครับ",
        BOT_NAME + "ต้องให้พี่ " + user_name + " บอกชื่อสมุนไพรที่อยากรู้" + info + "ให้หน่อยครับ",
        "ช่วยบอกน้อง" + BOT_NAME + "หน่อยครับว่าอยากดู" + info + "ของสมุนไพรชื่ออะไร"
    ]
    return random.SystemRandom().choice(ask_name_to_info_herb_name_text_list)


def random_info_not_found_text(user_name, herb_name, info):
    info_not_found_text_list = [
        "พี่ " + user_name + " ขออภัยนะครับ น้อง" + BOT_NAME + "หา" + info + "ของ" + herb_name + "ไม่เจอครับ",
        BOT_NAME + "หา" + info + "ของ" + herb_name + "ไม่เจอ ขอโทษพี่ " + user_name + " ด้วยนะครับ",
        "น้อง" + BOT_NAME + "เสียใจ หา" + info + "ของ" + herb_name + "ให้พี่" + user_name + " ไม่เจอครับ"
    ]
    return random.SystemRandom().choice(info_not_found_text_list)


def random_ask_feature_to_herb_text(user_name):
    ask_feature_to_herb_text_list = [
        "พี่ " + user_name + " รบกวนช่วยบอกสรรพคุณที่ต้องการให้น้อง" + BOT_NAME + "หน่อยครับ",
        BOT_NAME + "ต้องให้พี่ " + user_name + " บอกสรรพคุณที่สนใจให้หน่อยครับ",
        "ช่วยบอกน้อง" + BOT_NAME + "หน่อยครับว่าอยากรู้สมุนไพรที่มีสรรพคุณอะไรครับ"
    ]
    return random.SystemRandom().choice(ask_feature_to_herb_text_list)


def random_finding_feature_to_herb_text(user_name, feature_list):
    feature = ', '.join(feature_list)
    finding_feature_to_herb_text_list = [
        "เดี๋ยว" + BOT_NAME + "ขอเวลาค้นดูว่ามีสมุนไพรตัวไหนที่ช่วยเรื่อง" + feature + "สักครู่นะครับ",
        "รอสักครู่คร้าบ " + BOT_NAME + "กำลังหาสมุนไพรที่มีสรรพคุณ" + feature + "ให้ครับ",
        "พี่ " + user_name + " รอแป๊บนึงนะ " + BOT_NAME + "กำลังหาสมุนไพรเกี่ยวกับ" + feature + "อยู่ครับผม"
    ]
    return random.SystemRandom().choice(finding_feature_to_herb_text_list)


def random_herb_feature_not_found_text(user_name, feature_list):
    feature = ', '.join(feature_list)
    herb_feature_not_found_text_list = [
        "นี่ ๆ " + BOT_NAME + "หาสมุนไพรเกี่ยวกับ" + feature + "ไม่เจอแฮะครับ",
        "พี่ " + user_name + " จ๋า ขออภัยนะ น้องหาสมุนไพรที่มีสรรพคุณ" + feature + "ไม่เจอครับ",
        BOT_NAME + "หาสมุนไพรที่มีสรรพคุณเกี่ยวกับ" + feature + "ไม่เจอ ขอโทษด้วยนะครับ",
        "ขออภัยครับ ตอนนี้" + BOT_NAME + "ยังไม่มีสมุนไพรที่มีสรรพคุณ" + feature + "ครับ"
    ]
    return random.SystemRandom().choice(herb_feature_not_found_text_list)


def random_ask_more_text(user_name):
    ask_more_text_list = [
        "พี่ " + user_name + " อยากรู้อะไรเพิ่มเติมไหมครับ",
        "พี่ " + user_name + " อยากให้" + BOT_NAME + "ช่วยอะไรเพิ่มเติมไหมครับ"
    ]
    return random.SystemRandom().choice(ask_more_text_list)


def create_reply(text):
    return {
        'content_type': 'text',
        'title': text,
        "payload": text
    }


def get_feature_list_from_entities(entities):
    feature_list = []
    for entity in entities:
        if entity['entity'] == 'feature':
            feature_list.append(entity['value'])
    return feature_list
