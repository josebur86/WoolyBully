# To get all the people in the database
# from data.db import DataHelper
# db = DataHelper()
# people = db.get_all_people()

# Each person has the following member variables:
# id
# first_name | string
# last_name | string
# phone_num | string
# risk_value | integer

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# TODO(joe): Figure out the best place to create this database.
# On my machine this puts it in the C:/ directory.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////test.db'
db = SQLAlchemy(app)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(120))
    last_name = db.Column(db.String(120))
    #email = db.Column(db.String(120), unique=True)
    phone_num = db.Column(db.String(20), unique=True)
    risk_value = db.Column(db.Integer)

    def __init__(self, first_name, last_name, phone_num, risk_value):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_num = phone_num
        self.risk_value = risk_value

    # def __repr__(self):
    #     return '<%i Person>' % self.id

class DataHelper:
    def get_all_people(self):
        people = Person.query.all()
        #print people
        return people
