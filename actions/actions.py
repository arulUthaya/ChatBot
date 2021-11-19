# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#
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

class ActionOrderNumber(Action):

    def name(self) -> Text:
        return "action_order_number"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         dispatcher.utter_message(text="மிகவும் நன்றி. சற்று நேரம் காத்திருங்கள்...")

         return []

class ActionDefault(Action):

    def name(self) -> Text:
        return "action_default"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         dispatcher.utter_message(text="மன்னிக்கவும். உங்கள் கோரிக்கையை என்னால் நிறைவேற்றமுடியவில்லை, மீண்டும் முயற்சியுங்கள்.")

         return []


class ActionRefund(Action):
    """an action which acts when user wants a refund"""

    def name(self) -> Text:
        return "action_refund"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # keep it simple
        orderno = tracker.get_slot("orderno")

        if orderno is None :
            dispatcher.utter_message(text="நீங்கள் பதிவு செய்த order number பிழையாக உள்ளது. மீண்டும் முயற்சியுங்கள்.")
        else:
           
            dispatcher.utter_message(text= "உங்களுடைய பொதி எங்களிடம் கையளிக்கப்பட்டுவிட்டது. உங்களுக்கான refund செயற்பாடுகள் நடைப்பெறுகின்றது. இன்னும் 48 மணி நேரத்தில் உங்கள் பணத்தை நீங்கள் பெற்று விடுவீர்கள். தொடர்பிற்கு நன்றி")
                  
        return []
