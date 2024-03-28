# runs an error "A device attached to the system is not functioning."

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_driver_path = './web scraping/chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get('https://www.python.org/')

list_upcoming_events = driver.find_elements(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li')
for i in list_upcoming_events:
    print(i)
event = driver.find_elements(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[1]/a')

events = {}

for n in range(0,len(event)):
    events[n] = {
        "time": event[n].text,
        "name": list_upcoming_events[n].text
    }


time.sleep(3)
driver.quit()