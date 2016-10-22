from utility import Ameren, Laclede
from flask import Flask
from flask import request

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from data.db import db, Person

app = Flask(__name__)

@app.route('/')
def hello():
    return "hi. Try /at_risk"

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
    for customer in at_risk_customers:
        person = Person(customer.first_name, customer.last_name, customer.phone_number, 1)
        db.session.add(person)
        db.session.commit()

    #TODO: Based on the at-risk customers we have found, let's compute the risk_index of each customer.

    # Return all of the customers as a string for now.
    all_at_risk_customers = ""
    for customer in at_risk_customers:
        all_at_risk_customers += str(customer)
    return all_at_risk_customers
