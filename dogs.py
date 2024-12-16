from animal import Animal

class Dog(Animal):
    def __init__(self, name, breed, age, colour):
        super().__init__(name)
        self.breed = breed
        self.age = age
        self.colour = colour

    def bark(self):
        return f'{self.name} says WOOF!!'
    
    # def speak(self): # Overide the speak method of Animal
    #     return self.bark()