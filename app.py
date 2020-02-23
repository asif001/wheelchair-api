from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_restful import Api
from flask_cors import CORS
from resourses.todo import Status, Trigger, Restart, Direction, User, Setup
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
## local config ##
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'wheelchair-api.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
## local config ##
## cloud config ##
#app.config.from_mapping(SECRET_KEY=os.environ.get('SECRET_KEY') or 'dev_key',
                        #SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL') or
                        #'sqlite:///' + os.path.join(app.instance_path, 'wheelchair-api.sqlite'),
                        #SQLALCHEMY_TRACK_MODIFICATIONS=False)
## cloud config ##

CORS(app)
api = Api(app)

api.add_resource(Status, "/status/")
api.add_resource(Trigger, "/trigger/")
api.add_resource(Restart, "/restart/")
api.add_resource(Direction, "/direction/")
api.add_resource(User, "/user/")
api.add_resource(Setup, "/setup/")

db = SQLAlchemy()
migrate = Migrate()


db.init_app(app)
migrate.init_app(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


class Values(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, default=0)
    username = db.Column(db.String, default="")
    password = db.Column(db.String, default="")
    fall_status = db.Column(db.Integer, default=0)
    Accelerometer_x = db.Column(db.Float, default=0.0)
    Accelerometer_y = db.Column(db.Float, default=0.0)
    Accelerometer_z = db.Column(db.Float, default=0.0)
    isTriggered = db.Column(db.Integer, default=0)
    direction = db.Column(db.String, default="front")

    def __repr__(self):
        return '<Name: {}>'.format(self.name)


if __name__ == '__main__':
    manager.run()
