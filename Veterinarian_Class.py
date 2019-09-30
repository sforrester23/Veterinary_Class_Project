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

    def list_appointment(self):
        count = 1
        for appointment in self.appointment_list:
            # return appointment.appointment_list
            print('{}: {} has an appointment with {} on {} for {}. It costs {}.'.format(count, self.name, appointment.pet.name, appointment.date, appointment.ailment, appointment.cost))
            count += 1

