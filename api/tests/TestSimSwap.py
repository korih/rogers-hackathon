import os
import requests

def TestSimSwap():
	url = "https://pplx.azurewebsites.net/api/rapid/v0/numberVerification/verify"
	headers = {
		"Authorization": f"Bearer {os.getenv('BEARER')}",
		"Cache-Control": "no-cache",
		"accept": "application/json",
		"Content-Type": "application/json"
	}
	data = {
		"phoneNumber": f"{os.getenv('PHONE_NUMBER')}"
	}

	response = requests.post(url, headers=headers, json=data)
	print(response.json())

if __name__ == "__main__":
	TestSimSwap()