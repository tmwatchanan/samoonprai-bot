from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import argparse
import logging
import warnings

from rasa_core.policies.fallback import FallbackPolicy
from policy import RestaurantPolicy
from rasa_core import utils
from rasa_core.actions import Action
from rasa_core.agent import Agent
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.events import SlotSet
from rasa_core.featurizers import (MaxHistoryTrackerFeaturizer,BinarySingleStateFeaturizer)
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.policies.keras_policy import KerasPolicy

logger = logging.getLogger(__name__)


class RestaurantAPI(object):
    def search(self, info):
        return "papi's pizza place"


class ActionSearchRestaurants(Action):
    def name(self):
        return 'action_search_restaurants'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("looking for restaurants")
        restaurant_api = RestaurantAPI()
        restaurants = restaurant_api.search(tracker.get_slot("cuisine"))
        return [SlotSet("matches", restaurants)]


class ActionSuggest(Action):
    def name(self):
        return 'action_suggest'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("here's what I found:")
        dispatcher.utter_message(tracker.get_slot("matches"))
        dispatcher.utter_message("is it ok for you? "
                                 "hint: I'm not going to "
                                 "find anything else :)")
        return []


def train_dialogue(domain_file="domain.yml",
                   model_path="models/dialogue",
                   training_data_file="data/stories.md"):
    fallback = FallbackPolicy(fallback_action_name="bot.utter.default",
                              core_threshold=0.3,
                              nlu_threshold=0.3)
    agent = Agent(domain_file,
                  policies=[MemoizationPolicy(max_history=3),KerasPolicy(),fallback])

    training_data = agent.load_data(training_data_file)
    agent.train(
            training_data,
            epochs=400,
            batch_size=100,
            validation_split=0.2
    )

    agent.persist(model_path)
    return agent


def train_nlu():
    from rasa_nlu.training_data import load_data
    from rasa_nlu import config
    from rasa_nlu.model import Trainer
    from rasa_nlu.convert import convert_training_data
    import convert

    convert.read_excel()
    convert_training_data('data/nlu.md', 'nludata/train_data_md.json', 'json', 'ay')
    training_data = load_data('nludata/')
    trainer = Trainer(config.load("nlu_model_config.yml"))
    trainer.train(training_data)
    model_directory = trainer.persist('models/nlu/', fixed_model_name="current")


    return model_directory


def run(serve_forever=True):
    interpreter = RasaNLUInterpreter("models/nlu/default/current")
    agent = Agent.load("models/dialogue", interpreter=interpreter)

    if serve_forever:
        agent.handle_channel(ConsoleInputChannel())
    return agent
def run_nlu(serve_forever=True):
    interpreter = RasaNLUInterpreter("models/nlu/default/current")

    while(True):
            text = input("Input text: ")
            print(interpreter.parse(text))

if __name__ == '__main__':
    utils.configure_colored_logging(loglevel="INFO")

    parser = argparse.ArgumentParser(
            description='starts the bot')

    parser.add_argument(
            'task',
            choices=["train-nlu", "train-dialogue", "run_core","run_nlu"],
            help="what the bot should do - e.g. run or train?")
    task = parser.parse_args().task

    # decide what to do based on first parameter of the script
    if task == "train-nlu":
        train_nlu()
    elif task == "train-dialogue":
        train_dialogue()
    elif task == "run_nlu":
        run_nlu()
    elif task == "run_core":
        run()