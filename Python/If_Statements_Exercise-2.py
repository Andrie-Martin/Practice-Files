# The price of a house is 1 million pesos. If the buyer has a good credit, they need to put down a 10% down payment. Otherwise, they need to put 20%.
# Write a code that will ask if the user has a good credit then apply if else statements to get results.

# Code Implementation:

buyer = input("Answer yes or no only, do you have a good credit? ")
is_bad_credit = 1000000 * 0.2
is_good_credit = 1000000 * 0.1
if buyer == "yes":
    print(f"Your downpayment is ₱ {is_good_credit}")
else:
    print(f"Your downpayment is ₱ {is_bad_credit}")