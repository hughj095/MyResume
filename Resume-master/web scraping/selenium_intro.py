from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = './web scraping/chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get('https://www.amazon.com/s?k=disney+tee&i=fashion&crid=4Y8SOBCG5A1L&sprefix=disney+tee%2Cfashion%2C96&ref=nb_sb_noss_1')
price = driver.find_element(By.CLASS_NAME, 'a-price-whole')
print(price.text)

# search_bar = driver.find_element(By.TAG_NAME, "placeholder")
# search_bar = driver.find_element(By.ID, "placeholder")

#logo = driver.find_element(By.CLASS_NAME, "python-logo")
# Can get the size of an element with logo.size
#print(logo.size)

#css_element = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
#print(css_element.text)

#X Path element
#link = driver.find_element(By.XPATH, "X_path_here")
#print(link.text)

#find every tag of the same name
#multiple = driver.find_elements(By.ID, "a")





# close driver tab
#driver.close()

# quits entire browser
driver.quit()