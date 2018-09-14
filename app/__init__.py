#app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy



#Initialize app
app = Flask(__name__, instance_relative_config=True)
#db = SQLAlchemy(app)

#Load views
from app import views, models

#Load config file
app.config.from_object('config')
