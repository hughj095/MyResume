# Send SMS text to notify user to bring an umbrella if the forecast is rain

# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import requests

# Find your Account SID and Auth Token in Account Info and set the environment variables.
# See http://twil.io/secure

TWILIO_ACCOUNT_SID = 'account sid here'
TWILIO_AUTH_TOKEN = 'token here'

# in BASH, type export OWN_API_KEY=type key here.  
# #api_key = os.environ.get(OWM_API_KEY)
# This saves and secures your
# in BASH as opposed to saving it in the .py file.

account_sid = TWILIO_ACCOUNT_SID
auth_token = TWILIO_AUTH_TOKEN
proxy_client = TwilioHttpClient()   
client = Client(account_sid, auth_token, http_client=proxy_client)

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "api key here"
#Rhode Island
lat = 41.580093
lon = -71.477432

will_rain = False

weather_params = {
    "lat": lat,
    "lon": lon,
    "appid": api_key
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
#weather_data = weather_data["hourly"][0]["weather"][0]["id"]
weather_slice = weather_data["hourly"][:12]

for hour_data in weather_slice:
    cond_code = hour_data["weather"][0]["id"]
    if cond_code < 700:
        will_rain = True

message = client.messages.create(
  body="Bring an umbrella",
  from_='+12202341958',
  to='+18453723892'
)

if will_rain:
    print(message.sid)










 