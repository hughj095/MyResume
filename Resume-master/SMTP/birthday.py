#Selects random birthday letter from folder to email on birthday
# Auto runs with BASH script on PythonAnywhere.com, daily at 15:21

##################### Extra Hard Starting Project ######################

import datetime as dt
import random
import smtplib

my_email = "your email here"
password = "your password here"

# 2. Check if today matches a birthday in the birthdays.csv

now = dt.datetime.now()
month = now.month
day = now.day

with open("birthdays.csv", "r") as data:
    data = data.read()
    data = data.split(",")
print(data)
Jenn_month = data[7]
Jenn_day = data[8]

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
randint = random.randint(1,3)
with open(f"./SMTP/letter_templates/letter_{randint}.txt", "r") as letter:
    letter = letter.read()
    letter = letter.replace("[NAME]",data[0])


# 4. Send the letter generated in step 3 to that person's email address.
if month == Jenn_month and day == Jenn_day:
    with smtplib.SMTP_SSL("smtp.gmail.com") as connection:
        #TLS secures smtp connection
        connection.ehlo()

        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs=data[5],
            msg=letter
        )