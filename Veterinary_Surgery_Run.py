# Import the revelant class information
from Owner_Class import *
from Veterinarian_Class import *
from Pet_Class import *
from Pet_Class import *


## User Stories

### As a user, I can create a pet

# Create some owners for the pets first so we can assign the pet their owner
owner_1 = Owner('Constance Huxton', '07884446661', 'c___huxie___bbe___xoxox@gmail.co.uk', 'Cheque')
owner_2 = Owner('Tina Two-face', '01580 997456', 'tina_rocks_so_much@hotmail.co.uk', 'Cash')
owner_3 = Owner('Perseval Battlement', '0748615793', 'percy_loves_pigs@yahoo.net', 'Credit Card')
owner_4 = Owner('Truman Banjo', '0745699521', 'banjo_player_boi@aol.com', 'Wire Transfer')
owner_5 = Owner('Susan Perrywinkle', '07045664813', 'not_susan_boyle_lol@sendymail.com', 'Debit Card')

# Create some pets
pet_1 = Pet('Rocky', owner_1, 'Dachshund')
pet_2 = Pet('Bernie', owner_2, 'Bernese Mountain Dog')
pet_3 = Pet('Balthasar', owner_3, 'Springer Spaniel')
pet_4 = Pet('Mongo', owner_4, 'Staffordshire Bull Terrier')
pet_5 = Pet('Harmony', owner_5, 'Basset Hound')
pet_list = [pet_1, pet_2, pet_3, pet_4, pet_5]

# Create some vets so we can have appointments with these vets
vet_1 = Veterinarian('Dr Frank Lovedog', '01622 845993', 'lovesdogs188@tiscali.net', 'Dogs')
vet_2 = Veterinarian('Dr Rosie Cheeks', '01622 941752', 'cheeky_gal_99@msn.com', 'Rodents')
vet_3 = Veterinarian('Dr Ben Dover', '01622 5524460', 'dover_ben_55@outlookinggood.com', 'Hippopotamuses')
# make a list of vets to iterate over if needs be
vet_list = [vet_1, vet_2, vet_3]

### As a user I can add a pet to an appointment
vet_1.add_appointment('Broken leg', '1/10/19', pet_1, '£83.51')
vet_1.add_appointment('Runny nose', '2/10/19', pet_2, '106.91')
vet_2.add_appointment('Busted Liver', '2/10/19', pet_3, '£900.06')
vet_3.add_appointment('Mangled Ear', '3/10/19', pet_4, '£415.47')
vet_3.add_appointment('Needs new glasses', '4/10/19', pet_5, '£125.99')

# print(' ')
# print('Get appointment list for each pet')
# print(vet_1.appointment_list)
# print(vet_2.appointment_list)
# print(vet_3.appointment_list)

### As a user, I can list all appointments and the pets in them
print(' ')

for index in range(len(vet_list)):
    print('List all appointments with Vet {}.'.format(index+1))
    vet_list[index].list_appointment()
# print('List all appointments with Vet 1')
# vet_1.list_appointment()
# print('List all appointments with Vet 2')
# vet_2.list_appointment()
# print('List all appointments with Vet 3')
# vet_3.list_appointment()

### As a user I can get pet details and owner details for ONE pet
print(' ')
print('Getting Pet info')
for index in range(len(pet_list)):
    print(pet_list[index].get_pet_info())

# print(pet_1.get_pet_info())
# print(pet_2.get_pet_info())
# print(pet_3.get_pet_info())
# print(pet_4.get_pet_info())
# print(pet_5.get_pet_info())
