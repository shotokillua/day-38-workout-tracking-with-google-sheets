import requests
from datetime import datetime


APP_ID = "***"

APP_KEY = "***"

USERNAME = "***"

PASSWORD = "***"

TOKEN = "***"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

parameters = {
    "query": input("Tell me which exercise you did: "),
    "gender": "male",
    "weight_kg": 77,
    "height_cm": 178,
    "age": 24,
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
result = response.json()

######################## START OF STEP 4 SOLUTION #########################################
today = datetime.now()

bearer_headers = {
"Authorization": f"Bearer {TOKEN}"
}

sheety_endpoint = "https://api.sheety.co/cb445a9d042d09272a19cd2dfcf3482e/myWorkoutsTmt/workouts"

for exercise in result["exercises"]:
    workout_inputs = {
        "workout": {
            "date": today.strftime("%m/%d/%Y"),
            "time": today.strftime("%H:%M:%S"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

# new_sheety_response = requests.post(url=sheety_endpoint, json=workout_inputs)
# print(new_sheety_response.text)


# #Basic Authentication
# sheet_response = requests.post(
#   sheety_endpoint_endpoint,
#   json=workout_inputs,
#   auth=(
#       YOUR USERNAME,
#       YOUR PASSWORD,
#   )
# )

#Bearer Token Authentication
# bearer_headers = {
# "Authorization": f"Bearer {TOKEN}"
# }
sheet_response = requests.post(
    sheety_endpoint,
    json=workout_inputs,
    headers=bearer_headers
)

print(sheet_response.text)