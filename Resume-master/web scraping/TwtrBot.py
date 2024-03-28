# Reference file for SpeedTest.py.  This houses the Class and methods.

from selenium import webdriver
from SpeedTest import chrome_driver_path
from SpeedTest import By
from SpeedTest import time
from selenium import Keys
from SpeedTest import PROMISED_DOWN
from SpeedTest import PROMISED_UP
from SpeedTest import TWITTER_EMAIL
from SpeedTest import TWITTER_PWORD

#main class of program execution
class InternetSpeedTwitterBot():
    def __init__(self):
        super().__init__()
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.down = 0
        self.up = 0

    #Scrapes Internet Speed
    def get_internet_speed(self):
        time.sleep(3)
        go_button = self.driver.find_element_by_css_selector(".start-button a")
        go_button.click()
        time.sleep(60)
        self.driver.get('https://www.speedtest.net/result/14211109769')
        self.up = self.driver.find_element(By.CLASS_NAME, 'result-data.u-align-left')
        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        
    #Tweets at ISP if internet speeds are lower than advertised
    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")
        time.sleep(2)

        #Login info
        email_input = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input')
        password_input = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')
        email_input.send_keys(TWITTER_EMAIL)
        password_input.send_keys(TWITTER_PWORD)
        time.sleep(2)
        password_input.send_keys(Keys.ENTER)
        time.sleep(5)

        #Compose Tweet
        tweet_compose = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_compose.send_keys(tweet)
        time.sleep(3)
        tweet_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        tweet_button.click()
        time.sleep(2)

        self.driver.quit()