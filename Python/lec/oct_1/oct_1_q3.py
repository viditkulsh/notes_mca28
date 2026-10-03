# Question 3: Write a Python program using a user-defined function to
# calculate the sum and average of a given set of numbers.

count = int(input("How many numbers will you enter? "))

if count <= 0:
    print("Please enter at least one number.")
else:
    total = 0
    for index in range(count):
        number = float(input("Enter a number: "))
        total = total + number

    average = total / count
    print("Sum:", total)
    print("Average:", average)