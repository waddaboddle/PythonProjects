import requests
from datetime import datetime

USERNAME = "waddaboddle"
TOKEN = "aseviadfvnj23i23krfgsd34"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "aseviadfvnj23i23krfgsd34",
    "username": "waddaboddle",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "sora"
}

header = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=header)
# print(response.text)

today = datetime.now()
print(today.strftime("%Y%m%d"))
pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many Kms did you cycle today? "),
}

response = requests.post(url=pixela_endpoint, json=pixel_config, headers=header)
print(response.text)

put_endpoint = f"{pixel_endpoint}/20231001"

put_config = {
    "quantity": "3.35",
}

# response = requests.put(url=put_endpoint, json=put_config, headers=header)
# print(response.text)

delete_endpoint = f"{put_endpoint}"

# response = requests.delete(url=delete_endpoint, headers=header)
# print(response.text)
