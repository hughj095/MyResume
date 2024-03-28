# Connects to API to get realtime position of the ISS, then emails you if conditions are right for you 
# to see it above your location

import requests
import datetime as dt
import time
import smtplib

MY_LAT = 41.9192
MY_LONG = -71.3963
my_email = "your email here"
password = "your password here"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()

longitude = float(data["iss_position"]["longitude"])
latitude = float(data["iss_position"]["latitude"])

iss_position = (longitude, latitude)

parameters = {"lat": MY_LAT,
              "lng": MY_LONG,
              "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
print(data)
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

print(sunrise)
print(sunset)


time_now = dt.datetime.now()

while True:
    time.sleep(60)
    if MY_LAT < latitude + 5 and MY_LAT > latitude - 5:
        if MY_LONG < longitude + 5 and MY_LONG > longitude - 5:
            if time_now > sunset and time_now < sunrise:
                with smtplib.SMTP_SSL("smtp.gmail.com") as connection:
                    #TLS secures smtp connection
                    connection.ehlo()

                    connection.login(user=my_email, password=password)
                    connection.sendmail(
                        from_addr=my_email, 
                        to_addrs=my_email,
                        msg="Look Up to see ISS")




