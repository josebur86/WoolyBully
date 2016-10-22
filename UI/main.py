from flask import Flask, render_template
# from ..data.db import DataHelper
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from data.db import DataHelper

app = Flask(__name__)

@app.route('/')
def Index():
    db = DataHelper()
    persons = db.get_all_people();
    return render_template('index.html', persons=persons)
