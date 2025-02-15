# Using nested loop, create the letter F in this format:

#  xxxxx
#  xx
#  xxxxx
#  xx
#  xx
#  xx

# Code Implementation

numbers = [5, 2, 5, 2, 2, 2]

for x in numbers:
    outcome = ""
    for y in range(x):
        outcome += 'x'
    print(outcome)


# Now, do it for the letter L:
print(" ")
print(" ")

numbers = [2, 2, 2, 2, 10]

for x in numbers:
    outcome = ""
    for y in range(x):
        outcome += 'x'
    print(outcome)
