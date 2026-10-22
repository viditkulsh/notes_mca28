# Write a Python program to create a list of numbers and perform the following operations:
# i. Display all even numbers in the list. 
# ii. Display all odd numbers in the list. 
# iii. Count positive numbers. 
# iv. Count negative numbers. 
# v. Count zeros in the list.


numbers = [10, -3, 0, 7, -8, 2, 0, -1, 5]

even_numbers = [n for n in numbers if n % 2 == 0]
odd_numbers = [n for n in numbers if n % 2 != 0]
positive_count = sum(1 for n in numbers if n > 0)
negative_count = sum(1 for n in numbers if n < 0)
zero_count = numbers.count(0)

print("List:", numbers)
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
print("Positive numbers:", positive_count)
print("Negative numbers:", negative_count)
print("Zeros:", zero_count)