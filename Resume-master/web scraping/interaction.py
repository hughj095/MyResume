from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pywin32_system32

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

chrome_driver_path = './web scraping/chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get('https://en.wikipedia.org/wiki/Main_Page')

#find the first div above the element, then space and 'a' tag
number = driver.find_element(By.CSS_SELECTOR, 'articlecount a')
print(number)

search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
search.send_keys("ENTER")

#number.click()

#Use find by CSS Selector when it's unique to the page, by element one level up and level you're looking for
#  "form button"

time.sleep(3)
driver.quit()


