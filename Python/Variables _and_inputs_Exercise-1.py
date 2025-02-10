# We check in John Smith. He's 20 y/o and is a old patient residing at the hospital for 1.5 years. Base on the given info, create 4 different types of variables.

name = "John Smith"
age = 20
is_new_patient = False
reside = 1.5

print (type(name))
print (type(age))
print (type(is_new_patient))
print (type(reside))


# Ask four questions about John.

name_question = input(" What is your name ")
print ("Hi " + name_question + "! ")
age_question = input ("How old are you " + name_question + "? ")
new_patient_question = input ("Are you new here " + name_question + "? ")
reside_question = input("When did you stay here? ")
