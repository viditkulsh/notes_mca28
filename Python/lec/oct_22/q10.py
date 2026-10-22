# Write a Python program to create a dictionary containing student names and their marks and perform the following operations:
# i. Display all keys and values. 
# ii. Add a new student and their marks. 
# iii. Update the marks of an existing student.
# iv. Display the marks of a specified student. 
# v. Remove a student from the dictionary.

students = {
    "Aarav": 85,
    "Diya": 92,
    "Kabir": 78
}

print("Student marks:")
for name, marks in students.items():
    print(name, ":", marks)

students["Meera"] = 88
print("After adding Meera:", students)

students["Aarav"] = 90
print("After updating Aarav's marks:", students)

student_name = "Diya"
if student_name in students:
    print(student_name + "'s marks:", students[student_name])
else:
    print("Student not found.")

students.pop("Kabir", None)
print("After removing Kabir:", students)