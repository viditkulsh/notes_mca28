from pathlib import Path

content = r'''# Python Practical Programs: Sets, Lists, and Dictionaries

This file contains solutions to all 13 Python programming questions. Each program is standalone and includes sample data and output-producing statements.

---

## 1. Find Elements Present in Either Set but Not Both

**Concept:** Symmetric difference (`^` or `symmetric_difference()`).

```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

result = set1 ^ set2

print("Set 1:", set1)
print("Set 2:", set2)
print("Elements in either set but not both:", result)
```

## 2. Find Common Elements Between Two Sets

**Concept:** Intersection (`&` or `intersection()`).

```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

common = set1 & set2

print("Set 1:", set1)
print("Set 2:", set2)
print("Common elements:", common)
```

## 3. Find Elements in the First Set but Not in the Second

**Concept:** Set difference (`-` or `difference()`).

```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

result = set1 - set2

print("Elements in the first set but not in the second:", result)
```

## 4. Perform Operations on a List of Numbers

Operations:
1. Display even numbers.
2. Display odd numbers.
3. Count positive numbers.
4. Count negative numbers.
5. Count zeros.

```python
numbers = [10, -3, 0, 7, -8, 2, 0, -1, 5]

even_numbers = [n for n in numbers if n % 2 == 0]
odd_numbers = [n for n in numbers if n % 2 != 0]
positive_count = sum(1 for n in numbers if n > 0)
negative_count = sum(1 for n in numbers if n < 0)
zero_count = numbers.count(0)

print("List:", numbers)
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
print("Positive numbers:", positive_count)
print("Negative numbers:", negative_count)
print("Zeros:", zero_count)
```

## 5. Perform Multiple Operations on Two Sets of Numbers

Operations:
1. Display both sets.
2. Find their union.
3. Find common elements.
4. Find elements in the first set but not the second.
5. Find elements in either set but not both.

```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("Set 1:", set1)
print("Set 2:", set2)
print("Union:", set1 | set2)
print("Common elements:", set1 & set2)
print("First set minus second set:", set1 - set2)
print("Elements in either set but not both:", set1 ^ set2)
```

## 6. Add and Remove Elements, Then Find Union and Intersection

```python
set1 = {10, 20, 30}
set2 = {20, 30, 40}

print("Original Set 1:", set1)
print("Original Set 2:", set2)

set1.add(50)
print("Set 1 after adding 50:", set1)

set1.discard(10)
print("Set 1 after removing 10:", set1)

print("Union:", set1 | set2)
print("Common elements:", set1 & set2)
```

> `discard()` removes an element if it exists and does not raise an error if it is absent.

## 7. Find Set Differences, Intersection, and Check Membership

```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
element = 3

print("Set 1:", set1)
print("Set 2:", set2)
print("First set minus second set:", set1 - set2)
print("Second set minus first set:", set2 - set1)
print("Intersection:", set1 & set2)

if element in set1:
    print(element, "exists in Set 1.")
else:
    print(element, "does not exist in Set 1.")
```

## 8. Perform Operations on a Set of Five Numbers

```python
numbers = {10, 20, 30, 40, 50}

print("Original set:", numbers)
print("Number of elements:", len(numbers))

numbers.add(60)
print("After adding 60:", numbers)

numbers.discard(30)
print("After removing 30:", numbers)

number_to_check = 40
if number_to_check in numbers:
    print(number_to_check, "exists in the set.")
else:
    print(number_to_check, "does not exist in the set.")
```

## 9. Perform Operations on Two Sets of Fruits

```python
fruits1 = {"apple", "banana", "mango", "orange"}
fruits2 = {"banana", "orange", "grapes", "kiwi"}

print("First set of fruits:", fruits1)
print("Second set of fruits:", fruits2)
print("Union:", fruits1 | fruits2)
print("Common fruits:", fruits1 & fruits2)
print("Fruits only in the first set:", fruits1 - fruits2)
```

## 10. Perform Operations on a Student Marks Dictionary

```python
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
```

## 11. Perform Operations on a Product Price Dictionary

```python
products = {
    "Notebook": 50,
    "Pen": 10,
    "Bag": 800
}

print("Product dictionary:", products)
print("Product names:", list(products.keys()))
print("Product prices:", list(products.values()))

products["Pencil"] = 5
print("After adding Pencil:", products)

total_price = sum(products.values())
print("Total price of all products:", total_price)
```

## 12. Perform Operations on an Employee Salary Dictionary

```python
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
```

## 13. Perform Operations on a Subject Marks Dictionary

```python
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
```

---

## Quick Reference

| Operation | Python syntax | Meaning |
|---|---|---|
| Union | `set1 \| set2` | Elements in either set |
| Intersection | `set1 & set2` | Elements common to both sets |
| Difference | `set1 - set2` | Elements in the first set but not the second |
| Symmetric difference | `set1 ^ set2` | Elements in either set but not both |
| Add to a set | `my_set.add(value)` | Adds one element |
| Remove safely | `my_set.discard(value)` | Removes an element if present |
| Dictionary keys | `my_dict.keys()` | All keys |
| Dictionary values | `my_dict.values()` | All values |
| Dictionary items | `my_dict.items()` | Key-value pairs |
| Dictionary size | `len(my_dict)` | Number of key-value pairs |
'''

path = Path("/mnt/data/python_sets_lists_dictionaries_practical.md")
path.write_text(content, encoding="utf-8")
print(f"Created: {path}")
