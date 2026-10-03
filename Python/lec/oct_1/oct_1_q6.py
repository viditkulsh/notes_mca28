# Question 6: Create a list of numbers and:
# i. Display all the elements of the list using a loop.
# ii. Count the number of even elements in the list.
# iii. Count the number of odd elements in the list.
# iv. Calculate the sum of even elements.
# v. Calculate the sum of odd elements.

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

even_count = 0
odd_count = 0
even_sum = 0
odd_sum = 0

print("List elements:")
for number in numbers:
    print(number)
    if number % 2 == 0:
        even_count = even_count + 1
        even_sum = even_sum + number
    else:
        odd_count = odd_count + 1
        odd_sum = odd_sum + number

print("Number of even elements:", even_count)
print("Number of odd elements:", odd_count)
print("Sum of even elements:", even_sum)
print("Sum of odd elements:", odd_sum)
