# Question 5: Create a list of numbers and:
# i. Display all the elements of the list.
# ii. Find the largest element in the list.
# iii. Find the smallest element in the list using a function.
# iv. Calculate the sum of all elements in the list.
# v. Calculate the average of the elements in the list.

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

if len(numbers) == 0:
    print("Please enter at least one number.")
else:
    largest = numbers[0]
    smallest = numbers[0]
    total = 0

    print("List elements:")
    for number in numbers:
        print(number)
        total = total + number
        if number > largest:
            largest = number
        if number < smallest:
            smallest = number

    average = total / len(numbers)
    print("Largest element:", largest)
    print("Smallest element:", smallest)
    print("Sum of elements:", total)
    print("Average of elements:", average)
