"""Simulator handler for Mastercard Flight Delay Pass.

Mirrors the live sandbox endpoints under ``/loyalty/flight-delay-pass`` so
local development can run without portal credentials.
"""
import uuid

from flask import jsonify, request

from simulator.datastore import store

API = "flight_delay_pass"


def register(bp):
    @bp.route("/flight_delay_pass/eligibility-checks", methods=["GET"])
    def eligibility_check():
        store.lazy_load(API)
        carrier = request.args.get("carrierCode", "").upper()
        flight  = request.args.get("flightNumber", "")
        dep     = request.args.get("departureAirport", "").upper()
        arr     = request.args.get("arrivalAirport", "").upper()
        date    = request.args.get("departureDate", "")

        eligibles = store.list(API, "eligibility")
        match = None
        for row in eligibles:
            if (row.get("carrierCode", "").upper() == carrier and
                str(row.get("flightNumber", "")) == str(flight) and
                row.get("departureAirport", "").upper() == dep and
                row.get("arrivalAirport", "").upper() == arr):
                match = row
                break
        if match is None and eligibles:
            # Fall back to the first eligible record so the UI always has data.
            match = dict(eligibles[0])
            match["carrierCode"] = carrier or match.get("carrierCode")
            match["flightNumber"] = flight or match.get("flightNumber")
            match["departureAirport"] = dep or match.get("departureAirport")
            match["arrivalAirport"] = arr or match.get("arrivalAirport")
            match["departureDate"] = date or match.get("departureDate")
        if match is None:
            return jsonify({"eligible": False, "reason": "No matching flight."}), 404
        return jsonify(match)

    @bp.route("/flight_delay_pass/registrations", methods=["POST"])
    def create_registration():
        store.lazy_load(API)
        body = request.get_json(silent=True) or {}
        reg_id = f"FDP-{uuid.uuid4().hex[:10].upper()}"
        record = {
            "id": reg_id,
            "registrationId": reg_id,
            "status": "REGISTERED",
            "carrierCode": body.get("carrierCode"),
            "flightNumber": body.get("flightNumber"),
            "departureDate": body.get("departureDate"),
            "departureAirport": body.get("departureAirport"),
            "arrivalAirport": body.get("arrivalAirport"),
            "passenger": {
                "firstName": body.get("firstName"),
                "lastName":  body.get("lastName"),
                "email":     body.get("email"),
                "phoneNumber": body.get("phoneNumber"),
            },
            "createdAt": "2026-01-01T00:00:00Z",
        }
        store.add(API, "registrations", record)
        return jsonify(record), 201

    @bp.route("/flight_delay_pass/registrations/<reg_id>", methods=["GET"])
    def get_registration(reg_id):
        store.lazy_load(API)
        rows = store.list(API, "registrations")
        for row in rows:
            if str(row.get("registrationId") or row.get("id")) == reg_id:
                return jsonify(row)
        return jsonify({"Errors": {"Error": [{"Source": "Flight Delay Pass", "ReasonCode": "NOT_FOUND",
                                              "Description": f"No registration with id {reg_id}"}]}}), 404

    @bp.route("/flight_delay_pass/registrations/<reg_id>", methods=["PUT"])
    def update_registration(reg_id):
        store.lazy_load(API)
        rows = store.list(API, "registrations")
        body = request.get_json(silent=True) or {}
        for row in rows:
            if str(row.get("registrationId") or row.get("id")) == reg_id:
                passenger = dict(row.get("passenger") or {})
                for k in ("firstName", "lastName", "email", "phoneNumber"):
                    if body.get(k):
                        passenger[k] = body[k]
                row["passenger"] = passenger
                row["status"] = "UPDATED"
                return jsonify(row)
        return jsonify({"Errors": {"Error": [{"Source": "Flight Delay Pass", "ReasonCode": "NOT_FOUND",
                                              "Description": f"No registration with id {reg_id}"}]}}), 404

    @bp.route("/flight_delay_pass/registrations/<reg_id>", methods=["DELETE"])
    def cancel_registration(reg_id):
        store.lazy_load(API)
        rows = store.list(API, "registrations")
        for row in rows:
            if str(row.get("registrationId") or row.get("id")) == reg_id:
                row["status"] = "CANCELLED"
                return jsonify({"registrationId": reg_id, "status": "CANCELLED"})
        return jsonify({"Errors": {"Error": [{"Source": "Flight Delay Pass", "ReasonCode": "NOT_FOUND",
                                              "Description": f"No registration with id {reg_id}"}]}}), 404
