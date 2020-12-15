import os

from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from flask_cors import CORS

# Init app
app = Flask(__name__)

# Set Cors to allows cross origin : query from the api client on localhost
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


# Our SQL Alchemy db path
basedir = os.path.abspath(os.path.dirname(__file__))

# Database config
# app.config["SQLALCHEMY_ECHO"] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Set alchemy track modifications to false // disable warning in the console

# Init db
db = SQLAlchemy(app)

# Init Marshmallow to wrap our db using the configs we just set
ma = Marshmallow(app)

