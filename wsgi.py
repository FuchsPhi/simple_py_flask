from __future__ import print_function

import os

from flask import Flask, send_from_directory
from flask_restful import Resource, Api, reqparse, abort
from flask_cors import CORS

import werkzeug
import json
from datetime import datetime


application = Flask(__name__)

cors = CORS(application, resources={r"*": {"origins": "*"}})
api = Api(application)

parser = reqparse.RequestParser()

# based on example https://flask-restful.readthedocs.io/en/0.3.5/quickstart.html#full-example
USERS = {
    "user1": {
        "name": "Nicholas",
        "age": 42,
        "occupation": "Network Engineer"
    },
    "user2": {
        "name": "Elvin",
        "age": 32,
        "occupation": "Doctor"
    },
    "user3": {
        "name": "Jass",
        "age": 22,
        "occupation": "Web Developer"
    }
}

class User(Resource):
    def abort_if_user_doesnt_exist(self, user_id):
        if user_id not in USERS:
            abort(404, message="User {} doesn't exist".format(user_id))

    def get(self, user_id):
        self.abort_if_user_doesnt_exist(user_id)
        return USERS[user_id], 200

    def put(self, user_id):
        parser.add_argument("name")
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        updated_user = {
            "name": args['name'],
            "age": args['age'],
            "occupation": args['occupation']
        }
        
        if not user_id in USERS:
            USERS[user_id] = updated_user
            return updated_user, 201
        else:
            USERS[user_id] = updated_user
            return updated_user, 200

    def delete(self, user_id):
        self.abort_if_user_doesnt_exist(user_id)
        del USERS[user_id]
        return '', 204
        
api.add_resource(User, "/users/<string:user_id>")

class Users(Resource):
    def get(self):
        return USERS

    def post(self):
        parser.add_argument("name")
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        user_id = int(max(USERS.keys()).lstrip('user')) + 1
        user_id = 'user%i' % user_id
        USERS[user_id] = {
            "name": args['name'],
            "age": args['age'],
            "occupation": args['occupation']
        }
        return USERS[user_id], 201

api.add_resource(Users, '/users')

class Info(Resource):
    description = {
        'id': 'flask-example',
        'displayName': 'Backend with Python and Flask using wsgi',
        'type': 'cluster',
    }

    def get(self):
        return self.description

api.add_resource(Info, '/info/')

class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()

        return json.JSONEncoder.default(self, o)

@application.route('/')
def index():
    return 'Welcome to an example Python flask backend application.'

# application.run(debug=True)