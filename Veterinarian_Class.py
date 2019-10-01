# Import Human Class
from Human_Class import *
from Appointment_Class import *

# Define our Veterinarian class as a sub class of Human
class Veterinarian(Human):
    def __init__(self, name, phone_number, email, specialisation):
        super().__init__(name, phone_number, email)
        self.specialisation = specialisation
        self.appointment_list = []

    def add_appointment(self, ailment, date, pet, cost):
        self.appointment_list.append(Appointment(ailment, date, pet, cost))

    def list_appointment(self, appointment):
        # return appointment.appointment_list
        return '{} has an appointment with {} on {} for {}. It costs {}.'.format(self.name, appointment.pet.name, appointment.date, appointment.ailment, appointment.cost)


