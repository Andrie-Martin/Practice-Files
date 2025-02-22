# Create a class named Person that would have a name attribute and a talk method.

# Code implementation:

class Person:
    def __init__(self, name):
        self.name = name
    
    def talk (self):
        print(f"{user_name} is talking")

# Getting user input
user_name = input("Enter your name: ")
# Code sample

person = Person(user_name)
person.talk()