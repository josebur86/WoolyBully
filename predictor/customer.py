class Customer(object):
    """
    Customer object representing a current utility company customer.
    """

    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.phone_number = -1
        self.veteran = "False"
        self.sex = "Male"
        self.disabled = "False"
        self.age = 30

    def __init__(self, first_name, last_name, phone_number, veteran, sex, disabled, age):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.veteran = veteran
        self.sex = sex
        self.disabled = disabled
        self.age = age

    def __str__(self):
        return self.first_name + " " + self.last_name + " " + str(self.phone_number)


# veteran_status = db.Column(db.String(5))
# sex = db.Column(db.String(10))
# disabled = db.Column(db.String(5))
# age = db.Column(db.Integer)
