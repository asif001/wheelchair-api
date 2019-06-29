from flask import request
from flask_restful import Resource

acl_val = 0
fall_status = 0
isTriggered = "0"


class Status(Resource):
    def get(self):
        global fall_status, acl_val, isTriggered
        if isTriggered == "0":
            if 110 <= acl_val <= 250:
                fall_status = 1
                return {"Accelerometer": acl_val, "FallStatus": fall_status}
            else:
                fall_status = 0
                return {"Accelerometer": acl_val, "FallStatus": fall_status}
        else:
            return "Whhelchair is now in fall state. Please recover"


class Trigger(Resource):
    def post(self):
        global isTriggered
        isTriggered = request.form["isTriggered"]

    def get(self):
        global isTriggered
        return {"isTriggered": isTriggered}
