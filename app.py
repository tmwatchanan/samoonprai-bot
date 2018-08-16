#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Flask server
from flask import Flask, request
# Messenger Platform
from messenger_send_api import verify_webhook
# Samoonprai Bot
import controllers
# Utilities
import logging
import os.path
# Background Tasks
from celery import Celery
import redis

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
app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379/0',
    CELERY_RESULT_BACKEND='redis://localhost:6379/0',
)
r = redis.StrictRedis(host='localhost', port=6379, db=0)

def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL']
    )
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery

celery = make_celery(app)

# @app.route('/')
# def index():
#     return '<h1>Samoonprai</h1>'


@app.route("/webhook", methods=['GET', 'POST'])
def listen():
    """This is the main function flask uses to
    listen at the `/webhook` endpoint"""
    if request.method == 'GET':
        return verify_webhook(request)

    if request.method == 'POST':
        payload = request.get_json()
        if not payload.get('object') == 'page':
            return
        process.apply_async(args=[payload])
        # process(payload)
        # result = add_together.apply_async((5, 3))
        # print(result)
        return "ok", 200
        # return "no", 403


@celery.task(name='process')
def process(payload):
    with app.app_context():
        controllers.process_incoming_message(payload)


# @app.route('/bot')
# def bot():
#     message = request.args.get('message')
#     return message  # Echo message
#     # return jsonify(interpreter.parse(message))


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, threaded=True, debug=True)
