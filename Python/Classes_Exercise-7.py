# Create a class named Person that would have a name attribute and a talk method.

# Code implementation:

class Person:
    def __init__(self, name):
        self.name = name
    
    def talk (self):
        print("talk")


# Code sample

name = Person("Liam")
print (name.name)
name.talk()