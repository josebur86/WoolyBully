from utility import Ameren
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def hello():
    return "hi. Try /at_risk"

@app.route('/at_risk', methods=['GET'])
def get_at_risk_customers():
    utilities_to_check = []
    utilities_to_check.append(Ameren())

    at_risk_customers = set()

    for utility in utilities_to_check:
        unpaid_customers = utility.get_unpaid_customers()

        # For now, all unpaid customers will be considered at-risk customers.
        at_risk_customers = at_risk_customers.union(unpaid_customers)

    #TODO: Insert the at-risk customers into the database.
    #TODO: Based on the at-risk customers we have found, let's compute the risk_index of each customer.

    # Return all of the customers as a string for now.
    all_at_risk_customers = ""
    for customer in at_risk_customers:
        all_at_risk_customers += str(customer)
    return all_at_risk_customers
