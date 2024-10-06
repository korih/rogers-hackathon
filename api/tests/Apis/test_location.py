import requests
import unittest
import json
import os

from dotenv import load_dotenv
load_dotenv()

class TestLocation(unittest.TestCase):
    ACCESS_TOKEN = os.getenv('BEARER')
    PHONE_NUMBER = os.getenv('PHONE_NUMBER')

    def test_basic_api_call(self): 
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

        self.assertEqual(response.status_code, 200)
        
        actual_response = response.json()

        self.assertEqual(actual_response['status'], 200)
        self.assertEqual(actual_response['cell']['phoneNumber'], self.PHONE_NUMBER)
        self.assertEqual(actual_response['verificationResult'], False, "Should be false as both coordinates are incorrect")
        

    def test_basic_api_call_wrong_number(self): 
        url = "https://pplx.azurewebsites.net/api/rapid/v0/location-verification/verify"
        
        headers = {
            "Authorization": f"Bearer {self.ACCESS_TOKEN}",
            "Cache-Control": "no-cache",
            "accept": "application/json",
            "Content-Type": "application/json"
        }
        
        data = {
            "device": {
                "phoneNumber": "11231231234"
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

        self.assertEqual(response.status_code, 200)
        
        actual_response = response.json()

        self.assertEqual(actual_response['status'], 401)
        self.assertEqual(actual_response['message'], "Please provide a valid consented phoneNumber")


    def test_correct_coordinate(self): 
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
                    "latitude": 49.261177,
                    "longitude": -123.249161
                },
                "accuracy": 12000
            }
        }
        
        response = requests.post(url, headers=headers, json=data)

        self.assertEqual(response.status_code, 200)
        
        actual_response = response.json()

        self.assertEqual(actual_response['status'], 200)
        self.assertEqual(actual_response['message'], "location-verification request successful")
        self.assertEqual(actual_response['verificationResult'], True, "Should pass")


    def test_coordinate_accuracy_latitude(self): 
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
                    "latitude": 1,
                    "longitude": -123.249161
                },
                "accuracy": 50
            }
        }
        
        response = requests.post(url, headers=headers, json=data)

        self.assertEqual(response.status_code, 200)
        
        actual_response = response.json()

        self.assertEqual(actual_response['status'], 200)
        self.assertEqual(actual_response['message'], "location-verification request successful")
        self.assertEqual(actual_response['verificationResult'], False, "Latitude Accuracy should fail")

    def test_coordinate_accuracy_longitude(self): 
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
                    "latitude": 49.261177,
                    "longitude": 123.249161
                },
                "accuracy": 50
            }
        }
        
        response = requests.post(url, headers=headers, json=data)

        self.assertEqual(response.status_code, 200)
        
        actual_response = response.json()

        self.assertEqual(actual_response['status'], 200)
        self.assertEqual(actual_response['message'], "location-verification request successful")
        self.assertEqual(actual_response['verificationResult'], False, "Should be false as this is incoorect")

if __name__ == "__main__":
    unittest.main()
