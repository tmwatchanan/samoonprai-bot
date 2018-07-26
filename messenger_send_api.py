import os
import requests
from requests_toolbelt import MultipartEncoder
import json
import logging

GRAPH_API_URL = 'https://graph.facebook.com'
SEND_API_URL = 'https://graph.facebook.com/v2.6/me/messages'
VERIFY_TOKEN = os.environ['VERIFY_TOKEN']
PAGE_ACCESS_TOKEN = os.environ['PAGE_ACCESS_TOKEN']

# Logging
logger = logging.getLogger('app')

auth = {
    'access_token': PAGE_ACCESS_TOKEN
}


def verify_webhook(req):
    if req.args.get("hub.verify_token") == VERIFY_TOKEN:
        return req.args.get("hub.challenge")
    else:
        return "Invalid Webhook Subscription's Verify Token"


def is_user_message(message):
    """Check if the message is a message from the user"""
    return (message.get('message') and
            message['message'].get('text') and
            not message['message'].get("is_echo"))


def get_user_info(recipient_id, fields=None):
    # https://developers.facebook.com/docs/messenger-platform/user-profile
    params = {}
    if fields is not None and isinstance(fields, (list, tuple)):
        params['fields'] = ",".join(fields)
    params.update(auth)
    request_endpoint = '{0}/{1}'.format(GRAPH_API_URL, recipient_id)
    response = requests.get(request_endpoint, params=params)
    if response.status_code == 200:
        return response.json()
    return None


def get_bot_response(message):
    return "ลูกสมุนไพร่: '{}'".format(message)


def respond(recipient_id, message):
    send_text(recipient_id, message)


def debug_respond(recipient_id, message):
    response = get_bot_response(message)
    send_text(recipient_id, response)


def send_response(recipient_id, notification_type='regular', add_payload=None):
    payload = {
        'recipient': {
            'id': recipient_id
        },
        'notification_type': notification_type
    }
    if payload is not None:
        payload['message'] = add_payload

    response = requests.post(
        SEND_API_URL,
        params=auth,
        json=payload,
    )

    return response.json()


def send_text(recipient_id, text):
    """Send a response to Facebook"""
    message = {
        'text': text
    }
    return send_response(recipient_id, add_payload=message)


def send_image(recipient_id, image_path):
    """Send a response to Facebook"""
    # print("image_path = " + image_path)
    payload = {
        'message': '{ "attachment": { "type": "image", "payload": {} } }',
        'filedata': (os.path.basename(image_path), open(image_path, 'rb'), 'image/png'),
        'recipient': '{ "id": ' + recipient_id + ' }',
        'notification_type': 'regular'
    }

    multipart_data = MultipartEncoder(payload)
    multipart_header = {
        'Content-Type': multipart_data.content_type
    }

    logger.debug("Send image %s to recipient id %s", recipient_id, image_path)

    return requests.post(SEND_API_URL, data=multipart_data,
                         params=auth, headers=multipart_header).json()


def send_button(recipient_id, text, buttons):
    # https://developers.facebook.com/docs/messenger-platform/send-api-reference/button-template
    attachment = {
        'attachment' : {
            'type': 'template',
            'payload': {
                'template_type': 'button',
                'text': text,
                "buttons": buttons
            }
        }
    }
    return send_response(recipient_id, add_payload=attachment)
