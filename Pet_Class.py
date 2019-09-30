# Define a Pet class
class Pet():
    def __init__(self, name, owner, breed, animal='Dog'):
        self.name = name
        self.owner = owner
        self.breed = breed
        self.animal = animal

    def get_pet_info(self):
        return '{} is a {} {} owned by {}.'.format(self.name, self.breed, self.animal, self.owner.name)