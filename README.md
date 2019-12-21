# Wheelchair API to detect fall and control the wheelchair


## Python Package Dependencies
1. alembic
2. Flask
3. Flask-Restful
4. SQLAlchemy
5. Flask-SQLAlchemy
6. Flask-Migrate
7. Flask-Script
8. requests
9. idna
10. urllib3 


## Introduction
In this project an API for wheelchair has been implemented. The target of the API is to get different information of the wheelchair. The information is given and recieved in json format.


## Motivation
The project is made for the my Academic thesis - "Secured wheelchair in IoT Environment"


## Features
* Fall detection using Accelerometer data (Used threshold technique)
* Control Wheelchair


## Quick start running the project
1. `git clone https://github.com/asif001/wheelchair-api.git`
2. Create python virtual environment with python-3.7.3
3. Install required python dependencies into your python virtual environment using `pip install -r requirements.txt`
4. Comment out cloud config section and uncomment local config section in `app.py` to run locally
5. `python app.py db upgrade`
6. `python app.py runserver`
7. Go to `http://127.0.0.1:5000/<params>` to get data for given params. The list of params are given below


### Params
* All data are sent and received in json format
1. status -- To send and receive whhelchair status
* POST: {"Accelerometer": accelerometer_data}
* GET: {"Accelerometer": .. , "FallStatus": ..}

2. direction -- Control wheelchair in different direction
* POST: {"direction": direction_to_go}
* GET: {"direction": ..}

3. trigger -- Trigger when a fall is detected
* POST: {"isTriggered": boolean_trigger_data}
* GET: {"isTriggered": ..}

4. restart -- Reset all values to default
* GET: {"isTriggered": .. , "fall_status": .., "Accelerometer": ..}

## Contributing
The main reason to publish something open source, is that anyone can just jump in and start contributing to my project.
So If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.


## Author
Asifur Rahman
asifurarahman@gmail.com
Student at Department of Computer Science and Engineering
Khulna University of Engineering & Technology, Khulna
Bangladesh