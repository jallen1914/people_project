# views.py

from flask import render_template
from flask import request

from app import app


@app.route('/', methods=["GET", "POST"])
def index():
    if request.form:
        print(request.form)
    return render_template("index.html")

#TESTING
'''
@app.route('/about')
def about():
    return render_template("about.html")
'''
