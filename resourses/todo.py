from flask import request, jsonify
from flask_restful import Resource

acl_val = 0
fall_status = 0
isTriggered = 0


class Status(Resource):
    def get(self):
        global fall_status, acl_val, isTriggered
        if fall_status == 0:
            if 110 <= acl_val <= 250:
                fall_status = 1
                data = {
                    "Accelerometer": acl_val,
                    "FallStatus": fall_status,
                }
                resp = jsonify(data)
                resp.status_code = 200
                return resp
            else:
                fall_status = 0
                data = {
                    "Accelerometer": acl_val,
                    "FallStatus": fall_status,
                }
                resp = jsonify(data)
                resp.status_code = 200
                return resp
        else:
            data = {
                "Accelerometer": acl_val,
                "FallStatus": fall_status,
            }
            resp = jsonify(data)
            resp.status_code = 200
            return resp

    def post(self):
        global acl_val
        acl_val = float(request.form["Accelerometer"])


class Trigger(Resource):
    def post(self):
        global isTriggered
        print(int(request.form["isTriggered"]))
        isTriggered = int(request.form["isTriggered"])

    def get(self):
        global isTriggered
        data = {
            "isTriggered": isTriggered,
        }
        resp = jsonify(data)
        resp.status_code = 200
        return resp
