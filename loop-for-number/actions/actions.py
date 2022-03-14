import numbers
from typing import Text, List, Any, Dict

from rasa_sdk import Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

name_list= []
class ValidateNameForm(FormValidationAction):
    
    def name(self) -> Text:
        return "validate_full_name_form"
    

    def validate_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `full_name` value."""
        
        print(f"Name given = {slot_value}")
        number = 4 
        if number >0 :
            for i in range(number):
                dispatcher.utter_message(text=f":")
                return {"Name": None}
        else:
            return {"Name": slot_value}


