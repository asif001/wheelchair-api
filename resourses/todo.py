from flask import request, jsonify
from flask_restful import Resource


class Status(Resource):
    values = {'acl_val': 0.0, 'fall_status': 0}

    def get(self):
        if self.values['fall_status'] == 0:
            if 110 <= self.values['acl_val'] <= 250:
                self.values['fall_status'] = 1
                data = {
                    "Accelerometer": self.values['acl_val'],
                    "FallStatus": self.values['fall_status'],
                }
                resp = jsonify(data)
                resp.status_code = 200
                return resp
            else:
                self.values['fall_status'] = 0
                data = {
                    "Accelerometer": self.values['acl_val'],
                    "FallStatus": self.values['fall_status'],
                }
                resp = jsonify(data)
                resp.status_code = 200
                return resp
        else:
            data = {
                "Accelerometer": self.values['acl_val'],
                "FallStatus": self.values['fall_status'],
            }
            resp = jsonify(data)
            resp.status_code = 200
            return resp

    def post(self):
        self.values['acl_val'] = float(request.form["Accelerometer"])


class Trigger(Resource):
    values = {'isTriggered': 0}

    def post(self):
        self.values['isTriggered'] = int(request.form["isTriggered"])

    def get(self):
        data = {
            "isTriggered": self.values['isTriggered'],
        }
        resp = jsonify(data)
        resp.status_code = 200
        return resp
