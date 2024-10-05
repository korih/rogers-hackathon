import os
import requests
import unittest
from unittest.mock import patch

class TestSimSwap(unittest.TestCase):
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
	
	def test_sim_swap(self):
		url = self.base_url + "/api/rapid/v0/simswap/check"
		response = requests.post(url, headers=self.headers, json=self.data)
		print("Sim Swap Response:")
		print(response)

		self.assertEqual(response.status_code, 200, "API call failed with status code other than 200")

		response_json = response.json()
		self.assertIn('status', response_json, "Response JSON does not contain 'status'")
	

if __name__ == "__main__":
	unittest.main
