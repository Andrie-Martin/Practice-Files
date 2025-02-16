# Write a program to remove the duplicates in a list.

list = [1,1,2,2,3,4,4,5,5]

# Code Implementation:

unique_numbers = []
for list in list:
    if list not in unique_numbers:
        unique_numbers.append(list)
print(unique_numbers)