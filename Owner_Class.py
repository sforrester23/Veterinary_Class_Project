# Import Human Class
from Human_Class import *

# Define our Owner class as a sub class of Human
class Owner(Human):
    def __init__(self, name, phone_number, email, payment_details):
        super().__init__(name, phone_number, email)
        self.payment_details = payment_details