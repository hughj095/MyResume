from bs4 import BeautifulSoup
import requests
import lxml
import smtplib

my_email = "your email here"
password = "your password here"

response = requests.get("https://www.amazon.com/Zuluf-Small-Hanging-Cross-Bethlehem/dp/B00AYE039U/" + 
    "ref=sr_1_2_sspa?crid=RGAOI1GYTP&keywords=small%2Bcross%2Bfor%2Bwall&qid=1672428745&s=home-garden&sprefix=small%2Bcross%2Bfor%2Bwal%2Cgarden%2C117&sr=1-2-spons&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUE5TzFNQUs2RDZRVDEmZW5jcnlwdGVkSWQ9QTAyMDY5ODIxNk9FQkdIUzc5OUlZJmVuY3J5cHRlZEFkSWQ9QTA1MjkwNjIzNThKNDJVMzRJVExNJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ&th=1", 
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47",
    "Accept-Language":"en-US,en;q=0.9"})
webpage = response.text
soup = BeautifulSoup(webpage, "lxml")

item = soup.find_all(name="span", class_="a-price-whole")
print(item)

item_list = []

for pot in item:
    item_list.append(pot.text)

for price in item_list:
    price = price.rstrip(price[-1])


print(item_list)
target_price = 9

for price in item_list:
    if price < target_price:
        print("Cheap price found")




with smtplib.SMTP_SSL("smtp.gmail.com") as connection:
        #TLS secures smtp connection
        connection.ehlo()

        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs="recipient email here",
            msg=f"Price Alert on {response} under {target_price}!"
        )
