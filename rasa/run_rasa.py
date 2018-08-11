from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.agent import Agent
from rasa_core import events
import os

interpreter = RasaNLUInterpreter(os.path.join(os.getcwd(), "models", "nlu", "default", "current"))
agent = Agent.load(os.path.join(os.getcwd(), "models", "dialogue"), interpreter=interpreter)


def run():
    while(True):
        user_message = input()
        next_action = agent.start_message_handling(user_message) #Get Next action from input user message
        print(next_action)
        while(next_action['next_action']!="action_listen"):
            next_action = run_action(next_action)
            print(next_action)
def run_action(input_action):
    next_action = input_action
    if next_action['next_action'] == 'bot.action.name_to_photo':
        status = name_to_photo()
        next_action = agent.continue_message_handling(executed_action=next_action['next_action'],sender_id=next_action['tracker']['sender_id'], events=[])
        next_action = agent.start_message_handling(status)
        return next_action
    elif(next_action['next_action'] == 'action_slot_reset'):
        evts = events.deserialise_events([{"event":"reset_slots"}])
        next_action = agent.continue_message_handling(executed_action=next_action['next_action'],sender_id=next_action['tracker']['sender_id'],events=evts)
        return next_action
    elif(next_action['next_action']=="bot.utter.herb_name"):
        herb_name = "มะนาว"
        evts = events.deserialise_events([{"event": "slot", "name": "herb", "value": herb_name}])
        next_action = agent.continue_message_handling(executed_action=next_action['next_action'],
                                                      sender_id=next_action['tracker']['sender_id'], events=evts)
        return next_action

    else:
        next_action = agent.continue_message_handling(executed_action=next_action['next_action'],sender_id=next_action['tracker']['sender_id'], events=[])
        return next_action

def name_to_photo():
    if True:
        return "พบสมุนไพร"
    else:
        return "ไม่พบสมุนไพร"
if __name__ == '__main__':
    run()