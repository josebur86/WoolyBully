from flask import Flask, request

app = Flask(__name__)

app.config.from_pyfile('../config.py')

from routes import *
