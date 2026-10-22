# Write a Python program to create two sets and perform the following operations:
# i. Display all elements of both sets. 
# ii. Find the difference between the first and second sets. 
# iii. Find the difference between the second and first sets. 
# iv. Find the intersection of both sets. 
# v. Check whether a specified element exists in a set.

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
element = 3

print("Set 1:", set1)
print("Set 2:", set2)
print("First set minus second set:", set1 - set2)
print("Second set minus first set:", set2 - set1)
print("Intersection:", set1 & set2)

if element in set1:
    print(element, "exists in Set 1.")
else:
    print(element, "does not exist in Set 1.")
    