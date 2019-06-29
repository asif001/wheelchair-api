from flask import Flask
from flask_restful import Api

from resourses.todo import Status,Trigger

app = Flask(__name__)
api = Api(app)

api.add_resource(Status, "/status/")
api.add_resource(Trigger, "/trigger/")


if __name__ == '__main__':
    app.run()
