# Question 2: Accept a number and perform these operations:
# i. Check whether it is even or odd.
# ii. Check whether it is positive or negative.
# iii. Calculate its factorial.
# iv. Display its multiplication table.
# v. Check whether it is divisible by both 5 and 7.

number = int(input("Enter an integer: "))

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

if number < 0:
    print("Factorial is not defined for negative integers.")
else:
    factorial = 1
    for value in range(1, number + 1):
        factorial = factorial * value
    print("Factorial:", factorial)

print("Multiplication table:")
for multiplier in range(1, 11):
    print(number, "x", multiplier, "=", number * multiplier)

if number % 5 == 0 and number % 7 == 0:
    print("The number is divisible by both 5 and 7.")
else:
    print("The number is not divisible by both 5 and 7.")