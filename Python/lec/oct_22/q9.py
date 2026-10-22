# Write a Python program to create two sets of fruits and perform the following operations:
# i. Display both sets. 
# ii. Find the union of both sets. 
# iii. Find the common fruits between the sets. 
# iv. Find fruits present only in the first set.

fruits1 = {"apple", "banana", "mango", "orange"}
fruits2 = {"banana", "orange", "grapes", "kiwi"}

print("First set of fruits:", fruits1)
print("Second set of fruits:", fruits2)
print("Union:", fruits1 | fruits2)
print("Common fruits:", fruits1 & fruits2)
print("Fruits only in the first set:", fruits1 - fruits2)