from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.agent import Agent
import os

interpreter = RasaNLUInterpreter(os.path.join(os.getcwd(), "models", "nlu", "default", "current"))
agent = Agent.load(os.path.join(os.getcwd(), "models", "dialogue"), interpreter=interpreter)


def run():
    # while(True):
    user_message = "ต้องการดูรูปขมิ้นชัน"
    print(user_message)
    next_action = agent.start_message_handling(user_message) #Get Next action from input user message
    print(next_action)
    while(next_action['next_action']!="action_listen"):
        now_action = next_action['next_action']
        next_action = agent.continue_message_handling(executed_action=next_action['next_action'],sender_id=next_action['tracker']['sender_id'],events=[])
        next_action = run_action(now_action,next_action)
        print(next_action)
def run_action(input_action,next_action):
    if input_action == 'bot.action.name_to_photo':
        status = name_to_photo()
        print(status)
        next_action = agent.start_message_handling(status)
        return next_action
    else:
        return next_action

def name_to_photo():
    if True:
        return "พบสมุนไพร"
    else:
        return "ไม่พบสมุนไพร"
if __name__ == '__main__':
    run()