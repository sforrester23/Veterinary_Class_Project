# Import the revelant class information
from Owner_Class import *
from Veterinarian_Class import *
from Pet_Class import *


## User Stories

### As a user, I can create a pet

# Create some owners for the pets first so we can assign the pet their owner
owner_1 = Owner('Constance Huxton', '07884446661', 'c___huxie___bbe___xoxox@gmail.co.uk', 'Cheque')
owner_2 = Owner('Tina Two-face', '01580 997456', 'tina_rocks_so_much@hotmail.co.uk', 'Cash')
owner_3 = Owner('Perseval Battlement', '0748615793', 'percy_loves_pigs@yahoo.net', 'Credit Card')
owner_4 = Owner('Truman Banjo', '0745699521', 'banjo_player_boi@aol.com', 'Wire Transfer')
owner_5 = Owner('Susan Perrywinkle', '07045664813', 'not_susan_boyle_lol@sendymail.com', 'Debit Card')
owner_list = [owner_1, owner_2, owner_3, owner_4, owner_5]

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

# for vets in range(len(vet_list)):
#     print('List all appointments with Vet {}.'.format(vets + 1))
#     for appointment in range(len(vet_list[vets].appointment_list)):
#         print(vet_list[vets].list_appointment(vet_list[vets].appointment_list[appointment]))

# print('List all appointments with Vet 1')
# vet_1.list_appointment()
# print('List all appointments with Vet 2')
# vet_2.list_appointment()
# print('List all appointments with Vet 3')
# vet_3.list_appointment()

### As a user I can get pet details and owner details for ONE pet
# print(' ')
# print('Getting Pet info')
# for index in range(len(pet_list)):
#     print(pet_list[index].get_pet_info())

# print(pet_1.get_pet_info())
# print(pet_2.get_pet_info())
# print(pet_3.get_pet_info())
# print(pet_4.get_pet_info())
# print(pet_5.get_pet_info())

# Give the user some options to choose from
print(' ')
print('Option 1: Add a pet to the list.')
print('Option 2: Add an appointment for a pet.')
print('Option 3: Add an owner.')
print('Option 4: Print appointment info for a particular vet.')
print('Type exit to leave')
user_choice = input('What would you like to do?: ').strip().upper()


## Run the while loop to form the basis of the user interaction
while user_choice != 'EXIT':
    if user_choice == '1':
        pet_name = input('What is the pet\'s name? ')
        pet_animal = input('What type of animal is the pet? ')
        pet_breed = input('What breed is the pet? ')
        print(' ')
        print('Owner List:') # for loop for printing the owners names from the owner list
        for owner in range(len(owner_list)):
            print('Owner {}: {}'.format(owner+1, owner_list[owner].name))
        pet_owner_choice = int(input('Which owner would you like to assign the pet to? '))
        owner_choice = owner_list[pet_owner_choice-1]
        # make the pet based on the user input
        pet_add = Pet(pet_name, owner_choice, pet_breed, pet_animal)
        # Add the pet to the list
        pet_list.append(pet_add)

    elif user_choice == '2':
        print('Which pet are you wishing to make an appointment for? ')
        for pet in range(len(pet_list)):
            print('Pet {}: {}'.format(pet+1, pet_list[pet].name))
        pet_name_choice = int(input('Please select a pet from the options: '))
        pet_choice = pet_list[pet_name_choice-1]
        ailment_choice = input('What is wrong with your pet? ')
        date_choice = input('When would you like the appointment? ')
        cost_choice = input('How much will it cost? ')
        for vets in range(len(vet_list)):
            print('Vet {} : {} '.format(vets+1, vet_list[vets].name))
        vet_choice = int(input('Which vet would you like to do the appointment? Please choose from the above: '))
        vet_choice = vet_list[vet_choice-1]
        vet_choice.add_appointment(ailment_choice, date_choice, pet_choice, cost_choice)
        print('Appointment on {} added with {}'.format(date_choice, vet_choice.name))

    elif user_choice == '3':
        print('So you wish to add an owner.')
        owner_name = input('What is the owner\'s name? ')
        owner_phone = input('What is the owner\'s phone number? ')
        owner_email = input('What is the owner\'s email address? ')
        owner_payment = input('What is the owner\'s preferred payment method? ')
        owner_add = Owner(owner_name, owner_phone, owner_email, owner_payment)
        owner_list.append(owner_add)

    elif user_choice == '4':
        print('So you\'d like to print some appointment information.')
        for vet in range(len(vet_list)):
            print('Vet {}: {}'.format(vet+1, vet_list[vet].name))
        vet_choice_app = int(input('Which vet would you like to print appointment information for? Choose an option from above. '))
        print('List all appointments with Vet {}.'.format(vet_choice_app))
        for appointment in range(len(vet_list[vet_choice_app-1].appointment_list)):
            print(vet_list[vet_choice_app-1].list_appointment(vet_list[vet_choice_app-1].appointment_list[appointment]))

    else:
        print('Sorry, that is not an option, please try again. ')

    # Repeat the main menu back to the user
    print(' ')
    print('Option 1: Add a pet to the list.')
    print('Option 2: Add an appointment for a pet.')
    print('Option 3: Add an owner.')
    print('Option 4: Print appointment info for a particular vet.')
    print('Type exit to leave')
    user_choice = input('What would you like to do?: ').strip().upper()