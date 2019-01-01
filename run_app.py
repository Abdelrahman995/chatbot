from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput


nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/weathernlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-447688795587-447097410720-515405873591-5139924591ae1c4b1b8d18618c8b8209', #app verification token
							'xoxb-447688795587-513616440176-9ttYHr2hHAV9NVxdJHn5Nv68', # bot verification token
							'zFPeg8jCo3BTeMmT5I5RIhYB', # slack verification token
							True)

agent.handle_channel(HttpInputChannel(5006, '/', input_channel))
