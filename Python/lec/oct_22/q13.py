# Write a Python program to create a dictionary containing subject names and their marks and perform the following operations:
# i. Display all subject names and marks. 
# ii. Add a new subject and its marks. 
# iii. Display the highest marks. 
# iv. Calculate the total marks of all subjects. v. Calculate the average marks of all
# subjects.

subjects = {
    "Python": 88,
    "DBMS": 82,
    "Java": 91
}

print("Subject marks:")
for subject, marks in subjects.items():
    print(subject, ":", marks)

subjects["Networking"] = 86
print("After adding Networking:", subjects)

highest_marks = max(subjects.values())
total_marks = sum(subjects.values())
average_marks = total_marks / len(subjects)

print("Highest marks:", highest_marks)
print("Total marks:", total_marks)
print("Average marks:", round(average_marks, 2))