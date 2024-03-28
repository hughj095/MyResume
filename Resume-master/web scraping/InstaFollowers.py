# This program executes on your Instagram Account.  With a chosen competitor IG Account, it follows all of the 
# followers on your competitors IG Account.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time
import pywin32_system32

chrome_driver_path = './web scraping/chromedriver.exe'
SIMILAR_ACCOUNT = 'chefsteps'
INSTA_EMAIL = "YOUR INSTA EMAIL"
INSTA_PWORD = "YOUR INSTA PWORD"

class IGFollower():
    def __init__(self):
        super().__init__()
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)

    def login(self):
        self.driver.get('https://www.instagram.com/accounts/login/')
        email_input = self.driver.find_element(By.NAME, "username")
        password_input = self.driver.find_element(By.NAME, "password")
        email_input.send_keys(INSTA_EMAIL)
        password_input.send_keys(INSTA_PWORD)
        time.sleep(2)
        password_input.send_keys(Keys.ENTER)
        time.sleep(5)

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")

        time.sleep(2)
        followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()

        time.sleep(2)
        modal = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')
        for i in range(10):
            #In this case we're executing some Javascript, that's what the execute_script() method does. 
            #The method can accept the script as well as a HTML element. 
            #The modal in this case, becomes the arguments[0] in the script.
            #Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()

IGFollower.login
IGFollower.find_followers
IGFollower.follow




