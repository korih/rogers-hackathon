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

# curl -X POST "https://pplx.azurewebsites.net/api/rapid/v0/numberVerification/verify" \
#         -H "Authorization: Bearer bca7ba" \
#         -H "Cache-Control: no-cache" \
#         -H "accept: application/json" \
#         -H "Content-Type: application/json" \
#         -d '{
#           "phoneNumber": "14372197463"
#         }'
# {"status":200,"method":"POST","endpoint":"numberVerification","api":"verify","accessToken":"Bearer bca7ba","phoneNumber":"14372197463","message":"numberVerification request successful","datetime":"2024-10-05T00:33:53.441Z","cell":{"phoneNumber":"14372197463","name":"team 2","message":"Hi","accessToken":"Bearer bca7ba"},"device":{},"area":{},"devicePhoneNumberVerified":true,"devicePhoneNumber":"14372197463"}