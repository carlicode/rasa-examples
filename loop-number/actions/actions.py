from typing import Text, List, Any, Dict

from rasa_sdk import Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

list_aux = []
class ValidateNameForm(FormValidationAction):
    
    def name(self) -> Text:
        return "validate_full_name_form"
    
    def validate_full_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `full_name` value."""
        if slot_value[0].isnumeric(): value = slot_value[2:] 
        else: value =slot_value
        list_aux.append(value)
        print(f"Full name given = {value}")
        print(list_aux)
        if slot_value[0].isnumeric():
            dispatcher.utter_message(text=f"write other name")
            return {"full_name": None}
            
            
        else:
            return {"full_name": slot_value}



