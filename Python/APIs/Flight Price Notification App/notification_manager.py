import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import requests
from data_manager import DataManager

TWILIO_ACCOUNT_SID = 'account sid here'
TWILIO_AUTH_TOKEN = 'token here'
account_sid = TWILIO_ACCOUNT_SID
auth_token = TWILIO_AUTH_TOKEN
proxy_client = TwilioHttpClient()   
client = Client(account_sid, auth_token, http_client=proxy_client)

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
   def __init__(self):
        pass
   
   def send_msg(self):
        d = DataManager()
        self.message = client.messages.create(
            body= f"Here are the cheapest flights today:  {d.get_destination_data()} ",
            from_='+12202341958',
            to='+18453723892'
        )
        self.message.sid