# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 20:01:23 2021

@author: johnm
"""

from selenium import webdriver
import pandas as pd
import smtplib, ssl

#Local location of chromedriver version 87 from Google
executable_path = r'C:\Users\johnm\OneDrive\Documents\Udemy Python and R Code\Python Code\chromedriver.exe'

#SportsBetRI Browser
username = "hughesjm314@gmail.com"
password = "John08sports$"
driver = webdriver.Chrome(executable_path) 
driver.get('https://sportsbetrhodeisland.com/sports')
driver.maximize_window()
login = driver.find_element_by_xpath("//button[@class ='login_btn btn']")
login.click()
myusername = driver.find_element_by_id("username")
myusername.send_keys(username)
mypassword = driver.find_element_by_id("password")
mypassword.send_keys(password)
login2 = driver.find_element_by_xpath('//*[@id="app"]/div[5]/div/div/form/div[5]/button[2]/div/span')
login2.click()
driver.get('https://sportsbetrhodeisland.com/sports/navigation/830.1/12256.1')
dfold = pd.DataFrame()

if driver.find_element_by_xpath('/html/body/div/div/div[2]/div[6]/main/div/div/div/div/div/div[2]/div[2]/div/div/div[4]/div/div/div/div[2]/div/div/div/div/div/div/div[1]/div/div/div[2]/div[1]/div/div/div/div[3]/div/div/div[1]/span/div/div/div/div[1]/div[2]').text == 'null':
    liveover1 = 'none'
else: 
    liveover1 = int(driver.find_element_by_xpath('/html/body/div/div/div[2]/div[6]/main/div/div/div/div/div/div[2]/div[2]/div/div/div[4]/div/div/div/div[2]/div/div/div/div/div/div/div[1]/div/div/div[2]/div[1]/div/div/div/div[3]/div/div/div[1]/span/div/div/div/div[1]/div[2]').text)
    liveaway1 = driver.find_element_by_xpath('/html/body/div/div/div[2]/div[6]/main/div/div/div/div/div/div[2]/div[2]/div/div/div[4]/div/div/div/div[2]/div/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/span').text
    livehome1 = driver.find_element_by_xpath('/html/body/div/div/div[2]/div[6]/main/div/div/div/div/div/div[2]/div[2]/div/div/div[4]/div/div/div/div[2]/div/div/div/div/div/div/div[1]/div/div/div[1]/div/div[2]/span').text

if driver.find_element_by_xpath('/html/body/div/div/div[2]/div[6]/main/div/div/div/div/div/div[2]/div[2]/div/div/div[4]/div/div/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div/div/div[3]/div/div/div[1]/span/div/div/div/div[1]/div[2]').text == 'null':
    liveover2 = 'none'
else: 
    liveover2 = int(driver.find_element_by_xpath('/html/body/div/div/div[2]/div[6]/main/div/div/div/div/div/div[2]/div[2]/div/div/div[4]/div/div/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div/div/div[3]/div/div/div[1]/span/div/div/div/div[1]/div[2]').text)
    liveaway2 = driver.find_element_by_xpath('/html/body/div/div/div[2]/div[6]/main/div/div/div/div/div/div[2]/div[2]/div/div/div[4]/div/div/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div[1]/span').text
    livehome2 = driver.find_element_by_xpath('/html/body/div/div/div[2]/div[6]/main/div/div/div/div/div/div[2]/div[2]/div/div/div[4]/div/div/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div[2]/span').text


betdata = [[liveaway1, livehome1, liveover1]
,[liveaway2, livehome2, liveover2]]
dfbet = pd.DataFrame(betdata, columns=['away','homebet','o/u'])


#ESPN Browser
#driver2 = webdriver.Chrome()
driver.get('https://www.espn.com/nba/scoreboard/_/date/20221018')
#driver2.maximize_window()

if driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[4]/div[3]/div/div/div[1]/div/section/div/section[1]/div/div/div/div/div/a/div/div[1]/ul/li[1]/div/div').text == 'null':
    espnaway1 = 'none'
else:    
    espnaway1 = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[4]/div[3]/div/div/div[1]/div/section/div/section[1]/div/div/div/div/div/a/div/div[1]/ul/li[1]/div/div').text
if driver.find_element_by_xpath('//*[@id="401468016"]/div[1]/div/div[1]/div/div/ul/li[2]/div[1]/div/a/div').text == 'null':
    espnhome1 = 'none'
else:    
    espnhome1 = driver.find_element_by_xpath('//*[@id="401468016"]/div[1]/div/div[1]/div/div/ul/li[2]/div[1]/div/a/div').text
if driver.find_element_by_xpath('/html/body/div[5]/section/section/div/section[1]/div[1]/div[3]/article[1]/div/div/section/div/table/tbody/tr[1]/td[6]/span').text == 'null':
    awayscore1 = 0
    homescore1 = 0
else: 
    awayscore1 = int(driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[4]/div[3]/div/div/div[1]/div/section/div/section[1]/div/div/div/div/div/a/div[1]/div[1]/ul/li[2]/div/div/div').text)
if  driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[4]/div[3]/div/div/div[1]/div/section/div/section[1]/div/div/div/div/div/a/div/div[2]/div[1]').text == 'null':
    time1 = 0
else: 
    time1 = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[4]/div[3]/div/div/div[1]/div/section/div/section[1]/div/div/div/div/div/a/div/div[2]/div[1]').text


if driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[4]/div[3]/div/div[1]/div[1]/div/section/div/section[2]/div[1]/div/div[1]/div/div/ul/li[1]/div[1]/div/a/div').text == 'null':
    espnaway2 = 'none'
else:    
    espnaway2 = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[4]/div[3]/div/div[1]/div[1]/div/section/div/section[2]/div[1]/div/div[1]/div/div/ul/li[1]/div[1]/div/a/div').text
if driver.find_element_by_xpath('//*[@id="401468017"]/div[1]/div/div[1]/div/div/ul/li[2]/div[1]/div/a/div').text == 'null':
    espnhome2 = 'none'
else:    
    espnhome2 = driver.find_element_by_xpath('//*[@id="401468017"]/div[1]/div/div[1]/div/div/ul/li[2]/div[1]/div/a/div').text
if driver.find_element_by_xpath('//*[@id="401468017"]/div[1]/div/div[1]/div/div/ul/li[1]/div[2]').text == 'null':
    awayscore2 = 0
    homescore2 = 0
else: 
    awayscore2 = int(driver.find_element_by_xpath('//*[@id="401468017"]/div[1]/div/div[1]/div/div/ul/li[1]/div[2]').text)
if  driver.find_element_by_xpath('//*[@id="401468017"]/div[1]/div/div[1]/div/div/div/div[1]').text == 'null':
    time2 = 0
else: 
    time2 = driver.find_element_by_xpath('//*[@id="401468017"]/div[1]/div/div[1]/div/div/div/div[1]').text

livedata = [[espnaway1, espnhome1, awayscore1, homescore1, time1]
,[espnaway2, espnhome2, awayscore2, homescore2, time2]]
dfespn = pd.DataFrame(livedata, columns=['away','home','awayscore','homescore','time'])
dfteams = pd.read_csv(r"C:\Users\johnm\OneDrive\Documents\Udemy Python and R Code\Python Code\nba teams table.csv")
dfespn = pd.merge(dfespn, dfteams, how = 'inner', on = 'away')
dfespn = pd.merge(dfespn, dfbet, on = 'away')





driver.close()



try: awayscore1 = 
except: awayscore1 = 'none'
try: homescore1 = driver.find_element_by_xpath('/html/body/div[5]/section/section/div/section[1]/div[1]/div[3]/article[1]/div/div/section/div/table/tbody/tr[2]/td[6]/span').text
except: homescore1 = 'none'
try: time1 = driver.find_element_by_xpath('/html/body/div[5]/section/section/div/section[1]/div[1]/div[3]/article[1]/div/div/section/div/table/thead/tr/th[1]').text
except: time1 = 'none'

if time1[2] == ":":
    qtr1 = int(time1[8])
elif time1 == 'none':
    time1 == "12:00 - 1st"
elif time1[2] == ".":
    qtr1 = time1[7]
elif time1 == "Halftime":
    qtr1 = 3
elif time1[:3] == "End":
    qtr1 = time1[8]
elif time1 == "FINAL":
    qtr1 = 4
    timeleft1 = 0
else: qtr1 = int(time1[7])
if time1[2] == ":": 
    timeleft1 = 48-(int(time1[8])*12)+int(time1[:2])
elif time1[1] == ":":
    timeleft1 = 48-(int(time1[7])*12)+int(time1[:1])
elif time1 == "Halftime":
    time1 == "12:00 - 3rd"
    timeleft1 = 24
else: 
    timeleft1 = 0

try: avgptsmin1 = (int(awayscore1)+int(homescore1))/(48-float(timeleft1))
except: avgptsmin1 = 0
calc1=(int(awayscore1)+int(homescore1))/(48-timeleft1)*48

try: espnaway2 = driver.find_element_by_xpath('/html/body/div[5]/section/section/div/section[1]/div[1]/div[3]/article[2]/div/div/section/div/table/tbody/tr[1]/td[1]/div[2]/h2/a/span[1]').text = null:
    espnaway2 = 'none'
try: espnhome2 = driver.find_element_by_xpath('/html/body/div[5]/section/section/div/section[1]/div[1]/div[3]/article[2]/div/div/section/div/table/tbody/tr[2]/td[1]/div[2]/h2/a/span[1]').text
except: espnhome2 = 'none'
try: awayscore2 = driver.find_element_by_xpath('/html/body/div[5]/section/section/div/section[1]/div[1]/div[3]/article[2]/div/div/section/div/table/tbody/tr[1]/td[6]/span').text
except: awayscore2 = 'none'
try: homescore2 = driver.find_element_by_xpath('/html/body/div[5]/section/section/div/section[1]/div[1]/div[3]/article[2]/div/div/section/div/table/tbody/tr[2]/td[6]/span').text
except: homescore2 = 'none'
try: time2 = driver.find_element_by_xpath('/html/body/div[5]/section/section/div/section[1]/div[1]/div[3]/article[2]/div/div/section/div/table/thead/tr/th[1]').text
except: time2 = 'none'

if time2[2] == ":":
    qtr2 = int(time2[8])
elif time2 == 'none':
    time2 == "12:00 - 1st"
elif time2[2] == ".":
    qtr2 = time2[7]
elif time2 == "Halftime":
    qtr2 = 3
elif time2[:3] == "End":
    qtr2 = time2[8]
elif time2 == "FINAL":
    qtr2 = 4
    timeleft2 = 0
else: qtr2 = int(time2[7])
if time2[2] == ":": 
    timeleft2 = 48-(int(time2[8])*12)+int(time2[:2])
elif time2[1] == ":":
    timeleft2 = 48-(int(time2[7])*12)+int(time2[:1])
elif time2 == "Halftime":
    time2 == "12:00 - 3rd"
    timeleft2 = 24
else: 
    timeleft2 = 0

avgptsmin2 = (int(awayscore2)+int(homescore2))/(48-float(timeleft2))
calc2=(int(awayscore2)+int(homescore2))/(48-timeleft2)*48


try: espnaway3 = driver.find_element_by_xpath('/html/body/div[5]/section/section/div/section[1]/div[1]/div[3]/article[3]/div/div/section/div/table/tbody/tr[1]/td[1]/div[2]/h2/a/span[1]').text
except: espnaway3 = 'none'
try: espnhome3 = driver.find_element_by_xpath('/html/body/div[5]/section/section/div/section[1]/div[1]/div[3]/article[3]/div/div/section/div/table/tbody/tr[2]/td[1]/div[2]/h2/a/span[1]').text
except: espnhome3 = 'none'
try: awayscore3 = driver.find_element_by_xpath('/html/body/div[5]/section/section/div/section[1]/div[1]/div[3]/article[3]/div/div/section/div/table/tbody/tr[1]/td[6]/span').text
except: awayscore3 = 'none'
try: homescore3 = driver.find_element_by_xpath('/html/body/div[5]/section/section/div/section[1]/div[1]/div[3]/article[3]/div/div/section/div/table/tbody/tr[2]/td[6]/span').text
except: homescore3 = 'none'
try: time3 = driver.find_element_by_xpath('/html/body/div[5]/section/section/div/section[1]/div[1]/div[3]/article[3]/div/div/section/div/table/thead/tr/th[1]').text
except: time3 = 'none'

if time3[2] == ":":
    qtr3 = int(time3[8])
elif time3 == 'none':
    time3 == "12:00 - 1st"
elif time3[2] == ".":
    qtr3 = time3[7]
elif time3 == "Halftime":
    qtr3 = 3
elif time3[:3] == "End":
    qtr3 = time3[8]
elif time3 == "FINAL":
    qtr3 = 4
    timeleft3 = 0
else: qtr3 = int(time3[7])
if time3[2] == ":": 
    timeleft3 = 48-(int(time3[8])*12)+int(time3[:2])
elif time3[1] == ":":
    timeleft3 = 48-(int(time3[7])*12)+int(time3[:1])
elif time3 == "Halftime":
    time3 == "12:00 - 3rd"
    timeleft3 = 24
else: 
    timeleft3 = 0
avgptsmin3 = (int(awayscore3)+int(homescore3))/(48-float(timeleft3))
calc3=(int(awayscore3)+int(homescore3))/(48-timeleft3)*48

try: espnaway4 = driver.find_element_by_xpath('/html/body/div[5]/section/section/div/section[1]/div[1]/div[3]/article[4]/div/div/section/div/table/tbody/tr[1]/td[1]/div[2]/h2/a/span[1]').text
except: espnaway4 = 'none'
try: espnhome4 = driver.find_element_by_xpath('/html/body/div[5]/section/section/div/section[1]/div[1]/div[3]/article[4]/div/div/section/div/table/tbody/tr[2]/td[1]/div[2]/h2/a/span[1]').text
except: espnhome4 = 'none'
try: awayscore4 = driver.find_element_by_xpath('/html/body/div[5]/section/section/div/section[1]/div[1]/div[3]/article[3]/div/div/section/div/table/tbody/tr[1]/td[6]/span').text
except: awayscore4 = 'none'
try: homescore4 = driver.find_element_by_xpath('/html/body/div[5]/section/section/div/section[1]/div[1]/div[3]/article[3]/div/div/section/div/table/tbody/tr[2]/td[6]/span').text
except: homescore4 = 'none'
try: time4 = driver.find_element_by_xpath('/html/body/div[5]/section/section/div/section[1]/div[1]/div[3]/article[4]/div/div/section/div/table/thead/tr/th[1]').text
except: time4 = 'none'

if time4[2] == ":":
    qtr4 = int(time4[8])
elif time4 == 'none':
    time4 == "12:00 - 1st"
elif time4[2] == ".":
    qtr4 = time4[7]
elif time4 == "Halftime":
    qtr4 = 3
elif time4[:3] == "End":
    qtr4 = time4[8]
elif time4 == "FINAL":
    qtr4 = 4
    timeleft4 = 0
else: qtr4 = int(time4[7])
if time4[2] == ":": 
    timeleft4 = 48-(int(time4[8])*12)+int(time4[:2])
elif time4[1] == ":":
    timeleft4 = 48-(int(time4[7])*12)+int(time4[:1])
elif time4 == "Halftime":
    time4 == "12:00 - 3rd"
    timeleft4 = 24
else: 
    timeleft4 = 0

avgptsmin4 = (int(awayscore4)+int(homescore4))/(48-float(timeleft4))
calc4=(int(awayscore4)+int(homescore4))/(48-timeleft4)*48

livedata = [[espnaway1, espnhome1, awayscore1, homescore1, time1, calc1, avgptsmin1]
,[espnaway2, espnhome2, awayscore2, homescore2, time2, calc2, avgptsmin2]
,[espnaway3, espnhome3, awayscore3, homescore3, time3, calc3, avgptsmin3]
,[espnaway4, espnhome4, awayscore4, homescore4, time4, calc4, avgptsmin4]]

dfespn = pd.DataFrame(livedata, columns=['mascot','homeespn','awayscore','homescore','time','calc','avgptsmin'])



dfespn = pd.merge(dfespn, dfbet, on = 'away')
dfcount = dfespn.pivot_table(index=['mascot'], aggfunc='size')
#if dfcount[0]>1:
 #   dfespn = dfespn.loc[[0]]
#else: pass
#try: dfespn = pd.concat([dfold, dfespn], ignore_index = True, sort = False)
#except:  
#    dfold = pd.DataFrame()
#    dfold = dfespn
driver.close()
#driver2.close()
#dfespn.to_excel('dflive.xlsx')
    
#Email the info
smtpServer = "smtp.gmail.com"
port = 587
context = ssl.create_default_context()
emailSender = "hughesjm314@gmail.com"
password = "John08gmail%"
myEmail = "john.m.hughes84@outlook.com"
emailRecipients = [myEmail] 
if int(avgptsmin4) > 5.8:
    newEmail = espnaway4 + " Under"
    try:
        server = smtplib.SMTP(smtpServer,port)
        server.starttls(context=context)
        server.login(newEmail, password)
    except Exception as e:
        print("the email could not be sent.")
    finally:
        server.quit()  
elif int(avgptsmin4) < 3.2:
    newEmail = espnaway4 + " Over"
    try:
        server = smtplib.SMTP(smtpServer,port)
        server.starttls(context=context)
        server.login(newEmail, password)
    except Exception as e:
        print("the email could not be sent.")
    finally:
        server.quit()  
else: exit
