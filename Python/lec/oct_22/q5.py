# Write a Python program to create two sets of numbers and perform the following operations:
# i. Display all elements of both sets. 
# ii. Find the union of the two sets.
# iii. Find the common elements between the sets. 
# iv. Find elements present in the first set but not in the second set. 
# v. Find elements present in either set but not in both sets.

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("Set 1:", set1)
print("Set 2:", set2)
print("Union:", set1 | set2)
print("Common elements:", set1 & set2)
print("First set minus second set:", set1 - set2)
print("Elements in either set but not both:", set1 ^ set2)