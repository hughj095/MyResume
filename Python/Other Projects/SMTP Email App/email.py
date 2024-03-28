# Sends motivational quote from text file to email (change password to run)

import smtplib
import datetime as dt
import random

my_email = "your email here"
password = "your password here"

now = dt.datetime.now()
print(now)
year = now.year
print(year)

#Monday is 0, Sunday is 6
dayofweek = now.weekday()
print(dayofweek)

date_of_birth = dt.datetime(year=1985, month=7, day=25, hour=9)
print(date_of_birth)

with open("./SMTP/quotes.txt", "r") as quotes:
    list = quotes.read()
    list = list.split("\n")

rand_quote = random.choice(list)

if dayofweek == 4:
    with smtplib.SMTP_SSL("smtp.gmail.com") as connection:
        #TLS secures smtp connection
        connection.ehlo()

        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs="recipient email here",
            msg=rand_quote
        )