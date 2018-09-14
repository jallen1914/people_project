#app/__init__.py
import os
from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

#Find relative path to the DB
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "people.db"))

#Initialize app
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config['SECRET_KEY'] = "random string"

#Initializing DB
db = SQLAlchemy(app)

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(50), nullable=False)

    def __init__(self, name, phone, city, state):
        self.name = name
        self.phone = phone
        self.city = city
        self.state = state

#Main Page
@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        #people = People(name=request.form.get(["name","phone", "city", "state"]))
        people = People(request.form["name"], request.form["phone"], request.form["city"], request.form["state"])
        db.session.add(people)
        db.session.commit()
        flash('Record was successfully added')
        #print(request.form)
    #people = People.query.all()
    return render_template("index.html")

    def __repr__(self):
        #return f"People('{self.name}','{self.phone}','{self.city}','{self.state}')"
        return f"People('{self.name}')"
