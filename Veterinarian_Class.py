# Import Human Class
from Human_Class import *

# Define out Veterinarian class as a sub class of Human
class Veterinarian(Human):
    def __init__(self, name, phone_number, email, specialisation):
        super().__init__(name, phone_number, email)
        self.specialisation = specialisation
        
