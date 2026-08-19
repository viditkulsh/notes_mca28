# 1. Identify Data Types
# Write a Python program to create variables for an integer, floating-point number, complex number, string, and Boolean value. Display each value along with its data type. Hint: Use the type() function.

a = 25
b = 45.75
c = 3 + 4j
d = "Vidit"
e = True

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(e, type(e))


# 2. Student Information
# Write a Python program to store a student's name, age,
# roll number, percentage, and course.
# Display all the information along with their respective data types.
# Hint: Use appropriate data types such as str, int, and float.

name = "Vidit Kulshrestha"
age = 22
roll_no = 21
percentage = 89.5
course = "MCA"

print("Name:", name, type(name))
print("Age:", age, type(age))
print("Roll No:", roll_no, type(roll_no))
print("Percentage:", percentage, type(percentage))
print("Course:", course, type(course))


# 3. Type Conversion
# Write a Python program to convert the following values and
# display the results:
# • Integer into float
# • Integer into string
# • String containing a number into integer
# • Integer into Boolean
# Hint: Use float(), str(), int(), and bool().

num = 100
num_str = "250"

print("Integer to Float:", float(num), type(float(num)))
print("Integer to String:", str(num), type(str(num)))
print("String to Integer:", int(num_str), type(int(num_str)))
print("Integer to Boolean:", bool(num), type(bool(num)))
print("Zero to Boolean:", bool(0))


# 4. List Operations
# Write a Python program to create a list containing the marks
# of five subjects. Display the following:
# • All marks
# • Highest marks
# • Lowest marks
# • Total marks
# • Average marks
# Hint: Use max(), min(), sum(), and len().

marks = [98, 85, 75, 68, 97]

print("All Marks:", marks)
print("Highest Marks:", max(marks))
print("Lowest Marks:", min(marks))
print("Total Marks:", sum(marks))
print("Average Marks:", sum(marks) / len(marks))


# 5. Modify a List
# Write a Python program to create a list containing
# five programming languages.
# Replace the second element with
# another programming language and display the modified list.
# Hint: Use list indexing.

languages = ["C", "C++", "Python", "Java", "JavaScript"]
print("Original List:", languages)
languages[1] = "PHP"
print("Modified List:", languages)


# 6. Tuple Operations
# Write a Python program to create a tuple containing
# five numbers.
# Display the number of elements,
# maximum value, minimum value, and sum of all elements.
# Hint: Use len(), max(), min(), and sum().

numbers = (90, 85, 78, 95, 65)

print("Tuple:", numbers)
print("Number of Elements:", len(numbers))
print("Maximum Value:", max(numbers))
print("Minimum Value:", min(numbers))
print("Sum of Elements:", sum(numbers))


# 7. Dictionary – Student Details
# Write a Python program to create
# a dictionary containing the name,
# roll number, course, and
# percentage of a student.
# Display each value separately using its corresponding key.
# Hint: Use dictionary keys to access individual values.

student = {
    "Name": "Deadpool",
    "Rno": 21,
    "Course": "MCA",
    "Prcntg": 89.5
}

print("Name:", student["Name"])
print("Roll No:", student["Rno"])
print("Course:", student["Course"])
print("Percentage:", student["Prcntg"])


# B) Write a Python program to create
# a dictionary containing the
# employee name, employee Id, salary,
# department and address
# of a employee.
# Display each value separately using its corresponding key.
# Hint: Use dictionary keys to access individual values.

employee = {
    "Name": "Wolverine",
    "EmpId": "E1024",
    "Salary": 75000.50,
    "Department": "IT",
    "Address": "Pune, Maharashtra"
}

print("Employee Name:", employee["Name"])
print("Employee Id:", employee["EmpId"])
print("Salary:", employee["Salary"])
print("Department:", employee["Department"])
print("Address:", employee["Address"])


# 8. Remove Duplicate Elements
# Write a Python program to create a list
# containing duplicate numbers and remove
# the duplicate values from the list.
# Hint: Convert the list into a set.

dup_list = [10, 20, 10, 30, 40, 20, 50, 30]
print("Original List:", dup_list)

unique_list = list(set(dup_list))
print("List After Removing Duplicates:", unique_list)


# 9. Mutable and Immutable Data Types
# Write a Python program to demonstrate that
# a list is mutable and a tuple is immutable.
# Hint: Create a list and a tuple, then try to modify one
# element of each.

my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)

print("List Before Change:", my_list)
my_list[0] = 100
print("List After Change:", my_list, "-> List is Mutable")

print("Tuple Before Change:", my_tuple)
try:
    my_tuple[0] = 100
except TypeError as err:
    print("Error:", err, "-> Tuple is Immutable")


# Part B – Strings
# 10. Basic String Operations
# Write a Python program to store your name in a variable
# and display:
# • The complete name
# • First character
# • Last character
# • Length of the name
# Hint: Use indexing and len().

my_name = "Vidit"

print("Complete Name:", my_name)
print("First Character:", my_name[0])
print("Last Character:", my_name[-1])
print("Length of Name:", len(my_name))


# Write a Python program to store your name in
# a variable and display:
# • The name in uppercase
# • The name in lowercase
# • Length of the name
# Hint: Use upper(),lower() and len().

print("Uppercase:", my_name.upper())
print("Lowercase:", my_name.lower())
print("Length of Name:", len(my_name))


# 11. String Slicing
# Write a Python program to store
# the string "PythonProgramming" and display:
# • First 6 characters
# • Last 11 characters
# • Characters from index 2 to 7
# Hint: Use string slicing [start:end].

s1 = "PythonProgramming"

print("String:", s1)
print("First 6 Characters:", s1[0:6])
print("Last 11 Characters:", s1[-11:])
print("Characters from Index 2 to 7:", s1[2:8])


# C) Write a Python program to store the
# string "PythonProgrammingDemo"
# and display:
# • First 10 characters
# • Last 15 characters
# • Characters from index 6 to 16
# Hint: Use string slicing [start:end].

s2 = "PythonProgrammingDemo"

print("String:", s2)
print("First 10 Characters:", s2[0:10])
print("Last 15 Characters:", s2[-15:])
print("Characters from Index 6 to 16:", s2[6:17])


# 12. String Case Conversion
# Write a Python program to accept
# a string from the user and display it in:
# • Uppercase
# • Lowercase
# • Capitalized form
# • Title case
# • Swapped case
# Hint: Use upper(), lower(), capitalize(),
# title(), and swapcase().

text = input("Enter a string: ")

print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Capitalized:", text.capitalize())
print("Title Case:", text.title())
print("Swapped Case:", text.swapcase())


# 13. Remove Extra Spaces
# Write a Python program to accept
# a string containing spaces at
# the beginning and end.
# Remove the unnecessary spaces
# and display the resulting string.
# Hint: Use strip().

spaced = input("Enter a string with spaces at both ends: ")

print("Before Strip:", "[" + spaced + "]")
print("After Strip:", "[" + spaced.strip() + "]")


# 14. Count a Character
# Write a Python program to accept
# a string and a character from the user.
# Count how many times
# the given character occurs in the string.
# Hint: Use the count() method.

str_input = input("Enter a string: ")
char_input = input("Enter a character to count: ")

print("Occurrences of", char_input, ":", str_input.count(char_input))


# 15. Find a Word
# Write a Python program to
# accept a sentence and
# search for a specified word.
# Display the position of the
# word if it is found.
# Hint: Use the find() method.

sentence = input("Enter a sentence: ")
word = input("Enter the word to search: ")

position = sentence.find(word)
if position != -1:
    print("Word found at position:", position)
else:
    print("Word not found in the sentence")


# 16. Replace a Word
# Write a Python program to accept
# a sentence and replace
# a specified word with another word.
# Display the modified sentence.
# Hint: Use the replace() method.

sentence2 = input("Enter a sentence: ")
old_word = input("Enter the word to replace: ")
new_word = input("Enter the new word: ")

print("Modified Sentence:", sentence2.replace(old_word, new_word))


# 17. Split a Sentence
# Write a Python program to accept a sentence and display each word separately.
# Hint: Use the split() method.

sentence3 = input("Enter a sentence: ")

for w in sentence3.split():
    print(w)


# 18. Check Starting and Ending
# Write a Python program to accept a string and check whether it starts with "Python" and ends
# with "Programming"
# .
# Hint: Use startswith() and endswith().

str18 = input("Enter a string: ")

print("Starts with 'Python':", str18.startswith("Python"))
print("Ends with 'Programming':", str18.endswith("Programming"))


# 19. Check String Content
# Write a Python program to accept a string and check whether it contains only alphabets, only
# digits, or both alphabets and digits.
# Hint: Use isalpha(), isdigit(), and isalnum().

str19 = input("Enter a string: ")

if str19.isalpha():
    print("The string contains only alphabets")
elif str19.isdigit():
    print("The string contains only digits")
elif str19.isalnum():
    print("The string contains both alphabets and digits")
else:
    print("The string contains other characters as well")


# 20. String Validation
# Write a Python program to accept a student's name and perform the following operations:
# 1. Display the name in uppercase.
# 2. Display the name in lowercase.
# 3. Display the length of the name.
# 4. Count the occurrence of the letter 'a'
# .
# 5.Display the first and last character of string.
# 6. Check whether the name starts with the letter 'S'
# .
# 7. Check whether the name contains only alphabets.
# Hints: Use upper(), lower(), len(), count(), startswith(), and isalpha().

sname = input("Enter student's name: ")

print("Uppercase:", sname.upper())
print("Lowercase:", sname.lower())
print("Length of Name:", len(sname))
print("Occurrence of 'a':", sname.count("a"))
print("First Character:", sname[0])
print("Last Character:", sname[-1])
print("Starts with 'S':", sname.startswith("S"))
print("Contains only alphabets:", sname.isalpha())


# 21. Student Information and String Operations
# Write a Python program to accept the following information from a student:
# • Name
# • Age
# • Course
# • Percentage
# Perform the following operations:
# 1. Display all the entered information.
# 2. Display the data type of each value.
# 3. Display the student's name in uppercase.
# 4. Display the student's name in lowercase.
# 5. Display the length of the student's name.
# 6. Check whether the name contains only alphabets.
# 7. Display the first and last character of the name.
# Hints:
# • Use int() for age.
# • Use float() for percentage.
# • Use type() to identify data types.
# • Use string methods for the name.
# • Use indexing to access the first and last characters.

st_name = input("Enter name: ")
st_age = int(input("Enter age: "))
st_course = input("Enter course: ")
st_percentage = float(input("Enter percentage: "))

print("Name:", st_name, type(st_name))
print("Age:", st_age, type(st_age))
print("Course:", st_course, type(st_course))
print("Percentage:", st_percentage, type(st_percentage))

print("Name in Uppercase:", st_name.upper())
print("Name in Lowercase:", st_name.lower())
print("Length of Name:", len(st_name))
print("Contains only alphabets:", st_name.isalpha())
print("First Character:", st_name[0])
print("Last Character:", st_name[-1])


# 25. String Formatting and Validation
# Write a Python program to accept a student's name from the user and perform the
# following operations:
# 1. Display the name in capitalized form.
# 2. Display the name in title case.
# 3. Display the name with swapped case.
# 4. Remove any extra spaces from the beginning and end of the name.
# 5. Check whether the name contains a space.
# 6. Check whether the name is written in lowercase.
# Hint: Use capitalize(), title(), swapcase(), strip(), isspace(), and islower().

name25 = input("Enter student's name: ")

print("Capitalized:", name25.capitalize())
print("Title Case:", name25.title())
print("Swapped Case:", name25.swapcase())
print("After Strip:", "[" + name25.strip() + "]")
print("Contains a space:", " " in name25)
print("Is written in lowercase:", name25.islower())


# 26. String Content Checking
# Write a Python program to accept a string from the user and perform the following
# operations:
# 1. Check whether the string contains only decimal digits.
# 2. Check whether the string contains only alphabets.
# 3. Check whether the string contains only lowercase characters.
# 4. Check whether the string contains only uppercase characters.
# 5. Check whether the string contains only whitespace characters.
# Hint: Use isdigit(), isalpha(), islower(), isupper(), and isspace().

str26 = input("Enter a string: ")

print("Only digits:", str26.isdigit())
print("Only alphabets:", str26.isalpha())
print("Only lowercase:", str26.islower())
print("Only uppercase:", str26.isupper())
print("Only whitespace:", str26.isspace())


# 27. Sentence Processing
# Write a Python program to accept a sentence from the user and perform the following
# operations:
# 1. Display each word separately.
# 2. Display the number of words in the sentence.
# 3. Find the position of the first occurrence of a specified word.
# 4. Replace a specified word with another word.
# 5. Remove unnecessary spaces from the beginning and end of the sentence.
# Hint: Use split(), len(), find(), replace(), and strip().

sent27 = input("Enter a sentence: ")
word_list = sent27.split()

print("Words in the sentence:")
for w in word_list:
    print(w)
print("Number of Words:", len(word_list))

search_word = input("Enter a word to search: ")
print("Position of first occurrence:", sent27.find(search_word))

old27 = input("Enter the word to replace: ")
new27 = input("Enter the new word: ")
print("After Replacement:", sent27.replace(old27, new27))

print("After Strip:", "[" + sent27.strip() + "]")


# 28. String Checking and Searching
# Write a Python program to accept a string from the user and perform the following
# operations:
# 1. Check whether the string ends with "ing"
# .
# 2. Find the position of the first occurrence of the letter "a"
# .
# 3. Count the number of characters in the string.
# 4. Check whether all characters in the string are alphanumeric.
# 5. Display the string in title case.
# Hint: Use endswith(), find(), len(), isalnum(), and title().

str28 = input("Enter a string: ")

print("Ends with 'ing':", str28.endswith("ing"))
print("Position of first 'a':", str28.find("a"))
print("Number of Characters:", len(str28))
print("All characters alphanumeric:", str28.isalnum())
print("Title Case:", str28.title())
