import os
import requests
import unittest
from unittest.mock import patch

from dotenv import load_dotenv
load_dotenv()

class TestNumberVerification(unittest.TestCase):
	ACCESS_TOKEN = os.getenv('BEARER')
	PHONE_NUMBER = os.getenv('PHONE_NUMBER')
	
	def setUp(self):
		self.base_url = "https://pplx.azurewebsites.net"
		self.headers = {
			"Authorization": f"Bearer {self.ACCESS_TOKEN}",
			"Cache-Control": "no-cache",
			"accept": "application/json",
			"Content-Type": "application/json"
		}
		self.data = {
			"phoneNumber": f"{self.PHONE_NUMBER}"
		}

	def test_phone_number(self):
		url = self.base_url + "/api/rapid/v0/numberVerification/verify"
		response = requests.post(url, headers=self.headers, json=self.data)

		self.assertEqual(response.status_code, 200)

		print(os.getenv('BEARER'))
		actual_response = response.json()

		self.assertEqual(actual_response["status"], 200)

		self.assertEqual(actual_response['cell']['phoneNumber'], os.getenv('PHONE_NUMBER'))


if __name__ == "__main__":
	unittest.main
