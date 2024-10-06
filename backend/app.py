from flask import Flask
import requests
import json
import time

ROGERS_URL = "https://pplx.azurewebsites.net/api/rapid/v0"


def get_rogers_headers(access_token):
    return {"Authorization": "Bearer " + access_token,
            "Cache-Control": "no-cache",
            "accept": "application/json",
            "Content-Type": "application/json"}


users_list = [
               {
                 "phone_number": "14372197463",
                 "token": "bca7ba",
                 "latitude": "49.2616",
                 "longitude": "-123.248854",
                 "accuracy": "0.0003"
                }
              ]

active_qr_phone_numbers = set()
scanned_qr_phone_numbers = set()
verification_results = []


def verify(phone_number):
    logfile = open("eventlog.txt", "a")
    # find user associated with user in our database
    user = None
    for u in users_list:
        if u["phone_number"] == phone_number:
            user = u

    if user is None:
        return

    # Check that the number user accesses from is the phone number
    # associated with the Rogers user
    data = json.dumps({"phoneNumber": phone_number})
    num_verify_res = requests.post(ROGERS_URL + "/numberVerification/verify",
                                   data=data,
                                   headers=get_rogers_headers(user["token"]))

    logfile.write("\n***** NEW NUMBER VERIFY REQUEST - "
                  + time.ctime() + " *****\n")
    logfile.write(data)
    logfile.write("\n----- NUMBER VERIFY RESPONSE -----\n")
    logfile.write(num_verify_res.text)

    if (not num_verify_res.json()["devicePhoneNumberVerified"]):
        verification_results.append({"phone_number": phone_number,
                                     "result": "numverify fail"})
        logfile.close()
        return

    # Check that the SIM was not swapped in last 240 hours
    sim_verify_res = requests.post(ROGERS_URL + "/simswap/check",
                                   data=data,
                                   headers=get_rogers_headers(user["token"]))

    logfile.write("\n***** NEW SIM SWAP VERIFY REQUEST - "
                  + time.ctime() + " *****\n")
    logfile.write(data)
    logfile.write("\n----- SIM SWAP VERIFY RESPONSE -----\n")
    logfile.write(sim_verify_res.text)

    if (sim_verify_res.json()["swapped"]):
        verification_results.append({"phone_number": phone_number,
                                     "result": "simswap fail"})
        logfile.close()
        return

    data = json.dumps({"device": {"phoneNumber": phone_number},
                       "area": {
                           "type": "Circle",
                           "location": {
                               "latitude": user["latitude"],
                               "longitude": user["longitude"]
                           },
                           "accuracy": user["accuracy"]
                       }})

    loc_verify_res = requests.post(ROGERS_URL + "/location-verification/verify",
                                   data=data,
                                   headers=get_rogers_headers(user["token"]))

    logfile.write("\n***** NEW LOCATION VERIFY REQUEST - "
                  + time.ctime() + " *****\n")
    logfile.write(data)
    logfile.write("\n----- LOCATION VERIFY RESPONSE -----\n")
    logfile.write(sim_verify_res.text)

    if (not loc_verify_res.json()["verificationResult"]):
        verification_results.append({"phone_number": phone_number,
                                     "result": "location fail"})
        logfile.close()
        return

    verification_results.append({"phone_number": phone_number,
                                 "result": "pass"})
    logfile.close()


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    @app.route("/", methods=["GET"])
    def root():
        return "I am /backend"

    @app.route("/api/generate_qr/<phone_number>", methods=["GET"])
    def generate_qr(phone_number):
        for u in users_list:
            if u["phone_number"] == phone_number:
                active_qr_phone_numbers.add(phone_number)
                return "https://rh.drismir.ca/api/phone_scan/"+phone_number
        return "failed"

    @app.route("/api/phone_scan/<phone_number>")
    def phone_scan(phone_number):
        if phone_number in active_qr_phone_numbers:
            active_qr_phone_numbers.remove(phone_number)
            scanned_qr_phone_numbers.add(phone_number)
            verify(phone_number)
            return "done"
        else:
            return "failed"

    @app.route("/api/qr_scanned/<phone_number>")
    def qr_scanned(phone_number):
        if phone_number in scanned_qr_phone_numbers:
            scanned_qr_phone_numbers.remove(phone_number)
            return "done"
        else:
            return "waiting"

    @app.route("/api/checks/<phone_number>")
    def checks(phone_number):
        for r in verification_results:
            if r["phone_number"] == phone_number:
                verification_results.remove(r)
                return r["result"]
        return "noresult"

    @app.route("/api/admin/<phone_number>")
    def admin(phone_number):
        for u in users_list:
            if u["phone_number"] == phone_number:
                return u
        return "failed"

    @app.route("/api/admin/<phone_number>/<latitude>/<longitude>/<accuracy>")
    def admin_change(phone_number, latitude, longitude, accuracy):
        for u in users_list:
            if u["phone_number"] == phone_number:
                u["latitude"] = latitude
                u["longitude"] = longitude
                u["accuracy"] = accuracy
                return u
        return "failed"

    return app

app = create_app()