# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, AllSlotsReset

from email.message import EmailMessage
import ssl,os
import smtplib
# import pandas as pd
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

product_details={'ChatBot':'Deploy Chatbots or virtual assistants that can providing fast and efficient service and converse with customers. Provide financial insights, HR Insights , Educational Details etc.. To know more please check: https://aiviveka.com/virtual-assistants-chat-with-your-customers-effortlessly/',
'QnA System':'Ask Questions and get answers from your knowledge base. No Need to read the whole document if you are looking for specific information in it. To Know more please check: https://aiviveka.com/semantic-search-find-what-you-need-faster/',
'Semantic Search':'We use NLP to understand the intent behind a search query and deliver more accurate and relevant search results to the user’s search query than simply matching keywords. To Know more please check: https://aiviveka.com/semantic-search-find-what-you-need-faster/'}

class ShowProductDetails(Action):
    def name(self) -> Text:
        return "show_product_details"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        product = tracker.get_slot('product')
        dispatcher.utter_message(text=product_details[product]) 

        return []

class ValidateSimpleProductForm(FormValidationAction):
    def name(self)  -> Text:
        return  "validate_simple_product_form"
    
    def validate_product(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        PRODUCTS = ['ChatBot','QnA System','Semantic Search']
        if slot_value not in PRODUCTS:
            dispatcher.utter_message(text=f"Please search for products :{'/'.join(PRODUCTS)} ") 
            return {"product":  None}
        # dispatcher.utter_message(text=f"Showing Details of Product : {slot_value}") 
        return {"product":  slot_value}

class ValidateSupportRequestForm(FormValidationAction):
    def name(self)  -> Text:
        return  "validate_support_request_form"
    
    def validate_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name = tracker.latest_message.get("text")
        if name.strip()== "":
            return {"name":  None}
        return {"name":  name}
    def validate_email(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        email = tracker.latest_message.get("text")
        if email.strip()== "":
            return {"email":  None}
        return {"email":  email}
    def validate_phone_number(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        phone_number = tracker.latest_message.get("text")
        if len(phone_number.strip())!= 10:
            return {"phone_number":  None}
        return {"phone_number":  phone_number}
    
    def validate_message(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message = tracker.latest_message.get("text")
        if len(message.strip())<5:
            dispatcher.utter_message(text="Could you please explain your issue in a bit more detail:")
            return {"message":  None}
        return {"message":  message}
    
    def validate_confirm_detail(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # intent_name=tracker.get_intent_of_latest_message()
        # confirm_detail = tracker.latest_message.get("text")
        confirm_detail = tracker.get_slot('confirm_detail')
        # if confirm_detail not in ['Yes','No']:
        # dispatcher.utter_message(text=confirm_detail)
            # return {"confirm_detail":  None}
        return {"confirm_detail":  confirm_detail}

class SubmitSupportRequestForm(Action):
    def name(self) -> Text:
        return "action_submit_support_request"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        intent_name=tracker.get_intent_of_latest_message()
        # confirm_detail = tracker.get_slot('confirm_detail')
        # if confirm_detail == 'Yes':
        if intent_name=='affirm':
            self.sendemail(tracker)
            dispatcher.utter_message(template="utter_mail_success")
        else: 
            dispatcher.utter_message(template="utter_mail_cancelled")
        return []
    def sendemail(self,tracker):
        email_sender='rasabot99@gmail.com'
        email_pwd=os.environ.get('RASA_PWD')
        email_receiver='rasabot99@gmail.com'

        name = tracker.get_slot('name')
        email = tracker.get_slot('email')
        phone_number = tracker.get_slot('phone_number')
        message = tracker.get_slot('message')
        body=f'''
        Name:{name} \n
        Email: {email} \n 
        Phone No: {phone_number} \n
        Message: {message} \n
        '''
        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['Subject'] = f"Support: {message[:50]}"
        em.set_content(body)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
            smtp.login(email_sender,email_pwd)
            smtp.sendmail(email_sender,email_receiver,em.as_string())

class ActionSlotReset(Action): 	
    def name(self): 		
        return 'action_slot_reset' 
	
    def run(self, dispatcher, tracker, domain): 		
        return[AllSlotsReset()]