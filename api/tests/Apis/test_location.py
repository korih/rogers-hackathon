import requests
import unittest
import os

class TestLocation(unittest.TestCase):
    ACCESS_TOKEN = os.getenv('BEARER')
    PHONE_NUMBER = os.getenv('PHONE_NUMBER')

    def TestLocation(self): 
        url = "https://pplx.azurewebsites.net/api/rapid/v0/location-verification/verify"
        
        headers = {
            "Authorization": f"Bearer {self.ACCESS_TOKEN}",
            "Cache-Control": "no-cache",
            "accept": "application/json",
            "Content-Type": "application/json"
        }
        
        data = {
            "device": {
                "phoneNumber": f"{self.PHONE_NUMBER}"
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
        print(f"hello: {self.ACCESS_TOKEN}")
        print(response.json())


if __name__ == "__main__":
    unittest.main()
