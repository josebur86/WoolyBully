from flask import Flask, render_template, redirect
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from data.db import DataHelper, db
from ui import app
from forms import signInForm

last_contacted = ["March 18, 2016", "October 21, 2016", "January 1, 2016","September 7, 2016","October 2, 2016","July 1, 2016","October 9, 2016"]

@app.route('/')
def Index():
    db.create_all()
    db_helper = DataHelper()
    persons = db_helper.get_all_people();
    return render_template('index.html', persons=persons, db_helper=db_helper, contact_dates=last_contacted)

@app.route('/login')
def log_in():
    return render_template('login.html', form=signInForm())

@app.route('/login', methods=['POST'])
def submit():
    return redirect('/')
