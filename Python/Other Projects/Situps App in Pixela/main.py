# Pixela tracker for situps by day at https://pixe.la/v1/users/john1/graphs/graph1.html

import requests
from datetime import datetime

USERNAME = "john1"
TOKEN = "3edc4rfv"
ID = "graph1"

#Setup Account
pixela_endpoint = "https://pixe.la/v1/users"
params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(pixela_endpoint, json=params)
# print(response.text)

#Setup Graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_params = {
    "id": ID,
    "name": "Situps",
    "unit": "Situps",
    "type": "int",
    "color": "ajisai"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
today = datetime.now()
# values = {
#     "date": today.strftime("%Y%m%d"),
#     "quantity": "10"
# }
# pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}"
# response = requests.post(url=pixel_creation_endpoint, json=values, headers=headers)
# print(response.text)

#Update Pixel
date = "20221122"
update_values = {
    "name": "graph1",
    "date": date,
    "quantity": "50"
}
# pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}/{date}"
# response = requests.put(url=pixel_update_endpoint, json=update_values, headers=headers)
# print(response.text)

#Delete Pixel
pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}/{date}"
response = requests.delete(pixel_delete_endpoint, headers=headers)