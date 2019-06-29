from flask import request, jsonify
from flask_restful import Resource


values = {'acl_val': 0.0, 'fall_status': 0, 'isTriggered': 0}


class Status(Resource):
    def get(self):
        if values['fall_status'] == 0:
            if 110 <= values['acl_val'] <= 250:
                values['fall_status'] = 1
                data = {
                    "Accelerometer": values['acl_val'],
                    "FallStatus": values['fall_status'],
                }
                resp = jsonify(data)
                resp.status_code = 200
                return resp
            else:
                values['fall_status'] = 0
                data = {
                    "Accelerometer": values['acl_val'],
                    "FallStatus": values['fall_status'],
                }
                resp = jsonify(data)
                resp.status_code = 200
                return resp
        else:
            data = {
                "Accelerometer": values['acl_val'],
                "FallStatus": values['fall_status'],
            }
            resp = jsonify(data)
            resp.status_code = 200
            return resp

    def post(self):
        values['acl_val'] = float(request.form["Accelerometer"])


class Trigger(Resource):
    def post(self):
        values['isTriggered'] = int(request.form["isTriggered"])

    def get(self):
        data = {
            "isTriggered": values['isTriggered'],
        }
        resp = jsonify(data)
        resp.status_code = 200
        return resp
