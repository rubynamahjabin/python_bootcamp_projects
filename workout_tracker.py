import requests
from datetime import datetime
import os
import sys

# Your personal data. Used by Nutritionix to calculate calories.
GENDER = "male"
WEIGHT_KG = 84
HEIGHT_CM = 180
AGE = 32

# --- Check for Environment Variables ---
required_vars = [
    "ENV_NIX_APP_ID",
    "ENV_NIX_API_KEY",
    "ENV_SHEETY_ENDPOINT",
    "ENV_SHEETY_USERNAME",
    "ENV_SHEETY_PASSWORD",
]

missing_vars = [var for var in required_vars if var not in os.environ]

if missing_vars:
    print("❌ Missing environment variables:")
    for var in missing_vars:
        print(f"   - {var}")
    print("\nPlease set these environment variables before running the script.")
    sys.exit(1)  # Stop program here

# Nutritionix APP ID and API Key
APP_ID = os.environ["ENV_NIX_APP_ID"]
API_KEY = os.environ["ENV_NIX_API_KEY"]

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

# --- User Input ---
exercise_text = input("Tell me which exercises you did: ")

# Nutritionix API Call
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(f"Nutritionix API call: \n {result} \n")

# Adding date and time
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

# Sheety Project API
GOOGLE_SHEET_NAME = "workout"
sheet_endpoint = os.environ["ENV_SHEETY_ENDPOINT"]

# --- Save to Google Sheet via Sheety ---
for exercise in result.get("exercises", []):
    sheet_inputs = {
        GOOGLE_SHEET_NAME: {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        auth=(
            os.environ["ENV_SHEETY_USERNAME"],
            os.environ["ENV_SHEETY_PASSWORD"],
        )
    )

    print(f"Sheety Response: \n {sheet_response.text}")