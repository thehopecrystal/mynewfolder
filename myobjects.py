class Dog:

    # Constructor
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        return f'{self.name} says WOOF!!'
    