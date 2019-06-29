from flask import Flask
from flask_restful import Api

from resourses.todo import Todo

app = Flask(__name__)
api = Api(app)

api.add_resource(Todo, "/todo/<int:id>")


if __name__ == '__main__':
    app.run()
