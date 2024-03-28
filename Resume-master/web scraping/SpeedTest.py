# This program scrapes your internet upload and download speeds, then tweets at your ISP if the speeds 
#   are slower than advertised
#       It references TwtrBot.py which houses the Class and methods used to scrape and tweet

########## References
from TwtrBot import InternetSpeedTwitterBot
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pywin32_system32

########## CONSTANTS
PROMISED_DOWN = 100
PROMISED_UP = 100
chrome_driver_path = './web scraping/chromedriver.exe'
TWITTER_EMAIL = "YOUR TWITTER EMAIL"
TWITTER_PWORD = "YOUR TWITTER PWORD"

########## Executes Class and Methods
InternetSpeedTwitterBot(chrome_driver_path)
InternetSpeedTwitterBot.get_internet_speed
InternetSpeedTwitterBot.tweet_at_provider

