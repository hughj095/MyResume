# API stock data and API news data to send notification to cell phone
# if stock price is > or < 5% in a closing price

import requests
from datetime import date, timedelta
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla"
API_KEY = "KU0OHB90ZUWQ9V5Y"
NEWS_KEY = "48e53659f2f64d418750d30264d30933"
TWILIO_ACCOUNT_SID = 'account sid here'
TWILIO_AUTH_TOKEN = 'token here'
yesterday = date.today()-timedelta(1)
print(yesterday)

STOCK_ENDPOINT = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={STOCK_NAME}&interval=5min&apikey={API_KEY}"
NEWS_ENDPOINT = f"https://newsapi.org/v2/everything?q={COMPANY_NAME}&from={yesterday}&sortBy=publishedAt&apiKey={NEWS_KEY}"

#Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
response = requests.get(url=STOCK_ENDPOINT)
response.raise_for_status()

data = response.json()['Time Series (5min)']
data_list = [value for (key,value) in data.items()]
yesterday_closing_price = data_list[0]["4. close"]
print(yesterday_closing_price)

#Get the day before yesterday's closing stock price
daybefore_closing_price = data_list[1]["4. close"]
print(daybefore_closing_price)

#Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
diff = float(abs(float(yesterday_closing_price) - float(daybefore_closing_price)))
posneg = float(yesterday_closing_price) - float(daybefore_closing_price)

change = diff/float(daybefore_closing_price)*100
print(str(round(change,2)) + '%')


#If percentage is greater than 5 then print("Get News").
if change > 5:

#Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
    news = requests.get(url=NEWS_ENDPOINT)
    news.raise_for_status()
    news = news.json()["articles"]


#Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    three_arts = news[:3]

#Create a new list of the first 3 article's headline and description using list comprehension.
    if posneg < 0:
        symbol = "🔻"
    else:
        symbol = "🔺"
    
    list = [f"{STOCK_NAME} {symbol}{change}\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_arts]
    account_sid = TWILIO_ACCOUNT_SID
    auth_token = TWILIO_AUTH_TOKEN
    proxy_client = TwilioHttpClient()   
    client = Client(account_sid, auth_token, http_client=proxy_client)

    for article in list:
        message = client.messages.create(
            body=article,
            from_='+12202341958',
            to='+18453723892'
        )
        print(message.sid)

