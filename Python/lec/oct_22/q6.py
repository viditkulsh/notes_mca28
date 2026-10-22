# Write a Python program to create two sets of numbers and perform the following operations:
# i. Display both sets. 
# ii. Add an element to the first set. 
# iii. Remove an element from the first set. 
# iv. Find the union of both sets. 
# v. Find the common elements between the sets.

set1 = {10, 20, 30}
set2 = {20, 30, 40}

print("Original Set 1:", set1)
print("Original Set 2:", set2)

set1.add(50)
print("Set 1 after adding 50:", set1)

set1.discard(10)
print("Set 1 after removing 10:", set1)

print("Union:", set1 | set2)
print("Common elements:", set1 & set2)