# Write a Python program to create a set of five numbers and perform the following operations:
# i. Display all elements of the set. 
# ii. Find the number of elements in the set. 
# iii. Add a new element to the set. 
# iv. Remove a specified element from the set. 
# v. Check whether a specified number exists in the set.

numbers = {10, 20, 30, 40, 50}

print("Original set:", numbers)
print("Number of elements:", len(numbers))

numbers.add(60)
print("After adding 60:", numbers)

numbers.discard(30)
print("After removing 30:", numbers)

number_to_check = 40
if number_to_check in numbers:
    print(number_to_check, "exists in the set.")
else:
    print(number_to_check, "does not exist in the set.")
    