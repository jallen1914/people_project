#app/__init__.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
from flask import request

#Find relative path to the DB
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "people.db"))

#Initialize app
app = Flask(__name__)

#Load views
#from app import models

#Load config
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

#Initializing DB
db = SQLAlchemy(app)

#Main Page
@app.route('/', methods=["GET", "POST"])
def index():
    if request.form:
        people = People(name=request.form.get(["name","phone", "city", "state"]))
        db.session.add(people)
        db.session.commit()
        #print(request.form)
    return render_template("index.html")


class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"People('{self.name}','{self.phone}','{self.city}','{self.state}')"
