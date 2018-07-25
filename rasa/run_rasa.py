from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.agent import Agent
import os

interpreter = RasaNLUInterpreter(os.path.join(os.getcwd(), "models", "nlu", "default", "current"))
agent = Agent.load(os.path.join(os.getcwd(), "models", "dialogue"), interpreter=interpreter)


def run():
    # while(True):
    user_message = "ขอดูรูปขมิ้นชันหน่อย"
    next_action = agent.start_message_handling(user_message) #Get Next action from input user message
    print(next_action)
    if next_action['next_action'] == 'bot.action.name_to_photo':
        print(next_action['tracker']['slots']['herb'])
    while(next_action['next_action']!="action_listen"):
        next_action = agent.continue_message_handling(executed_action=next_action['next_action'],sender_id=next_action['tracker']['sender_id'],events=[])
        print(next_action)

if __name__ == '__main__':
    run()