# 1. Access List Elements
print("Ques1")
# Write a Python program to create a list containing 10, 20, 30, 40 and 50. Display: first element, last element, third element.
numbers = [10, 20, 30, 40, 50]
print(f"First element: {numbers[0]}")
print(f"Last element: {numbers[-1]}")
print(f"Third element: {numbers[2]}")

print("")

# 2. Display Elements with Their Index
print("Ques2")
# Write a Python program to create a list of numbers and display each element along with its index.
numbers = [10, 20, 30, 40, 50]
for index, value in enumerate(numbers):
    print(f"Index {index} -> {value}")

print("")

# 3. Update an Element
print("Ques3")
# Write a Python program to create a list of 5 numbers. Replace the third element with 100 and display the updated list.
numbers = [10, 20, 30, 40, 50]
print(f"Original list: {numbers}")
numbers[2] = 100
print(f"Updated list: {numbers}")

print("")

# 4. Find the Length of a List
print("Ques4")
# Write a Python program to create a list and find the total number of elements present in the list.
numbers = [10, 20, 30, 40, 50]
print(f"The list has {len(numbers)} elements.")

print("")

# 5. Concatenate Two Lists
print("Ques5")
# Write a Python program to create two lists and combine them into a single list.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(f"First list: {list1}")
print(f"Second list: {list2}")
print(f"Combined list: {combined}")

print("")

# 6. Check Whether an Element Exists
print("Ques6")
# Write a Python program to create a list of numbers. Accept a number from the user and check whether it is present in the list.
numbers = [10, 20, 30, 40, 50]
print(f"List: {numbers}")
num = int(input("Enter a number to search: "))
if num in numbers:
    print(f"{num} is present in the list.")
else:
    print(f"{num} is not present in the list.")

print("")

# 7. Find Maximum and Minimum
print("Ques7")
# Write a Python program to find the largest and smallest elements from a list of numbers.
numbers = [45, 12, 78, 3, 56]
print(f"List: {numbers}")
print(f"Largest element: {max(numbers)}")
print(f"Smallest element: {min(numbers)}")

print("")

# 8. Find the Sum of List Elements
print("Ques8")
# Write a Python program to calculate and display the sum of all elements in a list.
numbers = [10, 20, 30, 40, 50]
print(f"List: {numbers}")
print(f"Sum of all elements: {sum(numbers)}")
