class Customer(object):
    """
    Customer object representing a current utility company customer.
    """

    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.phone_number = -1

    def __init__(self, first_name, last_name, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number

    def __str__(self):
        return self.first_name + " " + self.last_name + " " + str(self.phone_number)
