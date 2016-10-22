from flask import Flask, render_template
# from ..data.db import DataHelper
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from data.db import DataHelper, db
from ui import app

@app.route('/')
def Index():
    db.create_all()
    db_helper = DataHelper()
    persons = db_helper.get_all_people();
    return render_template('index.html', persons=persons)
