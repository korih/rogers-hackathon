import requests
import os
from dotenv import load_dotenv

load_dotenv();

ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
PHONE_NUMBER = os.getenv('PHONE_NUMBER')

url = "https://pplx.azurewebsites.net/api/rapid/v0/location-verification/verify"

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Cache-Control": "no-cache",
    "accept": "application/json",
    "Content-Type": "application/json"
}

data = {
    "device": {
        "phoneNumber": f"{PHONE_NUMBER}"
    },
    "area": {
        "type": "Circle",
        "location": {
            "latitude": 50.735851,
            "longitude": 7.10066
        },
        "accuracy": 50
    }
}

response = requests.post(url, headers=headers, json=data)

print(response.status_code)
print(f"hello: {ACCESS_TOKEN}")
print(response.json())

