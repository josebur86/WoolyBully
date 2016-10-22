from customer import Customer
from abc import ABCMeta, abstractmethod
from phone_numbers import PhoneNumbers

class Utility(object):
    """
    Abstract base class representing a utlity.
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_unpaid_customers(self):
        """
        Returns a list of unpaid customers for the utility
        """
        pass

    @abstractmethod
    def type(self):
        """ The type of the utility (electric, gas, etc) """
        pass

class Ameren(Utility):
    """
    Abstraction of the Ameren API.
    This class would wrap the calls to the Ameren API in the future.
    """

    def __init__(self):
        pass

    def fake_customers(self):
        """
        Return a list of fake customers.
        """
        customers = set()

        phone_numbers = PhoneNumbers()
        customers.add(Customer("Joanne", "Cook", phone_numbers.get_phone_number()))
        customers.add(Customer("Donald", "Townsend", phone_numbers.get_phone_number()))
        customers.add(Customer("Patricia", "Johnson", phone_numbers.get_phone_number()))

        return customers

    def get_unpaid_customers(self):
        """
        Here is where we would access the Ameren API to get the list of unpaid customers.
        Since there is no Ameren API at the moment, we will generate fake customers for now.
        """
        unpaid_customers = self.fake_customers()

        return unpaid_customers

    def type(self):
        return "Electricity"

class Laclede(Utility):
    """
    Abstraction of the Laclede API.
    This class would wrap the calls to the Laclede API in the future.
    """

    def __init__(self):
        pass

    def fake_customers(self):
        """
        Return a list of fake customers.
        """
        customers = set()

        phone_numbers = PhoneNumbers()
        customers.add(Customer("Eugene", "Matsumura", phone_numbers.get_phone_number()))

        return customers

    def get_unpaid_customers(self):
        """
        Here is where we would access the Laclede API to get the list of unpaid customers.
        Since there is no Laclede API at the moment, we will generate fake customers for now.
        """
        unpaid_customers = self.fake_customers()

        return unpaid_customers

    def type(self):
        return "Gas"
