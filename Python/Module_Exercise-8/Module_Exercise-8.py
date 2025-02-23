# Given this code:

# numbers = [10,20,30,40,50]
# max = numbers[0]
# def findmax():
#   for number in number:
#       if number > max:
#           max = number
# print (max)

# write a function called find max(),This function should take a list, and return the largest number in that list. 
# Now after you do this, go ahead and put this function in a separate module. 
# So extract it from here, and put it in a module, called utils.

# Code Implementation:

from utils import find_max

numbers = [20,30,40,50,60]
max = find_max(numbers)
print(max)