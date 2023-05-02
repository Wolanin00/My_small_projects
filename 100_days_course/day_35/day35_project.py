import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.8/onecall"
api_key = "REMOVED"

account_sid = "REMOVED"
auth_token = "REMOVED"

parameters = {
    'lat': 50.0833,
    'lon': 19.9167,
    'appid': api_key,
    'exclude': "current,minutely,daily,alerts"
}

response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False

hours_list = weather_data['hourly'][:12]
for hour_data in hours_list:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring umbrella.",
        from_='Trial_number',
        to='Your number'
    )
    print(message.status)
