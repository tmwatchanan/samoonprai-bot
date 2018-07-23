from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.agent import Agent

def run():
    interpreter = RasaNLUInterpreter("models/nlu/default/current")
    agent = Agent.load("models/dialogue", interpreter=interpreter)

    while(True):
        user_message = input()
        next_action = agent.start_message_handling(user_message) #Get Next action from input user message
        print(next_action)
        while(next_action['next_action']!="action_listen"):
            next_action = agent.continue_message_handling(executed_action=next_action['next_action'],sender_id=next_action['tracker']['sender_id'],events=[])
            print(next_action)

if __name__ == '__main__':
    run()