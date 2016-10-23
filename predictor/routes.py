from utility import Ameren, Laclede
from flask import Flask, request
from predictor import app

import random
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from data.db import db, Person, RiskFactor

@app.route('/')
def hello():
    return "hi... Try /at_risk"

@app.route('/at_risk', methods=['GET'])
def get_at_risk_customers():
    utilities_to_check = []
    utilities_to_check.append(Ameren())
    utilities_to_check.append(Laclede())

    at_risk_customers = set()

    for utility in utilities_to_check:
        unpaid_customers = utility.get_unpaid_customers()

        # For now, all unpaid customers will be considered at-risk customers.
        at_risk_customers = at_risk_customers.union(unpaid_customers)

    # Insert the at-risk customers into the database.
    db.create_all()
    for customer in at_risk_customers:
        person = db.session.query(Person).filter_by(phone_num=customer.phone_number).one_or_none()
        if (person == None):
            person = Person(customer.first_name, customer.last_name, customer.phone_number, generate_risk_value())
            db.session.add(person)
            add_risk_factor_for(person)
            db.session.commit()

    #TODO: Based on the at-risk customers we have found, let's compute the risk_index of each customer.
    # Use the phone number as the unique identifier.
    # Add the customer if they aren't in the database, update the risk value
    # if they are.
    # The risk value will be a random value between 0-100

    # Return all of the customers as a string for now.
    all_at_risk_customers = ""
    for customer in at_risk_customers:
        all_at_risk_customers += str(customer)
    return all_at_risk_customers

def add_risk_factor_for(person):
    if (person.risk_value > 80):
        print "High Risk"
        factor0 = RiskFactor("Shutoff date established", 1, person)
        factor1 = RiskFactor("Outstanding Balance", 600, person)
        db.session.add(factor0)
        db.session.add(factor1)
    else:
        print "Low Risk"
        factor = RiskFactor("Outstanding Balance", 600, person)
        db.session.add(factor)

def generate_risk_value():
    result = random.randrange(10, 100)
    return result
