from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pywin32_system32

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

chrome_driver_path = './web scraping/chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get('https://www.linkedin.com/in/john-hughes-42665152/')

profile = []
name = driver.find_element(By.CLASS_NAME, 'text-heading-xlarge inline t-24 v-align-middle break-words')
company = driver.find_element(By.XPATH, '//*[@id="ember767"]/div[3]/ul/li[1]/div/div[2]/div/div[1]/span[1]/span[1]/text()')
if "· Full-time" in company.text:
    company.text.replace("· Full-time","").strip()
elif "· Part-time" in company.text:
    company.text.replace("· Part-time","").strip()



profile.append(name, company)
print(profile)