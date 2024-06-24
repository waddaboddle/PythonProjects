import requests
from datetime import datetime

import os


APP_ID = os.environ.get("APP_ID")
APP_KEY = os.environ.get("APP_KEY")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_ENDPOINT = os.environ.get("SHEET_ENDPOINT")
SHEET_TOKEN = os.environ.get("SHEET_TOKEN")

GENDER = "male"
WEIGHT_KG = "92.9"
HEIGHT = "177.8"
AGE = "24"

exercise_header = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}

exercise_input = input("What exercises did you do today?:")

exercise_parameters = {
    "query": exercise_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT,
    "age": AGE,
}

exercise_response = requests.post(url=exercise_endpoint, json=exercise_parameters, headers=exercise_header)
exercise_response.raise_for_status()
print(exercise_response.json())

date = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%X")
exercise_data = exercise_response.json()

sheety_header = {
    "Authorization": SHEET_TOKEN,
}

exercises = exercise_data["exercises"]

for exercise in exercises:
    sheety_parameters = {
        "workout": {"date": date,
                    "time": time,
                    "exercise": exercise["name"].title(),
                    "duration": exercise["duration_min"],
                    "calories": exercise["nf_calories"], }
    }

    sheets_response = requests.post(url=SHEET_ENDPOINT, json=sheety_parameters, headers=sheety_header)
    sheets_response.raise_for_status()
    print(sheets_response.json())
