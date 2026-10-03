# Question 4: Accept a number and use a while loop to:
# i. Display each digit of the number.
# ii. Calculate the sum of its digits.
# iii. Calculate the product of its digits.
# iv. Count the number of digits.
# v. Display the number in reverse order.

number = int(input("Enter an integer: "))
remaining = abs(number)
digit_sum = 0
digit_product = 1
digit_count = 0
reverse = 0

print("Digits:")
if remaining == 0:
    print(0)
    digit_product = 0
    digit_count = 1
else:
    while remaining > 0:
        digit = remaining % 10
        print(digit)
        digit_sum = digit_sum + digit
        digit_product = digit_product * digit
        digit_count = digit_count + 1
        reverse = reverse * 10 + digit
        remaining = remaining // 10

if number < 0:
    reverse = -reverse

print("Sum of digits:", digit_sum)
print("Product of digits:", digit_product)
print("Number of digits:", digit_count)
print("Reversed number:", reverse)