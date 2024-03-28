from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import lxml

# set up the webdriver
driver = webdriver.Chrome()

# navigate to the mlb scores page
driver.get("https://www.mlb.com/scores")

# Wait for the page to fully load
driver.implicitly_wait(5)

soup = BeautifulSoup(driver.page_source, 'lxml')
tables = soup.find_all("div")
dfs = pd.read_html(str(tables))
print(dfs)

# find the scores container element
scores_container = driver.find_element(By.CLASS_NAME, "TeamWrappersstyle__DesktopTeamWrapper-sc-uqs6qh-0 fdaoCu").text
#(By.ID, "m-documentationgrid")
print(scores_container)
# find all of the scorecard elements within the container
scorecards = scores_container.find_elements_by_class_name("scorecard")

# loop through the scorecards and extract the relevant data
for card in scorecards:
    # extract the team names
    team_names = card.find_elements_by_class_name("team-name")
    home_team = team_names[0].text
    away_team = team_names[1].text
    
    # extract the score
    score = card.find_element_by_class_name("total-score").text
    
    # print out the results
    print(f"{away_team} @ {home_team}: {score}")
    
# close the webdriver
driver.quit()