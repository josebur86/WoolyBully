from flask import Flask, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

app.config.from_pyfile('../config.py')

from routes import *
