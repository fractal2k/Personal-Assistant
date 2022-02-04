# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from rasa_sdk.events import SlotSet

# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class ActionCreateProductivityUnit(Action):

    def name(self) -> Text:
        return "action_create_productivity_unit"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        type = tracker.get_slot('productivity_unit_type')
        requirements = {}
        if type == 'timer':
            requirements['timer_duration'] = tracker.get_slot('timer_duration')
        elif type in ['reminder', 'remind']:
            requirements['reminder_name'] = tracker.get_slot('reminder_name')
            requirements['reminder_datetime'] = tracker.get_slot('reminder_datetime')

        dispatcher.utter_message(f'Successfully created a {type} with requirements: {requirements}')
        
        events = [SlotSet(key, None) for key in requirements.keys()]
        events.append(SlotSet('productivity_unit_type', None))
        return events