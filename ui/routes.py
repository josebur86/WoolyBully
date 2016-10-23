from flask import Flask, render_template
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from data.db import DataHelper, db
from ui import app
from forms import signInForm

@app.route('/')
def Index():
    db.create_all()
    db_helper = DataHelper()
    persons = db_helper.get_all_people();

    return render_template('index.html', persons=persons, db_helper=db_helper)

@app.route('/login')
def log_in():
    return render_template('login.html', form=signInForm())
