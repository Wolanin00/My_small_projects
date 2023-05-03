from datetime import datetime, timedelta
import requests


USER_NAME = "wolanin00"
TOKEN = "REMOVED"
GRAPH_ID = "roller4skates"


pixela_endpoint = "https://pixe.la/v1/users"
pixela_param = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# CREATE USER
# response = requests.post(url=pixela_endpoint, json=pixela_param)
# print(response.text)

# CREATE GRAPH
graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"
graph_param = {
    "id": GRAPH_ID,
    "name": "Roller skates",
    "unit": "Km",
    "type": "float",
    "color": "sora"
}
headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_param, headers=headers)
# print(response.text)

# GET GRAPH
get_graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}.html"

# POST NEW DATA TO THE GRAPH
today = datetime.now()
new_pixel_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"
new_pixel_param = {
    'date': (today-timedelta(days=0)).strftime("%Y%m%d"),
    'quantity': input("How many km did you ride on roller skates today? --> "),
}
response = requests.post(url=new_pixel_endpoint, json=new_pixel_param, headers=headers)
print(response.text)

# PUT NEW DATA TO THE GRAPH
day_to_update = today.strftime('%Y%m%d')  # etc. '20230503'
update_pixel_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{day_to_update}"
update_pixel_param = {
    'quantity': '11.43'
}
# response = requests.put(url=update_pixel_endpoint, json=update_pixel_param, headers=headers)
# print(response.text)

# DELETE PIXEL DATA
day_to_delete = today.strftime('%Y%m%d')
delete_pixel_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{day_to_delete}"

# response = requests.delete(url=delete_pixel_endpoint, headers=headers)
# print(response.text)
