import requests
from datetime import datetime

CRACOW_LAT = 50.064651
CRACOW_LNG = 19.944981

parameters = {
    'lat': CRACOW_LAT,
    'lng': CRACOW_LNG,
    'formatted': 0
}

response = requests.get('https://api.sunrise-sunset.org/json', parameters)
response.raise_for_status()

data = response.json()
sunrise_hour = data['results']['sunrise'].split('T')[1].split(':')[0]
sunset_hour = data['results']['sunset'].split('T')[1].split(':')[0]
print(sunrise_hour)
print(sunset_hour)

time_now = datetime.now()
print(time_now.hour)
