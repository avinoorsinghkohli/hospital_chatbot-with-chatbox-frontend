# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionPatientRecord(Action):
	def name(self) -> Text:
		return "action_patient_record"
	def run(self,dispatcher: CollectingDispatcher, tracker:Tracker,domain: Dict[Text,Any]) -> List[Dict[Text,Any]]:
		entities=tracker.latest_message['entities']
		for e in entities:
			if e['entity']=='number':
				num=e['value']
			if num=="1":
				mess="1) Name: Avinoor Singh Kohli\n2) Age: 18\n3) Gender: Male\n4) Diseases: Chicken Pox"
			elif num=="2":
				mess="1) Name: Navneet\n2) Age: 28\n3) Gender: Female\n4) Diseases: Cancer"
			elif num=="3":
				mess="1) Name: Harvinder\n2) Age: 38\n3) Gender: Male\n4) Diseases: Covid 19"

			else:
				mess="Sorry, The patient with this number does not exist...."
		# if(len(mess)==0):

		# 	dispatcher.utter_message(text="Sorry, The patient with this number does not exist....")
		# else:
		dispatcher.utter_message(text=mess)


		return []



