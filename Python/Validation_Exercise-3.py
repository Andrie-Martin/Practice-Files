# If the name has fewer than 3 characters, it must be at least 3 characters long.  
# If the name exceeds 12 characters, it must not be longer than 12 characters.  
# Otherwise, the name is valid.

# Code implementation:

name = input("Please enter your desired name here: ")

if len(name) < 3:
    print("Invalid name! Your name must be 3 characters long.")
elif len(name) > 12:
    print("Invalid name! Your name must not be greater than 12 characters long.")
    
else:
    print("Good name!")


