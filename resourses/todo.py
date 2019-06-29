from flask import request, jsonify
from flask_restful import Resource


class Status(Resource):

    def get(self):
        from app import db, Values
        values = Values.query.get(1)

        if values is not None:
            if int(values.fall_status) == 0:
                if 110 <= float(values.Accelerometer) <= 250:
                    values.fall_status = 1
                    data = {
                        "Accelerometer": float(values.Accelerometer),
                        "FallStatus": int(values.fall_status),
                    }
                    resp = jsonify(data)
                    resp.status_code = 200
                    db.session.add(values)
                    db.session.commit()
                    return resp
                else:
                    values.fall_status = 0
                    data = {
                        "Accelerometer": float(values.Accelerometer),
                        "FallStatus": int(values.fall_status),
                    }
                    resp = jsonify(data)
                    resp.status_code = 200
                    db.session.add(values)
                    db.session.commit()
                    return resp
            else:
                data = {
                    "Accelerometer": float(values.Accelerometer),
                    "FallStatus": int(values.fall_status),
                }
                resp = jsonify(data)
                resp.status_code = 200
                return resp
        else:
            db.session.add(Values(id=1, fall_status=0, Accelerometer=0, isTriggered=0))
            db.session.commit()
            data = {
                "Accelerometer": 0,
                "FallStatus": 0,
            }
            resp = jsonify(data)
            resp.status_code = 200
            return resp

    def post(self):
        from app import db, Values
        values = Values.query.get(1)

        if values is not None:
            values.Accelerometer = float(float(request.form["Accelerometer"]))
            db.session.add(values)
            db.session.commit()
        else:
            db.session.add(Values(id=1, fall_status=0, Accelerometer=float(request.form["Accelerometer"]), isTriggered=0))
            db.session.commit()


class Trigger(Resource):

    def post(self):
        from app import db, Values
        values = Values.query.get(1)
        values.isTriggered = int(request.form["isTriggered"])
        db.session.add(values)
        db.session.commit()

    def get(self):
        from app import db, Values
        values = Values.query.get(1)
        data = {
            "isTriggered": int(values.isTriggered),
        }
        resp = jsonify(data)
        resp.status_code = 200
        return resp
