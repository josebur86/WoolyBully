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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

def recreate_db():
    db.drop_all()
    db.create_all()

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(120))
    last_name = db.Column(db.String(120))
    #email = db.Column(db.String(120), unique=True)
    phone_num = db.Column(db.String(20), unique=False)
    risk_value = db.Column(db.Integer)
    last_contacted = db.Column(db.Date)

    def __init__(self, first_name, last_name, phone_num, risk_value):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_num = phone_num
        self.risk_value = risk_value

    # def __repr__(self):
    #     return '<%i Person>' % self.id

# Late payments
# Outstanding balance
# Shut off date established
class RiskFactor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50))
    value = db.Column(db.Integer)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'))
    person = db.relationship('Person', backref=db.backref('riskfactors', lazy='dynamic'))

    def __init__(self, type, value, person):
        self.type = type
        self.value = value
        self.person = person

class DataHelper:
    def get_all_people(self):
        people = Person.query.order_by(Person.risk_value.desc()).all()
        #print people
        return people

    def get_risk_factors_for(self, person):
        risk_factors = person.riskfactors.all()
        result = dict()
        for risk in risk_factors:
            # result.append("%s: %i" % (risk.type, risk.value))
            result[risk.type] = risk.value

        #print result
        return result
