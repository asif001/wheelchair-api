from flask import request, jsonify
from flask_restful import Resource


class Setup(Resource):
    def get(self):
        from app import db, Values
        db.session.add(Values(id=1, fall_status=0,
                              username="admin", password="12345678",
                              Accelerometer_x=0.0, Accelerometer_y=0.0,
                              Accelerometer_z=0.0,
                              isTriggered=0, direction="front"))
        db.session.commit()
        data = {
            "setup": 1,
        }
        resp = jsonify(data)
        resp.status_code = 200
        return resp


class User(Resource):

    def get(self):
        from app import db, Values
        username = str(request.args.get("username"))
        password = str(request.args.get("password"))
        print(username, password)
        values = Values.query.filter_by(username=username, password=password).first()
        if values is None:
            print(0)
            data = {
                "exist": 0,
            }
            resp = jsonify(data)
            resp.status_code = 200
            return resp
        else:
            print(1)
            data = {
                "exist": 1,
            }
            resp = jsonify(data)
            resp.status_code = 200
            return resp


class Status(Resource):

    def get(self):
        from app import db, Values
        username = request.args.get("username")
        password = request.args.get("password")
        values = Values.query.filter_by(username=username, password=password).first()

        if values is not None:
            if int(values.fall_status) == 0:
                if 110 <= float(values.Accelerometer_x) <= 250:
                    values.fall_status = 1
                    data = {
                        "Accelerometer_x": float(values.Accelerometer_x),
                        "Accelerometer_y": float(values.Accelerometer_y),
                        "Accelerometer_z": float(values.Accelerometer_z),
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
                        "Accelerometer_x": float(values.Accelerometer_x),
                        "Accelerometer_y": float(values.Accelerometer_y),
                        "Accelerometer_z": float(values.Accelerometer_z),
                        "FallStatus": int(values.fall_status),
                    }
                    resp = jsonify(data)
                    resp.status_code = 200
                    db.session.add(values)
                    db.session.commit()
                    return resp
            else:
                data = {
                    "Accelerometer_x": float(values.Accelerometer_x),
                    "Accelerometer_y": float(values.Accelerometer_y),
                    "Accelerometer_z": float(values.Accelerometer_z),
                    "FallStatus": int(values.fall_status),
                }
                resp = jsonify(data)
                resp.status_code = 200
                return resp
        else:
            db.session.add(Values(fall_status=0,
                                  username=username, password=password,
                                  Accelerometer_x=0, Accelerometer_y=0, Accelerometer_z=0,
                                  isTriggered=0, direction="front"))
            db.session.commit()
            data = {
                "Accelerometer_x": 0,
                "Accelerometer_y": 0,
                "Accelerometer_z": 0,
                "FallStatus": 0,
            }
            resp = jsonify(data)
            resp.status_code = 200
            return resp

    def post(self):
        from app import db, Values
        username = request.form["username"]
        password = request.form["password"]
        values = Values.query.filter_by(username=username, password=password).first()

        if values is not None:
            values.Accelerometer_x = float(float(request.form["Accelerometer_x"]))
            values.Accelerometer_y = float(float(request.form["Accelerometer_y"]))
            values.Accelerometer_z = float(float(request.form["Accelerometer_z"]))
            db.session.add(values)
            db.session.commit()
        else:
            db.session.add(Values(fall_status=0,
                                  username=username, password=password,
                                  Accelerometer_x=float(request.form["Accelerometer_x"]),
                                  Accelerometer_y=float(request.form["Accelerometer_y"]),
                                  Accelerometer_z=float(request.form["Accelerometer_z"]),
                                  isTriggered=0, direction="front"))
            db.session.commit()


class Direction(Resource):

    def post(self):
        from app import db, Values
        username = request.form["username"]
        password = request.form["password"]
        values = Values.query.filter_by(username=username, password=password).first()

        if values is not None:
            values.direction = str(request.form["direction"])
            print(str(request.form["direction"]))
            db.session.add(values)
            db.session.commit()
        else:
            db.session.add(
                Values(fall_status=0, Accelerometer_x=0,
                       username=username, password=password,
                       Accelerometer_y=0, Accelerometer_z=0, isTriggered=0,
                       direction=str(request.form["direction"])))
            db.session.commit()

    def get(self):
        from app import db, Values
        username = request.args.get("username")
        password = request.args.get("password")
        values = Values.query.filter_by(username=username, password=password).first()

        if values is not None:
            data = {
                "direction": str(values.direction)
            }
            resp = jsonify(data)
            resp.status_code = 200
            return resp
        else:
            db.session.add(
                Values(fall_status=0, Accelerometer_x=0,
                       username=username, password=password,
                       Accelerometer_y=0, Accelerometer_z=0, isTriggered=0,
                       direction="front"))
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
                Values(id=1, fall_status=0, Accelerometer_x=0,Accelerometer_y=0,Accelerometer_z=0, isTriggered=int(request.form["isTriggered"]), direction="front"))
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
                Values(id=1, fall_status=0, Accelerometer_x=0,Accelerometer_y=0,Accelerometer_z=0, isTriggered=0, direction="front"))
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
            values.Accelerometer_x = 0
            values.Accelerometer_y = 0
            values.Accelerometer_z = 0
            db.session.add(values)
            db.session.commit()
            data = {
                "isTriggered": 0,
                "fall_status": 0,
                "Accelerometer_x": 0,
                "Accelerometer_y": 0,
                "Accelerometer_z": 0,
            }
            resp = jsonify(data)
            resp.status_code = 200
            return resp
        else:
            db.session.add(
                Values(id=1, fall_status=0, Accelerometer_x=0,Accelerometer_y=0,Accelerometer_z=0, isTriggered=0, direction="front"))
            db.session.commit()
            data = {
                "isTriggered": 0,
                "fall_status": 0,
                "Accelerometer_x": 0,
                "Accelerometer_y": 0,
                "Accelerometer_z": 0,
            }
            resp = jsonify(data)
            resp.status_code = 200
            return resp
