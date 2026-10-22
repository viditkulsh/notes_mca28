# Write a Python program to find the elements that are present in either set but not in both sets.

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

result = set1 ^ set2

print("Set 1:", set1)
print("Set 2:", set2)
print("Elements in either set but not both:", result)