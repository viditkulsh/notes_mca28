# Question 1: Write a Python program to perform these operations on a list:
# a) Create a list of numbers.
# b) Add elements to the list.
# c) Find and update an element.
# d) Display the elements of the list using a loop.
# e) Sort the list.

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Original list:", numbers)

new_number = int(input("Enter a number to add: "))
numbers.append(new_number)

target = int(input("Enter the number to find and update: "))
found = False
for index in range(len(numbers)):
    if numbers[index] == target:
        replacement = int(input("Enter its replacement value: "))
        numbers[index] = replacement
        found = True
        break

if found:
    print("The element was updated.")
else:
    print("The element was not found.")

print("List elements:")
for number in numbers:
    print(number)

numbers.sort()
print("Sorted list:", numbers)