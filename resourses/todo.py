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
            db.session.add(Values(id=1, fall_status=0, Accelerometer=0, isTriggered=0, direction="front"))
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
            db.session.add(Values(id=1, fall_status=0, Accelerometer=float(request.form["Accelerometer"]), isTriggered=0, direction="front"))
            db.session.commit()


class Direction(Resource):

    def post(self):
        from app import db, Values
        values = Values.query.get(1)
        if values is not None:
            values.direction = str(request.form["direction"])
            db.session.add(values)
            db.session.commit()
        else:
            db.session.add(
                Values(id=1, fall_status=0, Accelerometer=0, isTriggered=0, direction=str(request.form["direction"])))
            db.session.commit()

    def get(self):
        from app import db, Values
        values = Values.query.get(1)
        if values is not None:
            data = {
                "direction": str(values.direction)
            }
            resp = jsonify(data)
            resp.status_code = 200
            return resp
        else:
            db.session.add(
                Values(id=1, fall_status=0, Accelerometer=0, isTriggered=0, direction="front"))
            db.session.commit()
            data = {
                "direction": "front"
            }
            resp = jsonify(data)
            resp.status_code = 200
            return resp


class Trigger(Resource):

    def post(self):
        from app import db, Values
        values = Values.query.get(1)
        if values is not None:
            values.isTriggered = int(request.form["isTriggered"])
            db.session.add(values)
            db.session.commit()
        else:
            db.session.add(
                Values(id=1, fall_status=0, Accelerometer=0, isTriggered=int(request.form["isTriggered"]), direction="front"))
            db.session.commit()

    def get(self):
        from app import db, Values
        values = Values.query.get(1)
        if values is not None:
            data = {
                "isTriggered": int(values.isTriggered),
            }
            resp = jsonify(data)
            resp.status_code = 200
            return resp
        else:
            db.session.add(
                Values(id=1, fall_status=0, Accelerometer=0, isTriggered=0, direction="front"))
            db.session.commit()
            data = {
                "isTriggered": 0,
            }
            resp = jsonify(data)
            resp.status_code = 200
            return resp


class Restart(Resource):

    def get(self):
        from app import db, Values
        values = Values.query.get(1)
        if values is not None:
            values.isTriggered = 0
            values.fall_status = 0
            values.Accelerometer = 0
            db.session.add(values)
            db.session.commit()
            data = {
                "isTriggered": 0,
                "fall_status": 0,
                "Accelerometer": 0,
            }
            resp = jsonify(data)
            resp.status_code = 200
            return resp
        else:
            db.session.add(
                Values(id=1, fall_status=0, Accelerometer=0, isTriggered=0, direction="front"))
            db.session.commit()
            data = {
                "isTriggered": 0,
                "fall_status": 0,
                "Accelerometer": 0,
            }
            resp = jsonify(data)
            resp.status_code = 200
            return resp
