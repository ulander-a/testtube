import os, json, datetime
from bson.objectid import ObjectId
from flask import Flask
from flask_pymongo import PyMongo

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, datetime.datetime):
            return str(o)
        return json.JSONEncoder.default(self, o)

# create the flask object
app = Flask(__name__)

# add mongo url to flask config, so that flask_pymongo can use it to make connection
# might want to change to use .env instead of os.environ?
app.config['MONGO_URI'] = os.environ.get('DB')
mongo = PyMongo(app)

# use the modified encoder class to handle ObjectId & datetime object while jsonifying the response.
app.json_encoder = JSONEncoder

import modules.app.controllers