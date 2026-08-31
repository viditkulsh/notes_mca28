# 1. WAPP to check whether a number is even or odd.
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")


# 2. WAPP a Python program to check whether a number is positive, negative or zero.
num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


# 3. WAPP to check whether a person is eligible to vote or not.
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


# 4. WAPP to check whether a student has passed or failed. Assume passing marks are 40.
marks = int(input("Enter your marks: "))
if marks >= 40:
    print("You have passed.")
else:
    print("You have failed.")


# 5. WAPP to find the greater number among two numbers.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 > num2:
    print(f"The greater number is {num1}.")
elif num2 > num1:
    print(f"The greater number is {num2}.")
else:
    print("Both numbers are equal.")


# 6. WAPP to check whether a number is divisible by 5 or not.
num = int(input("Enter a number: "))
if num % 5 == 0:
    print("The number is divisible by 5.")
else:
    print("The number is not divisible by 5.")


# 7. WAPP to check whether a number is divisible by 5 and 7 both.
num = int(input("Enter a number: "))
if num % 5 == 0 and num % 7 == 0:
    print("The number is divisible by both 5 and 7.")
else:
    print("The number is not divisible by both 5 and 7.")


# 8. WAPP to accept a number and check whether it is positive or negative or zero.
num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


# 9. WAPP to accept marks and display the grade (90-100: A, 80-89: B, 70-79: C, 60-69: D, <60: F).
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Your grade is A.")
elif marks >= 80:
    print("Your grade is B.")
elif marks >= 70:
    print("Your grade is C.")
elif marks >= 60:
    print("Your grade is D.")
else:
    print("Your grade is F.")


# 10. WAPP to accept to person's age and display Below 18-Not Eligible to vote, 18-59-Eligible to vote, 60 and above- Senior Citizen.
age = int(input("Enter your age: "))
if age < 18:
    print("Not Eligible to vote.")
elif age >= 18 and age <= 59:
    print("Eligible to vote.")
else:
    print("Senior Citizen.")


# 11. WAPP to accept two accept two numbers and an operator (+,-,*,/,**) perform the corresponding operation.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator = input("Enter the operator (+,-,*,/,**): ")

if operator == "+":
    print(f"The result is {num1 + num2}.")
elif operator == "-":
    print(f"The result is {num1 - num2}.")
elif operator == "*":
    print(f"The result is {num1 * num2}.")
elif operator == "/":
    print(f"The result is {num1 / num2}.")
elif operator == "**":
    print(f"The result is {num1 ** num2}.")
else:
    print("Invalid operator.")