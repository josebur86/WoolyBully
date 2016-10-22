from customer import Customer
from abc import ABCMeta, abstractmethod

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

    def fake_ameren_customers(self):
        """
        Return a list of fake customers.
        """
        customers = set()

        customers.add(Customer("Joanne", "Cook", "1112223333"))
        customers.add(Customer("Donald", "Townsend", "1112223334"))
        customers.add(Customer("Patricia", "Johnson", "1112223335"))

        return customers

    def get_unpaid_customers(self):
        """
        Here is where we would access the Ameren API to get the list of unpaid customers.
        Since there is no Ameren API at the moment, we will generate fake customers for now.
        """
        unpaid_customers = self.fake_ameren_customers()

        return unpaid_customers

    def type(self):
        return "Electricity"
