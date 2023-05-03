import requests
from datetime import datetime

# ---------------------- NUTRITION ----------------------
GENDER = "male"
WEIGHT_KG = "69.1"
HEIGHT_CM = "182.5"
AGE = "23"

nutrition_id = "REMOVED"
nutrition_keys = "REMOVED"
sheet_bearer = "Bearer REMOVED"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoints = "https://api.sheety.co/001804097fe74cbf3a51ce2c254f8d74/myWorkouts/workouts"

exercise_text = input("What exercise did you do today?: ")

nutrition_headers = {
    "x-app-id": nutrition_id,
    "x-app-key": nutrition_keys
}
nutrition_param = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=exercise_endpoint, headers=nutrition_headers, json=nutrition_param)
print(response.status_code)
result = response.json()
# print(result)

# ---------------------- SHEET ----------------------
sheet_headers = {
    "Authorization": sheet_bearer
}

for exercise in result['exercises']:
    sheet_param = {
        "workout": {
            "date": datetime.now().strftime('%d/%m/%Y'),
            "time": datetime.now().strftime('%H:%M:%S'),
            "exercise": f"{exercise['name']}".title(),
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories'],
            "id": exercise['tag_id']
        }
    }
    response = requests.post(url=sheet_endpoints, json=sheet_param, headers=sheet_headers)
    print(response.status_code)
    # print(response.text)
