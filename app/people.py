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
        if not request.form["name"] or not request.form["phone"] or not request.form["city"] or not request.form["state"]:
            flash('Please enter all the fields', 'error')
        else:
            people = People(request.form["name"], request.form["phone"], request.form["city"], request.form["state"])
            db.session.add(people)
            db.session.commit()
            flash('Record was successfully added')
            return redirect(url_for('show_people'))
    return render_template("index.html")

    def __repr__(self):
        #return f"People('{self.name}','{self.phone}','{self.city}','{self.state}')"
        return f"People('{self.name}')"

@app.route('/show_people', methods = ['GET'])
def show_people():
    return render_template('show_people.html', people = People.query.all())
