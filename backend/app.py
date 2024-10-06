from flask import Flask, request, jsonify, Response

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
    # TODO: Do Rogers checks
    verification_results.append({"phone_number": phone_number,
                                 "result": "pass"})


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    @app.route("/api/generate_qr/<phone_number>", methods=["GET"])
    def generate_qr(phone_number):
        for u in users_list:
            if u["phone_number"] == phone_number:
                active_qr_phone_numbers.add(phone_number)
                return "http://localhost:5000/api/phone_scan/"+phone_number
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
