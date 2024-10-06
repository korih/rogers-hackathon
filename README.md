# rogers-hackathon
<img width="1000" alt="Screenshot 2024-10-06 at 14 17 39" src="https://github.com/user-attachments/assets/f7877b44-b0bd-4c46-b87b-9af6c2d3682d">

## API Getting Started:
These are the tests for the api, verifying that they work.

Place a .env at api/.env. It should have:
```
BEARER=<bearer_token>

PHONE_NUMBER=<phone_number>
```

To run tests `python api/RunTests.py`

## Backend
Written in Flask, it will verify the phone number, generate a QR code for the phone which will let the phone send a request to the apis for the phone number and bearer token which will verify the computers request.

## Frontend
Written with React, the front end will call the backend server and be authenticated by the backend. This is a demonstration of the general user flow.
