# Write a Python program to create a dictionary containing employee names and their salaries and perform the following operations:
# i. Display all elements of the dictionary. 
# ii. Add a new employee and salary. 
# iii. Update the salary of an existing employee. 
# iv. Display the salary of a specified employee. 
# v. Display the total number of employees in the dictionary.

employees = {
    "Rohan": 30000,
    "Priya": 35000,
    "Aman": 40000
}

print("Employee details:")
for name, salary in employees.items():
    print(name, ":", salary)

employees["Neha"] = 38000
print("After adding Neha:", employees)

employees["Rohan"] = 32000
print("After updating Rohan's salary:", employees)

employee_name = "Priya"
if employee_name in employees:
    print(employee_name + "'s salary:", employees[employee_name])
else:
    print("Employee not found.")

print("Total number of employees:", len(employees))