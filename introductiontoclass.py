# Introduction to Class
# - Introduction to Object-Oriented Programming (OOP)

class Animal:
    # Constructor
    #   - Creates a new Animal object
    def __init__(self, name: str):

        self.name = name
        self.colour = ""
        self.age = 0        # in years
        self.weight = 0     # in kgs

        print("Created a new Animal!")

    def breathe(self):
        """Print '---{name} breathes in and out---'"""
        print(f"---{self.name} breathes in and out---")

# Create a new Animal object

fred = Animal("Fred")     # this is a call to __init__()

# Check fred's Type
print(type(fred))

# Change fred's properties
fred.colour = "Blue"
fred.age = 18
fred.weight = 160

# Use the breathe() method on fred
fred.breathe()

fran = Animal("Fran")
fran.breathe()

class Cat(Animal):
    def __init__(self, name: str):
        super().__init__(name)      # superclass constructor

        print("Created a new cat")
        self.sassy = True

    def meow(self):
        print("Meow")
        print(f"My name is {self.name}")

    def breathe(self):
        print(f"---{self.name} purrs as it breathes---")

class Dog(Animal):
    def __init__(self, name:str):
        super().__init__(name)

        print("Created a new dog")
        self.loyal_friend = True

    def bark(self):
        print("Bark!")

    def breathe(self):
        print(f"---{self.name} drools as it breathes---")

chester = Cat("Chester")
chester.breathe()
chester.meow()

dogster = Dog("Dogster")
dogster.breathe()
dogster.bark()
dogster.name = "Dogster Evolved"
print(dogster.name)