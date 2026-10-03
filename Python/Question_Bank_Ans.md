# Python — Answers to Question Bank

Structured, exam-oriented answers to every question in [Question_Bank.md](Question_Bank.md). Numbering matches the question bank exactly, so question 9 here answers question 9 there.

Theory answers (Q1–Q13) follow the same shape: **Definition → Explanation → Code with output → Comparison table → One-line summary**. Program answers (Q14–Q19) give the full program, a sample run and the logic in brief. Q1, Q2, Q4, Q5, Q8, Q9, Q12 and Q13 are written at 10-mark depth; the rest at 5-mark depth.

Mid-term pattern ([Paper_pattern.pdf](Paper_pattern.pdf)): Units 1 and 2, 30 marks, 1 hour. Section I is compulsory (two 5-mark questions); in Section II you answer any two of three 10-mark questions.

> Student-written notes. Every code block was run with Python 3.14 and the outputs shown are the real outputs; in sample runs, the text after each prompt is what was typed. Cross-check terminology against the class slides in [Slides/](Slides/) before the exam.

## Contents

- [Part A — Theory (Q1–Q13)](#part-a--theory-q1q13)
  - [Q1. Data types, variables, identifiers, keywords and literals](#q1-data-types-variables-identifiers-keywords-and-literals)
  - [Q2. Cloning, aliasing and mutability of lists](#q2-cloning-aliasing-and-mutability-of-lists)
  - [Q3. Assignment, membership and identity operators](#q3-assignment-membership-and-identity-operators)
  - [Q4. Arithmetic, relational and logical operators; recursion and factorial](#q4-arithmetic-relational-and-logical-operators-recursion-and-factorial)
  - [Q5. User-defined functions — definition, arguments, return and scope](#q5-user-defined-functions--definition-arguments-return-and-scope)
  - [Q6. String indexing and slicing](#q6-string-indexing-and-slicing)
  - [Q7. Functions of the statistics module](#q7-functions-of-the-statistics-module)
  - [Q8. Iteration — for and while loops, break, continue and pass](#q8-iteration--for-and-while-loops-break-continue-and-pass)
  - [Q9. Functions of the math module](#q9-functions-of-the-math-module)
  - [Q10. Positional, default and keyword arguments](#q10-positional-default-and-keyword-arguments)
  - [Q11. Input and output statements](#q11-input-and-output-statements)
  - [Q12. Lists — adding, finding, updating, nesting, looping, sorting, concatenation, slicing](#q12-lists--adding-finding-updating-nesting-looping-sorting-concatenation-slicing)
  - [Q13. List methods — adding, removing, reversing and sorting](#q13-list-methods--adding-removing-reversing-and-sorting)
- [Part B — Programs (Q14–Q19)](#part-b--programs-q14q19)
  - [Q14. List operations — create, add, find and update, display, sort](#q14-list-operations--create-add-find-and-update-display-sort)
  - [Q15. Even/odd, sign, factorial, table and divisibility by 5 and 7](#q15-evenodd-sign-factorial-table-and-divisibility-by-5-and-7)
  - [Q16. Sum and average using a user-defined function](#q16-sum-and-average-using-a-user-defined-function)
  - [Q17. Digits of a number using a while loop](#q17-digits-of-a-number-using-a-while-loop)
  - [Q18. Display, largest, smallest, sum and average of a list](#q18-display-largest-smallest-sum-and-average-of-a-list)
  - [Q19. Count and sum of even and odd elements](#q19-count-and-sum-of-even-and-odd-elements)
- [Quick revision sheet](#quick-revision-sheet)

---

## Part A — Theory (Q1–Q13)

### Q1. Data types, variables, identifiers, keywords and literals

**Definition**

A **data type** specifies the kind of value an object holds and the operations allowed on it (two numbers can be divided, two strings cannot). Python is **dynamically typed**: the type belongs to the value, not to the variable, and is decided at run time. The built-in `type()` function reports it.

**Built-in data types**

| Category | Type | Example | Mutable? |
|---|---|---|---|
| Numeric | `int` — whole numbers of any size | `25`, `-8`, `0b1010` | No |
| | `float` — real numbers (decimal point or exponent) | `3.14`, `2.5e3` | No |
| | `complex` — `a + bj` | `3 + 4j` | No |
| Boolean | `bool` — `True` / `False` (a subclass of `int`) | `True` | No |
| Text | `str` — sequence of characters in quotes | `"MCA"`, `'Pune'` | No |
| Sequence | `list` — ordered collection in `[]` | `[10, 20, 30]` | **Yes** |
| | `tuple` — ordered collection in `()` | `(10, 20, 30)` | No |
| | `range` — sequence of integers | `range(1, 6)` | No |
| Set | `set` — unordered, no duplicates, in `{}` | `{1, 2, 3}` | **Yes** |
| | `frozenset` — immutable set | `frozenset({1, 2, 3})` | No |
| Mapping | `dict` — `key: value` pairs, keys unique | `{"name": "Vidit", "rno": 21}` | **Yes** |
| None | `NoneType` — the single value `None` ("no value") | `None` | No |
| Binary | `bytes`, `bytearray`, `memoryview` | `b"abc"` | `bytes` no, `bytearray` yes |

**Mutable** types (`list`, `dict`, `set`, `bytearray`) can be changed in place and keep the same `id()`; **immutable** types (`int`, `float`, `complex`, `bool`, `str`, `tuple`, `frozenset`, `bytes`) cannot — any "change" creates a new object.

```python
age = 25
price = 45.75
z = 3 + 4j
passed = True
course = "MCA"
marks = [10, 20, 30]
point = (10, 20, 30)
nums = range(1, 6)
ids = {1, 2, 3, 2}
frozen = frozenset([1, 2, 3])
student = {"name": "Vidit", "rno": 21}
result = None
data = b"abc"

for value in (age, price, z, passed, course, marks, point,
              nums, ids, frozen, student, result, data):
    print(value, type(value))
```

Output:

```text
25 <class 'int'>
45.75 <class 'float'>
(3+4j) <class 'complex'>
True <class 'bool'>
MCA <class 'str'>
[10, 20, 30] <class 'list'>
(10, 20, 30) <class 'tuple'>
range(1, 6) <class 'range'>
{1, 2, 3} <class 'set'>
frozenset({1, 2, 3}) <class 'frozenset'>
{'name': 'Vidit', 'rno': 21} <class 'dict'>
None <class 'NoneType'>
b'abc' <class 'bytes'>
```

The set printed `{1, 2, 3}` because duplicates are dropped. A few properties worth quoting:

```python
print(2 ** 100)                      # 1267650600228229401496703205376
print(0.1 + 0.2)                     # 0.30000000000000004
print((3 + 4j).real, (3 + 4j).imag)  # 3.0 4.0
print(True + True)                   # 2
```

`int` has unlimited precision, `float` is stored in binary so it is approximate, a `complex` exposes `.real` and `.imag`, and `bool` behaves as `1`/`0` in arithmetic.

**Variables**

A variable is a name that refers to a value stored in memory. It is created automatically the first time a value is assigned with `=` — there is no declaration — and the same name can later refer to a value of a different type.

```python
course = "MCA"            # str
year = 1                  # int
year = "First"            # same name now refers to a str (dynamic typing)
x = y = z = 0             # one value, many names
name, age = "Vidit", 22   # multiple assignment
print(course, year, x, y, z, name, age)  # MCA First 0 0 0 Vidit 22
```

**Identifiers**

An identifier is the name given to a variable, function, class, module or object. Rules:

1. It may contain letters (`A–Z`, `a–z`), digits (`0–9`) and the underscore `_`.
2. It must not start with a digit.
3. No spaces or special symbols such as `@`, `$`, `-`, `%`.
4. It cannot be a keyword.
5. It is case-sensitive: `marks`, `Marks` and `MARKS` are three different names.
6. There is no length limit, but names should be meaningful (convention: `snake_case` for variables and functions, `UPPER_CASE` for constants).

```python
import keyword

for name in ["student_name", "_count", "marks2", "2marks", "student-name", "class"]:
    valid = name.isidentifier() and not keyword.iskeyword(name)
    print(name, "->", "valid" if valid else "invalid")
```

Output:

```text
student_name -> valid
_count -> valid
marks2 -> valid
2marks -> invalid
student-name -> invalid
class -> invalid
```

`2marks` starts with a digit, `student-name` contains a hyphen and `class` is a keyword.

**Keywords**

Keywords are reserved words with a predefined meaning; they cannot be used as identifiers. All are lowercase except `True`, `False` and `None`. The `keyword` module lists them:

```python
import keyword

print(keyword.kwlist)
print(len(keyword.kwlist))
print(keyword.iskeyword("for"), keyword.iskeyword("For"))
print(keyword.softkwlist)
```

Output (Python 3.14 — the count can differ between versions):

```text
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
35
True False
['_', 'case', 'match', 'type']
```

| Purpose | Keywords |
|---|---|
| Values | `True`, `False`, `None` |
| Operators | `and`, `or`, `not`, `in`, `is` |
| Decisions | `if`, `elif`, `else` |
| Loops | `for`, `while`, `break`, `continue` |
| Functions | `def`, `return`, `lambda`, `yield`, `global`, `nonlocal` |
| Modules | `import`, `from`, `as` |
| Exceptions | `try`, `except`, `finally`, `raise`, `assert` |
| Others | `class`, `pass`, `del`, `with`, `async`, `await` |

*Soft keywords* (`match`, `case`, `type`, `_`) act as keywords only in particular statements and can still be used as ordinary names elsewhere.

**Literals**

A literal is a fixed value written directly in the program; it does not change during execution.

| Literal | Examples |
|---|---|
| Integer | `100`, `-7`, `0b1010` (binary), `0o17` (octal), `0xFF` (hexadecimal), `1_000_000` |
| Float | `3.14`, `-0.5`, `2.5e3` |
| Complex | `3 + 4j`, `2j` |
| String | `'single'`, `"double"`, `'''triple'''`, `"""multi-line"""` |
| Boolean | `True`, `False` |
| Special | `None` |
| Collections | `[1, 2]` (list), `(1, 2)` (tuple), `{1, 2}` (set), `{"a": 1}` (dict) |

```python
print(0b1010, 0o17, 0xFF, 1_000_000)     # 10 15 255 1000000
print(2.5e3, 3 + 4j, True, None)         # 2500.0 (3+4j) True None
print('single', "double", '''triple''')  # single double triple
```

**Summary:** Python's built-in types are numeric (`int`, `float`, `complex`), `bool`, `str`, sequences (`list`, `tuple`, `range`), sets (`set`, `frozenset`), `dict` and `NoneType`; a variable is a name bound to a value, an identifier is a programmer-chosen name that follows the naming rules, keywords are reserved words (`keyword.kwlist`), and literals are fixed values written in code.

---

### Q2. Cloning, aliasing and mutability of lists

**Mutability**

A list is **mutable**: its elements can be changed, added or removed *in place* after it is created, and the list object itself — its identity, `id()` — stays the same.

```python
nums = [10, 20, 30]
before = id(nums)

nums[0] = 99       # change an element
nums.append(40)    # add an element
del nums[1]        # remove an element

print(nums)                # [99, 30, 40]
print(id(nums) == before)  # True
```

Strings and tuples are immutable, so the same kind of change is refused:

```python
text = "python"
try:
    text[0] = "P"
except TypeError as err:
    print("TypeError:", err)  # TypeError: 'str' object does not support item assignment
```

Because lists are mutable, it matters whether two names share one list (**aliasing**) or each has its own copy (**cloning**).

**Aliasing**

Aliasing means giving another name to the same list. `b = a` copies only the *reference*: no new list is created, both names point to one object, and a change made through either name is visible through the other.

```python
a = [10, 20, 30]
b = a              # alias: no new list

b[0] = 100
print(a)               # [100, 20, 30]
print(b)               # [100, 20, 30]
print(a is b)          # True
print(id(a) == id(b))  # True
```

```text
Aliasing:   a ----+
                  +---> [100, 20, 30]     one list object, two names
            b ----+

Cloning:    a --------> [10, 20, 30]      two separate list objects
            c --------> [10, 20, 30]
```

Passing a list to a function also creates an alias — the parameter refers to the caller's list:

```python
def add_bonus(marks):
    marks.append(5)   # changes the caller's list


scores = [70, 80]
add_bonus(scores)
print(scores)  # [70, 80, 5]
```

**Cloning**

Cloning means creating a separate copy of a list, so the copy and the original can be changed independently. There are three ways to clone a simple list:

```python
a = [10, 20, 30]

c1 = a[:]       # 1. slicing
c2 = list(a)    # 2. list() constructor
c3 = a.copy()   # 3. copy() method

c1[0] = 100
c2[1] = 200
c3[2] = 300

print(a)                     # [10, 20, 30]
print(c1, c2, c3)            # [100, 20, 30] [10, 200, 30] [10, 20, 300]
print(a == a[:], a is a[:])  # True False
```

A fresh clone is *equal* to the original (`==` is `True`) but is a *different object* (`is` is `False`).

**Shallow copy vs deep copy (nested lists)**

`a[:]`, `list(a)` and `a.copy()` are **shallow** copies: they create a new outer list, but the inner lists are still shared with the original. For a nested list use `copy.deepcopy()`, which copies the inner lists too.

```python
import copy

marks = [[80, 90], [70, 60]]
shallow = marks.copy()
deep = copy.deepcopy(marks)

shallow[0][0] = 100   # changes the inner list shared with marks
deep[1][1] = 0        # changes deep's own inner list only

print(marks)                   # [[100, 90], [70, 60]]
print(shallow)                 # [[100, 90], [70, 60]]
print(deep)                    # [[80, 90], [70, 0]]
print(shallow[0] is marks[0])  # True
print(deep[0] is marks[0])     # False
```

**Cloning vs aliasing**

| Basis | Aliasing | Cloning |
|---|---|---|
| Syntax | `b = a` | `b = a[:]`, `list(a)`, `a.copy()`, `copy.deepcopy(a)` |
| New list created? | No — a second name for the same object | Yes — a separate object |
| `b is a` / `id(a) == id(b)` | `True` | `False` |
| `b == a` (just after) | `True` | `True` |
| Change through `b` | Also seen through `a` | `a` unaffected (for nested lists only with `deepcopy`) |
| Memory | No extra memory | Extra memory for the copy |
| Use when | Two names, or a function, should work on the same list | The original must stay safe while the copy changes |

**Summary:** Lists are mutable, so `b = a` (aliasing) gives two names for one list and changes show through both, while cloning with `a[:]`, `list(a)` or `a.copy()` — or `copy.deepcopy(a)` for nested lists — creates an independent copy.

---

### Q3. Assignment, membership and identity operators

**1. Assignment operators**

Assignment operators store a value in a variable. `=` is simple assignment; the **augmented** (compound) operators combine an arithmetic operation with assignment, so `x += 4` means `x = x + 4`.

| Operator | Example | Same as | Result if `x = 10` before |
|---|---|---|---|
| `=` | `x = 10` | — | `10` |
| `+=` | `x += 4` | `x = x + 4` | `14` |
| `-=` | `x -= 4` | `x = x - 4` | `6` |
| `*=` | `x *= 4` | `x = x * 4` | `40` |
| `/=` | `x /= 4` | `x = x / 4` | `2.5` |
| `//=` | `x //= 4` | `x = x // 4` | `2` |
| `%=` | `x %= 4` | `x = x % 4` | `2` |
| `**=` | `x **= 4` | `x = x ** 4` | `10000` |

The bitwise forms `&=`, `|=`, `^=`, `<<=` and `>>=` work the same way.

```python
x = 10
x += 5
print(x)     # 15
x *= 2
print(x)     # 30
x //= 4
print(x)     # 7
x %= 4
print(x)     # 3
x **= 3
print(x)     # 27
x /= 3
print(x)     # 9.0

a, b = 1, 2  # multiple assignment
a, b = b, a  # swap without a temporary variable
print(a, b)  # 2 1
p = q = 0    # chained assignment
print(p, q)  # 0 0
```

The **walrus operator** `:=` (assignment expression, Python 3.8+) assigns a value *and* returns it, so it can be used inside a condition:

```python
data = [4, 8, 15, 16, 23, 42]
if (count := len(data)) > 5:
    print("List is long:", count, "items")  # List is long: 6 items
```

**2. Membership operators**

Membership operators test whether a value is present in a sequence or collection (string, list, tuple, set, dictionary) and return `True` or `False`.

| Operator | Returns `True` when | Example | Result |
|---|---|---|---|
| `in` | the value is found | `20 in [10, 20, 30]` | `True` |
| `not in` | the value is not found | `"z" not in "Python"` | `True` |

```python
numbers = [10, 20, 30, 40, 50]
print(20 in numbers)                # True
print(100 not in numbers)           # True
print("w" in "hello world")         # True
print("Java" in "Python")           # False
print("read" in ("read", "write"))  # True

user = {"username": "ajay", "level": 5}
print("username" in user)           # True
print("ajay" in user)               # False
print("ajay" in user.values())      # True
```

For a dictionary, `in` checks the **keys**; use `.values()` to search the values.

**3. Identity operators**

Identity operators check whether two names refer to the **same object in memory** (the same `id()`); `==` only checks whether the **values are equal**.

| Operator | Returns `True` when | Example |
|---|---|---|
| `is` | both names refer to the same object | `list1 is list3` |
| `is not` | the names refer to different objects | `list1 is not list2` |

```python
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(list1 == list2)          # True
print(list1 is list2)          # False
print(list1 is list3)          # True
print(list1 is not list2)      # True
print(id(list1) == id(list3))  # True

result = None
print(result is None)          # True
```

`list1` and `list2` hold equal values but are two separate objects; `list3` is another name for `list1`. Use `is` for identity checks such as `x is None`, not to compare numbers or strings — whether two equal numbers or strings are the same object depends on interpreter caching.

**`==` vs `is`**

| `==` (equality) | `is` (identity) |
|---|---|
| Compares values | Compares object identity (memory location) |
| `list1 == list2` → `True` | `list1 is list2` → `False` |
| Behaviour can be defined by the class | Cannot be changed |
| Use for comparing data | Use for `None` checks and to detect aliasing |

**Summary:** Assignment operators (`=`, `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`, and `:=`) store and update values; membership operators `in`/`not in` test whether a value is present in a collection (keys for a dict); identity operators `is`/`is not` test whether two names are the same object, which is different from `==` value equality.

---

### Q4. Arithmetic, relational and logical operators; recursion and factorial

**1. Arithmetic operators** perform mathematical calculations.

| Operator | Name | Example (`a = 17`, `b = 5`) | Result |
|---|---|---|---|
| `+` | Addition | `a + b` | `22` |
| `-` | Subtraction | `a - b` | `12` |
| `*` | Multiplication | `a * b` | `85` |
| `/` | Division (always a float) | `a / b` | `3.4` |
| `//` | Floor division (rounds down) | `a // b` | `3` |
| `%` | Modulus (remainder) | `a % b` | `2` |
| `**` | Exponentiation (power) | `a ** 2` | `289` |

- `/` always returns a `float`, even for an exact division: `10 / 2` is `5.0`.
- `//` rounds **down** (towards minus infinity): `17 // 5` is `3` but `-17 // 5` is `-4`. With a float operand the result is a float.
- `%` gives the remainder, which takes the sign of the divisor: `-17 % 5` is `3`. Always `a == (a // b) * b + a % b`.
- `**` is evaluated right to left: `2 ** 3 ** 2` is `2 ** 9`.
- Precedence: `**` → unary `-` → `*`, `/`, `//`, `%` → `+`, `-` → comparisons → `not` → `and` → `or`. Parentheses override it.

```python
a, b = 17, 5
print(a + b)         # 22
print(a - b)         # 12
print(a * b)         # 85
print(a / b)         # 3.4
print(10 / 2)        # 5.0
print(a // b)        # 3
print(-17 // 5)      # -4
print(17.0 // 5)     # 3.0
print(a % b)         # 2
print(-17 % 5)       # 3
print(a ** 2)        # 289
print(2 ** 3 ** 2)   # 512
print(2 + 3 * 4)     # 14
print((2 + 3) * 4)   # 20
```

**2. Relational (comparison) operators** compare two values and return `True` or `False`.

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `==` | Equal to | `5 == 3` | `False` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `>` | Greater than | `5 > 3` | `True` |
| `<` | Less than | `5 < 3` | `False` |
| `>=` | Greater than or equal to | `5 >= 5` | `True` |
| `<=` | Less than or equal to | `5 <= 3` | `False` |

`=` assigns, `==` compares. Strings are compared character by character using Unicode values, so an uppercase English letter comes before every lowercase one (`"Zebra" < "apple"`). Comparisons can be **chained**: `1 < x < 15` means `1 < x and x < 15`.

```python
x, y = 10, 20
print(x == y)              # False
print(x != y)              # True
print(x < y)               # True
print(x >= 10)             # True
print("apple" < "banana")  # True
print("Zebra" < "apple")   # True
print(1 < x < 15)          # True
print(10 < x < 20)         # False
```

**3. Logical operators** combine conditions.

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `and` | `True` only if both conditions are `True` | `(5 > 3) and (3 > 1)` | `True` |
| `or` | `True` if at least one condition is `True` | `(5 > 3) or (3 < 1)` | `True` |
| `not` | Reverses the result | `not (5 > 3)` | `False` |

| A | B | A `and` B | A `or` B | `not` A |
|---|---|---|---|---|
| True | True | True | True | False |
| True | False | False | True | False |
| False | True | False | True | True |
| False | False | False | False | True |

**Short-circuit evaluation:** Python stops evaluating as soon as the answer is known — `and` stops at the first false operand, `or` at the first true one. A guard condition can therefore protect the next one. `and`/`or` also return one of their operands, not necessarily `True`/`False`.

```python
age, has_id = 20, True
print(age >= 18 and has_id)   # True
print(age < 18 or has_id)     # True
print(not has_id)             # False

x = 0
print(x != 0 and 10 / x > 1)  # False
print(x == 0 or 10 / x > 1)   # True
print(0 or "default")         # default
print(5 and 7)                # 7
```

In the two lines with `x = 0`, `10 / x` is never evaluated, so there is no `ZeroDivisionError`.

**4. Recursion**

**Definition:** Recursion is a technique in which a function calls itself to solve a problem by breaking it into smaller sub-problems of the same type. Such a function is called a **recursive function**. Every recursive function has two parts:

1. **Base case (base condition)** — the simplest input, answered directly without another call. It stops the recursion.
2. **Recursive case** — the function calls itself with a smaller input that moves towards the base case.

Factorial is defined recursively: `n! = n × (n − 1)!`, with `0! = 1! = 1` as the base case.

**Program: factorial using recursion** (as in [func_prgm/q18.py](func_prgm/q18.py))

```python
def factorial(num):
    if num == 0 or num == 1:  # Base case, stops the recursion.
        return 1
    else:
        return num * factorial(num - 1)  # The function calls itself.


num = int(input("Enter a number: "))
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"The factorial of {num} is {factorial(num)}.")
```

Sample run:

```text
Enter a number: 5
The factorial of 5 is 120.
```

**How `factorial(5)` is evaluated**

```text
factorial(5) = 5 * factorial(4)
             = 5 * 4 * factorial(3)
             = 5 * 4 * 3 * factorial(2)
             = 5 * 4 * 3 * 2 * factorial(1)    <- base case returns 1
             = 5 * 4 * 3 * 2 * 1
             = 120
```

Each call waits on the **call stack** until the call below it returns; the results are multiplied on the way back. Without a base case the calls never stop, and Python raises `RecursionError` once the recursion limit (1000 by default) is exceeded:

```python
def no_base_case(n):
    return n * no_base_case(n - 1)  # never stops


try:
    no_base_case(5)
except RecursionError as err:
    print("RecursionError:", err)  # RecursionError: maximum recursion depth exceeded
```

| Recursion | Iteration (loop) |
|---|---|
| A function calls itself | A block repeats with `for` / `while` |
| Stops at the base case | Stops when the loop condition becomes false |
| A new stack frame per call — more memory, slower | Constant memory, usually faster |
| Short, natural code for self-similar problems (factorial, Fibonacci, tree traversal) | Better for simple repetition |
| Too many calls → `RecursionError` | No depth limit |

**Summary:** Arithmetic operators compute values (`/` gives a float, `//` floors, `%` gives the remainder, `**` is power); relational operators compare and return a `bool` and can be chained; logical operators `and`, `or`, `not` combine conditions with short-circuit evaluation. Recursion solves a problem by a function calling itself until a base case, e.g. `factorial(n) = n * factorial(n - 1)` with `factorial(0) = factorial(1) = 1`.

---

### Q5. User-defined functions — definition, arguments, return and scope

**Definition**

A function is a named block of code that performs a specific task and runs only when it is called. **Built-in functions** such as `print()`, `len()` and `max()` come with Python; a **user-defined function** is written by the programmer with the `def` keyword to perform a task according to custom requirements.

**Why use functions:** code reusability (write once, call many times), less repetition, a large program divided into small manageable parts (modularity), and easier reading, testing, debugging and maintenance.

**Function definition**

```text
def function_name(parameter1, parameter2, ...):
    """Optional docstring describing the function."""
    statement(s)
    return value          # optional
```

| Part | Meaning |
|---|---|
| `def` | Keyword that starts a function definition |
| `function_name` | Identifier used to call the function (identifier rules apply) |
| `(parameters)` | Variables that receive values from the call; may be empty |
| `:` | Marks the start of the function body |
| Docstring | Optional string on the first line of the body describing the function |
| Body | Indented statements that do the work |
| `return` | Optional; sends a value back to the caller and ends the function |

Defining a function does **not** run it; the body runs only when the function is **called** with `function_name(arguments)`.

```python
def greet():
    """Display a greeting."""
    print("Good Morning")


greet()   # function call
greet()   # a function can be called any number of times
```

Output:

```text
Good Morning
Good Morning
```

**Parameters and arguments**

- **Parameter** — the variable in the function definition (`a` and `b` in `def add(a, b)`).
- **Argument** — the actual value passed in the call (`10` and `20` in `add(10, 20)`).

```python
def add(a, b):        # a and b are parameters
    return a + b


result = add(10, 20)  # 10 and 20 are arguments
print(result)             # 30
print(add(2.5, 4))        # 6.5
print(add("Py", "thon"))  # Python
```

(`add()` is the function from [func_prgm/q1.py](func_prgm/q1.py), called here with fixed values instead of `input()`.)

**Types of arguments** (detailed in [Q10](#q10-positional-default-and-keyword-arguments))

| Type | How values reach parameters | Example |
|---|---|---|
| Positional | By position — first argument to first parameter | `power(2, 5)` |
| Default | The parameter has a default used when the argument is omitted | `def power(base, exponent=2)` then `power(3)` |
| Keyword | By parameter name, in any order | `power(exponent=5, base=2)` |
| Variable-length | `*args` collects any number of positional arguments into a tuple | `def total(*numbers)` |

```python
def total(*numbers):
    return sum(numbers)


print(total(10, 20))          # 30
print(total(10, 20, 30, 40))  # 100
```

**The `return` statement**

`return` sends a value back to the place where the function was called and immediately ends the function. The returned value can be stored, printed or used in further calculations.

- Several values separated by commas are returned together as a **tuple** (as in [func_prgm/q12.py](func_prgm/q12.py)).
- A function with no `return` statement (or a bare `return`) returns `None`.

```python
def sum_and_product(a, b):
    return a + b, a * b   # two values -> one tuple


def show(x):
    print("Value:", x)    # no return statement


total, product = sum_and_product(4, 5)
print(total, product)
print(sum_and_product(4, 5))
result = show(7)
print(result)
```

Output:

```text
9 20
(9, 20)
Value: 7
None
```

| `print()` | `return` |
|---|---|
| Displays a value on the screen | Sends a value back to the caller |
| The value cannot be reused in a calculation | The value can be stored in a variable and reused |
| The function continues after it | The function ends immediately |

**Scope of variables**

Scope is the region of the program in which a variable can be used.

- **Local variable** — created inside a function; it exists only while the function runs and cannot be used outside it (`NameError`).
- **Global variable** — created outside all functions; any function can read it.
- To **change** a global variable inside a function, declare it with the `global` keyword; otherwise an assignment creates a new local variable with the same name.
- Python looks a name up in the order **L**ocal → **E**nclosing function → **G**lobal → **B**uilt-in (the **LEGB rule**).

Based on [func_prgm/q11.py](func_prgm/q11.py):

```python
count = 10  # global variable


def show_local():
    count = 5  # local variable; hides the global one inside this function
    print("Inside show_local():", count)


def change_global():
    global count  # use the global variable
    count = count + 1
    print("Inside change_global():", count)


print("Global count:", count)
show_local()
print("After show_local():", count)
change_global()
print("After change_global():", count)
```

Output:

```text
Global count: 10
Inside show_local(): 5
After show_local(): 10
Inside change_global(): 11
After change_global(): 11
```

A local variable cannot be used outside its function:

```python
def display():
    y = 50  # local variable
    print("Inside display():", y)


display()
try:
    print(y)
except NameError as err:
    print("NameError:", err)
```

Output:

```text
Inside display(): 50
NameError: name 'y' is not defined
```

| Local variable | Global variable |
|---|---|
| Created inside a function | Created outside all functions |
| Usable only inside that function | Usable throughout the program |
| Exists only while the function runs | Exists until the program ends |
| The same name can be reused in other functions | One copy shared by all functions |
| — | Must be declared `global` to be changed inside a function |

**Putting it together** — parameters, a default argument, a docstring, a local variable and `return` in one function:

```python
def simple_interest(principal, rate, time=1):
    """Return simple interest; time defaults to 1 year."""
    interest = principal * rate * time / 100  # interest is local
    return interest


print(simple_interest(10000, 8, 2))  # 1600.0
print(simple_interest(10000, 8))     # 800.0
```

**Summary:** A user-defined function is created with `def name(parameters):`, runs only when called, receives values through positional, default, keyword or variable-length arguments, sends its result back with `return` (no `return` gives `None`), and its local variables exist only inside it while global variables are shared (changed only through `global`).

---

### Q6. String indexing and slicing

**Definition**

A string is an ordered, **immutable** sequence of characters, so every character has a position number called its **index**.

- **Indexing** — accessing one character: `s[i]`.
- **Slicing** — extracting a substring (a range of characters): `s[start:stop:step]`.

**Index positions for `s = "PYTHON"`**

```text
Character :   P    Y    T    H    O    N
+ve index :   0    1    2    3    4    5
-ve index :  -6   -5   -4   -3   -2   -1
```

Positive indexes count from the left starting at `0`; negative indexes count from the right starting at `-1`. Valid indexes run from `0` to `len(s) - 1` (or `-len(s)` to `-1`); any other index raises `IndexError`.

```python
s = "PYTHON"
print(s[0])           # P
print(s[3])           # H
print(s[-1])          # N
print(s[-3])          # H
print(s[len(s) - 1])  # N
```

```python
s = "PYTHON"
try:
    print(s[10])
except IndexError as err:
    print("IndexError:", err)
try:
    s[0] = "J"
except TypeError as err:
    print("TypeError:", err)
print("J" + s[1:])
```

Output:

```text
IndexError: string index out of range
TypeError: 'str' object does not support item assignment
JYTHON
```

A character cannot be replaced because strings are immutable — build a new string instead.

**Slicing: `s[start:stop:step]`**

- `start` — index where the slice begins (**included**); default `0`.
- `stop` — index where it ends (**excluded**); default `len(s)`.
- `step` — how far to move each time; default `1`. A negative step walks from right to left (then the defaults become the end and the start of the string).
- Slicing never raises `IndexError`: out-of-range positions are clipped to the ends of the string.
- The result is a new string; the original is unchanged.

```python
s = "PythonProgramming"
print(s[0:6])         # Python
print(s[:6])          # Python
print(s[6:])          # Programming
print(s[2:8])         # thonPr
print(s[-11:])        # Programming
print(s[-11:-7])      # Prog
print(s[::2])         # PtoPormig
print(s[1:10:3])      # yor
print(s[::-1])        # gnimmargorPnohtyP
print(s[5:100])       # nProgramming
print(repr(s[8:3]))   # ''
```

| Expression | Meaning | Result for `s = "PythonProgramming"` |
|---|---|---|
| `s[2:8]` | index 2 up to index 7 | `'thonPr'` |
| `s[:6]` | first 6 characters | `'Python'` |
| `s[6:]` | from index 6 to the end | `'Programming'` |
| `s[-11:]` | last 11 characters | `'Programming'` |
| `s[:]` | copy of the whole string | `'PythonProgramming'` |
| `s[::2]` | every second character | `'PtoPormig'` |
| `s[::-1]` | the string reversed | `'gnimmargorPnohtyP'` |
| `s[8:3]` | start after stop with a positive step | `''` (empty) |

A common use is the palindrome check:

```python
word = "madam"
print(word == word[::-1])  # True
```

| Indexing | Slicing |
|---|---|
| `s[i]` | `s[start:stop:step]` |
| Returns one character | Returns a substring (possibly empty) |
| Out-of-range index → `IndexError` | Out-of-range bounds are clipped — no error |

**Summary:** Indexing `s[i]` picks one character (`0` from the left, `-1` from the right, `IndexError` if out of range); slicing `s[start:stop:step]` returns a new substring from `start` up to but not including `stop` (defaults `0`, `len(s)`, `1`) and never raises `IndexError` — `s[::-1]` reverses a string.

---

### Q7. Functions of the statistics module

**Definition**

`statistics` is a built-in module that calculates mathematical statistics of numeric data — **central tendency** (averages) and **spread** (dispersion). Its functions take a sequence of numbers such as a list or tuple, and it must be imported first: `import statistics`. (The `math` module works on single values; `statistics` works on collections of data.)

**Measures of central tendency**

| Function | Returns | Example | Result |
|---|---|---|---|
| `mean(data)` | Arithmetic average: sum ÷ count | `mean([10, 20, 30, 40])` | `25` |
| `fmean(data)` | Mean, always as a float (faster) | `fmean([10, 20, 30, 40])` | `25.0` |
| `median(data)` | Middle value of the sorted data; mean of the two middle values if the count is even | `median([10, 20, 30, 40, 50])` / `median([10, 20, 30, 40])` | `30` / `25.0` |
| `mode(data)` | Most frequent value (the first one met if there is a tie) | `mode([1, 2, 2, 3, 4])` | `2` |
| `multimode(data)` | List of all the most frequent values | `multimode([1, 1, 2, 2, 3])` | `[1, 2]` |
| `geometric_mean(data)` | nth root of the product of n values | `geometric_mean([2, 8])` | `4.0` |
| `harmonic_mean(data)` | n ÷ (sum of reciprocals); used to average rates | `harmonic_mean([2, 3, 6])` | `3.0` |
| `quantiles(data)` | Cut points dividing the data into 4 equal groups (quartiles) | `quantiles([1, 2, 3, 4, 5, 6, 7, 8, 9])` | `[2.5, 5.0, 7.5]` |

**Measures of spread**

| Function | Returns | Divides by |
|---|---|---|
| `variance(data)` | Sample variance | n − 1 |
| `pvariance(data)` | Population variance | n |
| `stdev(data)` | Sample standard deviation = √(sample variance) | n − 1 |
| `pstdev(data)` | Population standard deviation = √(population variance) | n |

**Sample vs population:** use the *population* versions (`pvariance`, `pstdev`) when the data covers the whole group (marks of every student in the class); they divide the sum of squared deviations from the mean by **n**. Use the *sample* versions (`variance`, `stdev`) when the data is a subset used to estimate the whole group; they divide by **n − 1**, so they come out slightly larger.

```text
population variance  σ² = Σ(x − μ)² / n          standard deviation = √variance
sample variance      s² = Σ(x − x̄)² / (n − 1)
```

```python
import statistics

data = [2, 4, 4, 4, 5, 5, 7, 9]

print("Mean:", statistics.mean(data))
print("Median:", statistics.median(data))
print("Mode:", statistics.mode(data))
print("Multimode:", statistics.multimode([1, 1, 2, 2, 3]))
print("Sample variance:", statistics.variance(data))
print("Population variance:", statistics.pvariance(data))
print("Sample std dev:", statistics.stdev(data))
print("Population std dev:", statistics.pstdev(data))
```

Output:

```text
Mean: 5
Median: 4.5
Mode: 4
Multimode: [1, 2]
Sample variance: 4.571428571428571
Population variance: 4
Sample std dev: 2.138089935299395
Population std dev: 2.0
```

Here the sum of squared deviations from the mean (5) is 32, so the population variance is 32 / 8 = 4 and the sample variance is 32 / 7 ≈ 4.57.

**Interpreting variance** — small variance means consistent data, large variance means scattered data, even when the means are equal:

```python
import statistics

student_a = [48, 49, 50, 51, 52]   # daily study minutes
student_b = [10, 30, 50, 70, 90]
print(statistics.mean(student_a), statistics.mean(student_b))          # 50 50
print(statistics.variance(student_a), statistics.variance(student_b))  # 2.5 1000
print(statistics.pvariance([30, 32, 31, 29, 30]))                      # 1.04
print(statistics.pvariance([10, 25, 40, 20, 45]))                      # 166
```

> The class slide quotes population variances of 1.2 and 170 for the last two lists; Python actually gives **1.04** and **166**.

Every function above except `multimode()` (which returns `[]`) raises `statistics.StatisticsError` for empty data, and `variance()`/`stdev()` need at least two values.

**Summary:** The `statistics` module computes central tendency — `mean`, `median`, `mode`, `multimode` — and spread — `variance`/`stdev` for a sample (divide by n − 1) and `pvariance`/`pstdev` for a whole population (divide by n).

---

### Q8. Iteration — for and while loops, break, continue and pass

**Iteration** means executing a block of statements repeatedly. Python has two loops: `for` (repeat for each item of a sequence) and `while` (repeat as long as a condition is true).

**1. `for` loop**

A `for` loop repeats its body once for every item of a sequence or other iterable (string, list, tuple, dictionary, set, `range`). The loop variable takes each item in turn.

```text
for variable in sequence:
    statement(s)
```

`range()` generates the integers a `for` loop often needs:

- `range(stop)` → `0, 1, …, stop − 1`
- `range(start, stop)` → `start, …, stop − 1`
- `range(start, stop, step)` → `start, start + step, …` (stop excluded); a negative step counts down.

```python
for ch in "MCA":
    print(ch)

for i in range(1, 10, 3):
    print(i)

for i in range(5, 0, -2):
    print(i)

subjects = ["Python", "Java", "DCN"]
for position, name in enumerate(subjects, start=1):
    print(position, name)

student = {"name": "Snehal", "course": "MCA"}
for key, value in student.items():
    print(key, "->", value)

total = 0
for n in range(1, 11):
    total += n
print("Sum of 1 to 10 =", total)
```

Output:

```text
M
C
A
1
4
7
5
3
1
1 Python
2 Java
3 DCN
name -> Snehal
course -> MCA
Sum of 1 to 10 = 55
```

**2. `while` loop**

A `while` loop repeats its body as long as its condition is `True`. The condition is checked **before** every iteration, so the body may run zero times. The body must change something that the condition depends on; otherwise the loop never ends (an **infinite loop**). It is used when the number of repetitions is not known in advance.

```text
initialisation
while condition:
    statement(s)
    update
```

```python
count = 1
while count <= 5:
    print(count)
    count += 1

num = 4721
digit_sum = 0
while num > 0:
    digit_sum += num % 10   # take the last digit
    num //= 10              # drop the last digit
print("Sum of digits:", digit_sum)
```

Output:

```text
1
2
3
4
5
Sum of digits: 14
```

| Basis | `for` loop | `while` loop |
|---|---|---|
| Use when | Iterating over a sequence / number of repetitions known | Repeating until a condition changes / number unknown |
| Controlled by | Items of a sequence or `range()` | A Boolean condition |
| Initialisation and update | Automatic | Written by the programmer |
| Risk of infinite loop | Practically none | Yes, if the update is forgotten |
| Example | `for i in range(1, 6):` | `while n > 0:` |

**3. `break`, `continue` and `pass`**

| Statement | Effect |
|---|---|
| `break` | Ends the loop immediately; control passes to the first statement after the loop |
| `continue` | Skips the rest of the current iteration and starts the next one |
| `pass` | Does nothing — a placeholder where Python requires a statement |

```python
for num in range(1, 6):
    if num == 3:
        break
    print(num)
print("Loop ended")
```

Output:

```text
1
2
Loop ended
```

```python
for num in range(1, 6):
    if num == 3:
        continue
    print(num)
```

Output:

```text
1
2
4
5
```

```python
for num in range(1, 6):
    if num % 2 == 0:
        pass              # nothing to do for even numbers yet
    else:
        print(num, "is odd")


def future_feature():
    pass                  # an empty body raises IndentationError, so pass is used
```

Output:

```text
1 is odd
3 is odd
5 is odd
```

`pass` does nothing and the rest of the iteration still runs; `continue` jumps straight to the next iteration.

A loop may also have an `else` block, which runs only if the loop finishes **without** a `break` — handy for searches:

```python
for n in [3, 5, 7, 9]:
    if n % 2 == 0:
        print("Even number found:", n)
        break
else:
    print("No even number in the list")
```

Output:

```text
No even number in the list
```

**Summary:** A `for` loop iterates over the items of a sequence or a `range()` (count known); a `while` loop repeats while a condition is true (count unknown, update written by you); `break` exits the loop, `continue` skips to the next iteration, and `pass` is an empty placeholder statement.

---

### Q9. Functions of the math module

**Definition**

`math` is a built-in module that provides mathematical functions and constants for numbers. It is imported with `import math`, and its functions are called as `math.function_name()`.

**Any five functions, explained** (learn these five well)

1. **`math.sqrt(x)`** — square root of `x` (x ≥ 0); always returns a float. `math.sqrt(25)` → `5.0`.
2. **`math.pow(x, y)`** — `x` raised to the power `y`, always as a float (the `**` operator keeps integers). `math.pow(2, 3)` → `8.0`.
3. **`math.factorial(n)`** — `n!` for a non-negative integer; a negative `n` raises `ValueError` and a float such as `5.0` raises `TypeError`. `math.factorial(5)` → `120`.
4. **`math.ceil(x)`** — rounds **up** to the smallest integer ≥ `x`. `math.ceil(4.2)` → `5`.
5. **`math.floor(x)`** — rounds **down** to the largest integer ≤ `x`. `math.floor(4.8)` → `4`.

**Other functions and constants**

| Function | Purpose | Example | Result |
|---|---|---|---|
| `math.fabs(x)` | Absolute value as a float | `math.fabs(-7.5)` | `7.5` |
| `math.gcd(a, b)` | Greatest common divisor | `math.gcd(12, 18)` | `6` |
| `math.lcm(a, b)` | Least common multiple | `math.lcm(12, 18)` | `36` |
| `math.log(x, base)` | Logarithm; natural log (base e) if no base | `math.log(100, 10)` | `2.0` |
| `math.log10(x)` | Base-10 logarithm | `math.log10(1000)` | `3.0` |
| `math.sin(x)`, `math.cos(x)`, `math.tan(x)` | Trigonometric ratios of `x` **radians** | `math.cos(0)` | `1.0` |
| `math.radians(d)` | Degrees → radians | `math.radians(180)` | `3.141592653589793` |
| `math.degrees(r)` | Radians → degrees | `math.degrees(math.pi)` | `180.0` |
| `math.pi`, `math.e` | Constants π and e (values, not functions) | `math.e` | `2.718281828459045` |

```python
import math

print(math.sqrt(25))                         # 5.0
print(math.pow(2, 3), 2 ** 3)                # 8.0 8
print(math.factorial(5))                     # 120
print(math.ceil(4.2), math.floor(4.8))       # 5 4
print(math.ceil(-4.2), math.floor(-4.2))     # -4 -5
print(math.fabs(-7.5), abs(-7))              # 7.5 7
print(math.gcd(12, 18), math.lcm(12, 18))    # 6 36
print(math.log(math.e), math.log(100, 10), math.log10(1000))  # 1.0 2.0 3.0
print(math.sin(math.radians(30)))            # 0.49999999999999994
print(round(math.sin(math.radians(30)), 2))  # 0.5
print(math.cos(0), math.degrees(math.pi))    # 1.0 180.0
print(math.pi, math.e)                       # 3.141592653589793 2.718281828459045
```

`sin(30°)` prints `0.49999999999999994` instead of `0.5` because π cannot be stored exactly as a float; round the result for display.

**Program using math functions** — the class example: a person sees the top of a building 20 m away (along the line of sight) at an angle of elevation of 30°. Find the building's height and the person's distance from it.

```python
import math

hypotenuse = 20              # line of sight to the top of the building, in m
angle = math.radians(30)     # sin() and cos() need radians

height = hypotenuse * math.sin(angle)
distance = hypotenuse * math.cos(angle)
print("Height of building:", round(height, 2), "m")
print("Distance from building:", round(distance, 2), "m")
print("Check with sqrt:", round(math.sqrt(height ** 2 + distance ** 2), 2), "m")
```

Output:

```text
Height of building: 10.0 m
Distance from building: 17.32 m
Check with sqrt: 20.0 m
```

Functions can also be imported by name, so no `math.` prefix is needed:

```python
from math import sqrt, pi

print(sqrt(49), round(pi, 4))  # 7.0 3.1416
```

**Summary:** The `math` module (`import math`) provides `sqrt`, `pow` (float result), `factorial`, `ceil`/`floor`, `fabs`, `gcd`/`lcm`, `log`/`log10` and the trigonometric functions `sin`/`cos`/`tan` (which take radians — convert with `radians()`), plus the constants `pi` and `e`.

---

### Q10. Positional, default and keyword arguments

Arguments are the values passed to a function's parameters when it is called. Python can match them to parameters by **position**, by a **default** value, or by **keyword** (parameter name).

**1. Positional arguments**

Values are assigned to parameters strictly in order — the first argument to the first parameter, the second to the second, and so on. The number of arguments must match the number of parameters, and the **order matters**.

```python
def student(name, age):
    print("Name:", name, "| Age:", age)


student("Rahul", 20)
student(20, "Rahul")   # wrong order -> wrong values, but no error
```

Output:

```text
Name: Rahul | Age: 20
Name: 20 | Age: Rahul
```

A missing positional argument is an error (function from [func_prgm/q2.py](func_prgm/q2.py)):

```python
def area_of_rectangle(length, breadth):
    return length * breadth


print(area_of_rectangle(5, 3))
try:
    area_of_rectangle(5)
except TypeError as err:
    print("TypeError:", err)
```

Output:

```text
15
TypeError: area_of_rectangle() missing 1 required positional argument: 'breadth'
```

**2. Default arguments**

A default argument is a parameter given a default value in the definition (`parameter=value`). If the caller omits that argument the default is used; if a value is passed it overrides the default. Default arguments make parameters optional, and they must come **after** all non-default parameters.

```python
def power(base, exponent=2):    # from func_prgm/q3.py
    return base ** exponent


def greet(name, message="Good Morning"):
    print(message + ",", name)


print(power(5))                  # exponent takes its default, 2
print(power(5, 3))               # 3 overrides the default
greet("Priya")
greet("Priya", "Good Evening")
```

Output:

```text
25
125
Good Morning, Priya
Good Evening, Priya
```

**3. Keyword arguments**

In a keyword argument the caller names the parameter (`parameter=value`), so the **order does not matter** and the call documents itself. Positional and keyword arguments can be mixed, but positional ones must come first.

```python
def student_details(name, roll_number, course):   # from func_prgm/q4.py
    print(f"Name: {name}, Roll No: {roll_number}, Course: {course}")


student_details(course="MCA", name="Vidit", roll_number=21)
student_details("Vidit", course="MCA", roll_number=21)
```

Output:

```text
Name: Vidit, Roll No: 21, Course: MCA
Name: Vidit, Roll No: 21, Course: MCA
```

**Rules when mixing them** (error messages as Python 3.14 prints them)

1. In a **call**, positional arguments come before keyword arguments — `student(name="Rahul", 20)` is `SyntaxError: positional argument follows keyword argument`.
2. In a **definition**, non-default parameters come before default ones — `def f(a=1, b):` is `SyntaxError: parameter without a default follows parameter with a default`.
3. A parameter receives only one value — `student("Rahul", name="Amit")` raises `TypeError: student() got multiple values for argument 'name'`.

**All three in one function**

```python
def bill(item, price, quantity=1, discount=0):
    total = price * quantity * (1 - discount / 100)
    print(f"{item}: Rs. {total}")


bill("Pen", 10)                            # positional; both defaults used
bill("Notebook", 50, 4)                    # positional; quantity overrides its default
bill("Bag", 800, discount=10)              # keyword argument skips quantity
bill(price=120, item="File", quantity=2)   # all keyword, any order
```

Output:

```text
Pen: Rs. 10.0
Notebook: Rs. 200.0
Bag: Rs. 720.0
File: Rs. 240.0
```

| Basis | Positional | Default | Keyword |
|---|---|---|---|
| Written in | The call, by order | The definition (`param=value`) | The call (`param=value`) |
| Matched by | Position | Used when the argument is omitted | Parameter name |
| Order matters? | Yes | Must follow non-default parameters in the definition | No |
| Compulsory? | Yes | No — optional | Only if the parameter has no default |
| Example | `power(2, 5)` | `def power(base, exponent=2)` → `power(3)` | `power(exponent=5, base=2)` |

**Summary:** Positional arguments are matched by order, default arguments supply a value when one is omitted (defaults go last in the definition), and keyword arguments are matched by parameter name so their order does not matter (they go after positional arguments in a call).

---

### Q11. Input and output statements

**Input: `input()`**

`input(prompt)` displays the prompt, waits for the user to type a line and press Enter, and returns the typed text — **always as a string (`str`)**, even if digits are typed. To use the value as a number, convert it with `int()` or `float()` (**type conversion**).

```text
variable = input("prompt message")
```

```python
a = input("Enter first number: ")
b = input("Enter second number: ")
print(type(a))
print("Without conversion:", a + b)
print("With conversion:", int(a) + int(b))
```

Sample run:

```text
Enter first number: 10
Enter second number: 20
<class 'str'>
Without conversion: 1020
With conversion: 30
```

Without conversion, `+` joins the two strings. `int("12.5")` raises `ValueError: invalid literal for int() with base 10: '12.5'`, so use `float()` for decimal input.

**Reading different kinds of input**

- `int(input())`, `float(input())` — one number.
- `input().split()` — splits the line at spaces into a list of strings.
- `map(int, input().split())` — applies `int()` to every piece; unpack into variables or wrap in `list()`.

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
percentage = float(input("Enter your percentage: "))
a, b = map(int, input("Enter two numbers: ").split())
marks = list(map(int, input("Enter marks separated by spaces: ").split()))

print("Name:", name, "| Age next year:", age + 1)
print("Percentage:", percentage, "| Sum:", a + b)
print("Marks:", marks, "| Total:", sum(marks))
print(type(name), type(age), type(percentage), type(marks))
```

Sample run:

```text
Enter your name: Vidit
Enter your age: 22
Enter your percentage: 89.5
Enter two numbers: 4 6
Enter marks separated by spaces: 78 85 92
Name: Vidit | Age next year: 23
Percentage: 89.5 | Sum: 10
Marks: [78, 85, 92] | Total: 255
<class 'str'> <class 'int'> <class 'float'> <class 'list'>
```

**Output: `print()`**

```text
print(value1, value2, ..., sep=" ", end="\n")
```

`print()` displays its values separated by `sep` (default one space) and then writes `end` (default a newline). Escape sequences such as `\n` (new line), `\t` (tab), `\\` and `\"` can be used inside strings.

```python
print("Python", "is", "fun")
print("16", "10", "2026", sep="/")
print("Loading", end="...")
print("done")
print("Name: Vidit\nCourse: MCA")
```

Output:

```text
Python is fun
16/10/2026
Loading...done
Name: Vidit
Course: MCA
```

**Formatted output**

| Method | Example | Output |
|---|---|---|
| f-string (Python 3.6+) | `f"{name} scored {marks:.2f} marks"` | `Vidit scored 89.46 marks` |
| `str.format()` | `"{} scored {:.1f} marks".format(name, marks)` | `Vidit scored 89.5 marks` |
| `%` formatting (old style) | `"%s scored %d marks" % (name, marks)` | `Vidit scored 89 marks` |

```python
name, marks = "Vidit", 89.456
print(f"{name} scored {marks:.2f} marks")                      # Vidit scored 89.46 marks
print("{} scored {:.1f} marks".format(name, marks))            # Vidit scored 89.5 marks
print("{0} is in MCA; {0}'s roll no is {1}".format(name, 21))  # Vidit is in MCA; Vidit's roll no is 21
print("%s scored %d marks" % (name, marks))                    # Vidit scored 89 marks
```

`:.2f` rounds to two decimal places; `{0}` and `{1}` refer to `format()`'s arguments by position, so one can be reused; `%d` drops the fractional part.

**Summary:** `input()` reads a line from the keyboard and always returns a string, so numbers must be converted with `int()`/`float()` (`split()` with `map()` for several values on one line); `print()` displays values separated by `sep` and followed by `end`, and f-strings or `format()` produce formatted output.

---

### Q12. Lists — adding, finding, updating, nesting, looping, sorting, concatenation, slicing

**Definition**

A list is an **ordered, mutable** sequence of elements enclosed in square brackets `[]` and separated by commas.

- **Ordered** — elements keep their order and are accessed by index (from `0`; negative indexes from `-1`).
- **Mutable** — elements can be changed, added and removed after creation.
- **Heterogeneous** — one list can hold integers, floats, strings, even other lists.
- **Duplicates allowed.**

```python
empty = []
numbers = [10, 20, 30, 40, 50]
mixed = [1, "Python", 3.5, True]
print(empty, numbers, mixed)                   # [] [10, 20, 30, 40, 50] [1, 'Python', 3.5, True]
print(list((1, 2, 3)), list(range(1, 6)))      # [1, 2, 3] [1, 2, 3, 4, 5]
print(list("abc"))                             # ['a', 'b', 'c']
print(numbers[0], numbers[-1], len(numbers))   # 10 50 5
```

**1. Adding items**

| Method | Adds | Example |
|---|---|---|
| `append(x)` | One item at the end | `nums.append(40)` |
| `insert(i, x)` | One item at index `i` (later items shift right) | `nums.insert(1, 15)` |
| `extend(iterable)` | Each item of another iterable at the end | `nums.extend([50, 60])` |

```python
nums = [10, 20, 30]
nums.append(40)
print(nums)            # [10, 20, 30, 40]
nums.insert(1, 15)
print(nums)            # [10, 15, 20, 30, 40]
nums.extend([50, 60])
print(nums)            # [10, 15, 20, 30, 40, 50, 60]
nums.append([70, 80])
print(nums)            # [10, 15, 20, 30, 40, 50, 60, [70, 80]]
```

The last `append()` added the list `[70, 80]` as a single element; `extend()` adds the elements one by one.

Items are often added from user input in a loop:

```python
numbers = []
n = int(input("How many numbers? "))
for i in range(n):
    numbers.append(int(input("Enter number: ")))
print("List:", numbers)
```

Sample run:

```text
How many numbers? 3
Enter number: 5
Enter number: 8
Enter number: 2
List: [5, 8, 2]
```

**2. Finding an item**

- `x in list` / `x not in list` — whether the item is present (`True`/`False`).
- `list.index(x)` — index of the first occurrence; raises `ValueError` if `x` is absent, so check with `in` first.
- `list.count(x)` — how many times `x` occurs.

**3. Updating an item**

- By index: `list[i] = new_value`.
- By value: find the index first, then assign — `list[list.index(old)] = new`.
- Several items at once with slice assignment: `list[1:3] = [...]`.

```python
nums = [10, 20, 30, 20, 40]
print(30 in nums)        # True
print(99 not in nums)    # True
print(nums.index(20))    # 1
print(nums.count(20))    # 2

nums[0] = 11             # update by index
pos = nums.index(30)     # find the position, then update
nums[pos] = 35
print(nums)              # [11, 20, 35, 20, 40]
nums[1:3] = [21, 31]     # update a slice
print(nums)              # [11, 21, 31, 20, 40]
```

Checking with `in` before calling `index()` avoids the `ValueError` for a missing item:

```python
nums = [11, 21, 31, 20, 40]
target = 99
if target in nums:
    print(target, "found at index", nums.index(target))
else:
    print(target, "not found")
```

Output:

```text
99 not found
```

**4. Nested lists**

A nested list is a list whose elements are themselves lists — useful for tables and matrices. An inner element is reached with two indexes, `list[row][column]`.

```python
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print(matrix[1])                     # [4, 5, 6]
print(matrix[1][2])                  # 6
matrix[2][0] = 70
print(matrix[2])                     # [70, 8, 9]
print(len(matrix), len(matrix[0]))   # 3 3
```

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    print(row, "sum =", sum(row))

total = 0
for row in matrix:          # nested loop visits every element
    for value in row:
        total += value
print("Total of all elements:", total)
```

Output:

```text
[1, 2, 3] sum = 6
[4, 5, 6] sum = 15
[7, 8, 9] sum = 24
Total of all elements: 45
```

**5. Looping through a list**

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:                 # 1. over the elements
    print(fruit)

for i in range(len(fruits)):         # 2. over the indexes
    print(i, fruits[i])

for i, fruit in enumerate(fruits):   # 3. index and element together
    print(i, fruit.upper())

i = 0
while i < len(fruits):               # 4. while loop with an index
    print(fruits[i][0])
    i += 1
```

Output:

```text
apple
banana
cherry
0 apple
1 banana
2 cherry
0 APPLE
1 BANANA
2 CHERRY
a
b
c
```

**6. Sorting**

- `list.sort()` sorts the list **in place** in ascending order and returns `None`.
- `list.sort(reverse=True)` sorts in descending order.
- `sorted(list)` returns a **new** sorted list and leaves the original unchanged.
- `key=` sorts by a computed value, e.g. `key=len` sorts strings by length.
- The elements must be comparable with each other: sorting `[3, "a"]` raises `TypeError`.

```python
nums = [50, 20, 40, 10, 30]
nums.sort()
print(nums)               # [10, 20, 30, 40, 50]
nums.sort(reverse=True)
print(nums)               # [50, 40, 30, 20, 10]

marks = [72, 95, 64]
print(sorted(marks))      # [64, 72, 95]
print(marks)              # [72, 95, 64]

names = ["Riya", "Al", "Vidit"]
names.sort(key=len)
print(names)              # ['Al', 'Riya', 'Vidit']
```

**7. Concatenation**

- `+` joins two lists into a **new** list; the original lists are unchanged. Both operands must be lists.
- `*` repeats a list.
- `+=` (or `extend()`) adds to an existing list in place.

```python
odd = [1, 3, 5]
even = [2, 4, 6]
combined = odd + even
print(combined)    # [1, 3, 5, 2, 4, 6]
print(odd)         # [1, 3, 5]
print([0] * 4)     # [0, 0, 0, 0]
odd += [7]
print(odd)         # [1, 3, 5, 7]
try:
    odd + "ab"
except TypeError as err:
    print("TypeError:", err)  # TypeError: can only concatenate list (not "str") to list
```

**8. Slicing**

`list[start:stop:step]` returns a new list from `start` up to but not including `stop`, with the same rules as string slicing ([Q6](#q6-string-indexing-and-slicing)).

```python
nums = [10, 20, 30, 40, 50, 60]
print(nums[1:4])        # [20, 30, 40]
print(nums[:3])         # [10, 20, 30]
print(nums[3:])         # [40, 50, 60]
print(nums[-2:])        # [50, 60]
print(nums[::2])        # [10, 30, 50]
print(nums[::-1])       # [60, 50, 40, 30, 20, 10]
print(nums[:] is nums)  # False
```

`nums[:]` is a new list — that is why slicing can clone a list ([Q2](#q2-cloning-aliasing-and-mutability-of-lists)).

**Summary:** A list is an ordered, mutable, heterogeneous collection in `[]`: add items with `append`/`insert`/`extend`, find them with `in`/`index()`/`count()`, update with `list[i] = value`, nest lists and access them as `m[row][col]`, traverse with `for`/`while`, sort with `sort()`/`sorted()`, join with `+` and extract parts with `[start:stop:step]`.

---

### Q13. List methods — adding, removing, reversing and sorting

**Definition**

List methods are built-in functions that belong to the list type and are called with dot notation: `list_name.method(arguments)`. Most of them change the list **in place** and return `None`; `pop()`, `index()`, `count()` and `copy()` return a value.

Each example starts from `nums = [10, 20, 30]`:

| Purpose | Method and syntax | Description | Example | Result |
|---|---|---|---|---|
| Add | `list.append(x)` | Adds `x` as one element at the end | `nums.append(40)` | `[10, 20, 30, 40]` |
| Add | `list.insert(i, x)` | Inserts `x` before index `i` | `nums.insert(1, 15)` | `[10, 15, 20, 30]` |
| Add | `list.extend(iterable)` | Adds each element of the iterable at the end | `nums.extend([40, 50])` | `[10, 20, 30, 40, 50]` |
| Remove | `list.remove(x)` | Removes the first occurrence of the **value** `x`; `ValueError` if absent | `nums.remove(20)` | `[10, 30]` |
| Remove | `list.pop(i)` | Removes and **returns** the element at **index** `i` (the last one if `i` is omitted) | `nums.pop()` | returns `30`; list `[10, 20]` |
| Remove | `list.clear()` | Removes all elements | `nums.clear()` | `[]` |
| Search | `list.index(x)` | Index of the first occurrence of `x`; `ValueError` if absent | `nums.index(30)` | `2` |
| Search | `list.count(x)` | Number of times `x` occurs | `nums.count(20)` | `1` |
| Arrange | `list.sort(key=None, reverse=False)` | Sorts in place, ascending by default | `nums.sort(reverse=True)` | `[30, 20, 10]` |
| Arrange | `list.reverse()` | Reverses the current order in place (does not sort) | `nums.reverse()` | `[30, 20, 10]` |
| Copy | `list.copy()` | Returns a shallow copy (a clone) | `b = nums.copy()` | `b` is `[10, 20, 30]` |

Related tools that are *not* methods: the `del list[i]` statement (removes by index or slice) and the built-in functions `len()`, `max()`, `min()`, `sum()` and `sorted()`, which take the list as an argument.

**Demonstration: adding, removing, reversing and sorting**

```python
marks = [72, 45, 90]
print("Original:", marks)

# Adding
marks.append(66)
marks.insert(0, 88)
marks.extend([54, 79])
print("After adding:", marks)

# Removing
marks.remove(45)
last = marks.pop()
second = marks.pop(1)
print("Popped:", last, "and", second)
print("After removing:", marks)

# Reversing
marks.reverse()
print("Reversed:", marks)

# Sorting
marks.sort()
print("Ascending:", marks)
marks.sort(reverse=True)
print("Descending:", marks)

# Searching and counting
print("Index of 66:", marks.index(66))
print("Count of 90:", marks.count(90))
```

Output:

```text
Original: [72, 45, 90]
After adding: [88, 72, 45, 90, 66, 54, 79]
Popped: 79 and 72
After removing: [88, 90, 66, 54]
Reversed: [54, 66, 90, 88]
Ascending: [54, 66, 88, 90]
Descending: [90, 88, 66, 54]
Index of 66: 2
Count of 90: 1
```

**Common mistakes**

```python
nums = [3, 1, 2]
result = nums.sort()
print(result)    # None
print(nums)      # [1, 2, 3]

nums.append([4, 5])
print(nums)      # [1, 2, 3, [4, 5]]
nums.pop()
nums.extend([4, 5])
print(nums)      # [1, 2, 3, 4, 5]

try:
    nums.remove(99)
except ValueError as err:
    print("ValueError:", err)  # ValueError: list.remove(x): x not in list
```

`sort()` returns `None` — use `sorted()` when a new list is needed; `append()` adds its argument as one element; `remove()` fails when the value is absent.

| | `remove(x)` | `pop(i)` | `del list[i]` | `clear()` |
|---|---|---|---|---|
| Removes by | Value | Index (default: last) | Index or slice | Everything |
| Returns | `None` | The removed element | — (a statement) | `None` |
| Error when missing | `ValueError` | `IndexError` | `IndexError` | — |

| `sort()` | `sorted()` | `reverse()` |
|---|---|---|
| List method | Built-in function, works on any iterable | List method |
| Sorts the list in place | Returns a new sorted list | Reverses the existing order in place |
| Returns `None` | Returns the new list | Returns `None` |

**Summary:** List methods are called as `list.method()`: `append`, `insert` and `extend` add; `remove`, `pop` and `clear` remove; `index` and `count` search; `sort` and `reverse` rearrange in place; `copy` clones — most return `None` because they change the list itself.

---

## Part B — Programs (Q14–Q19)

Each program reads its input from the keyboard. The sample runs show the screen exactly, with the typed input after each prompt.

### Q14. List operations — create, add, find and update, display, sort

Student's solution: [lec/oct_1/oct_1_q1.py](lec/oct_1/oct_1_q1.py) (reproduced below with the part labels added as comments).

```python
# a) Create a list of numbers
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Original list:", numbers)

# b) Add an element to the list
new_number = int(input("Enter a number to add: "))
numbers.append(new_number)

# c) Find and update an element
target = int(input("Enter the number to find and update: "))
found = False
for index in range(len(numbers)):
    if numbers[index] == target:
        replacement = int(input("Enter its replacement value: "))
        numbers[index] = replacement
        found = True
        break

if found:
    print("The element was updated.")
else:
    print("The element was not found.")

# d) Display the elements using a loop
print("List elements:")
for number in numbers:
    print(number)

# e) Sort the list
numbers.sort()
print("Sorted list:", numbers)
```

Sample run:

```text
Enter numbers separated by spaces: 50 20 40 10
Original list: [50, 20, 40, 10]
Enter a number to add: 30
Enter the number to find and update: 40
Enter its replacement value: 45
The element was updated.
List elements:
50
20
45
10
30
Sorted list: [10, 20, 30, 45, 50]
```

**Logic**

- a) `input().split()` breaks the typed line into strings, `map(int, …)` converts each to an integer and `list()` collects them.
- b) `append()` adds the new number at the end.
- c) The loop compares each element with the target; on a match it replaces the element with `numbers[index] = replacement` and `break` stops the search. The `found` flag records whether a match occurred. (Shorter alternative: `if target in numbers: numbers[numbers.index(target)] = replacement`.)
- d) `for number in numbers` prints the elements one per line.
- e) `sort()` arranges the list in ascending order in place.

---

### Q15. Even/odd, sign, factorial, table and divisibility by 5 and 7

Student's solution: [lec/oct_1/oct_1_q2.py](lec/oct_1/oct_1_q2.py) (part labels added as comments).

```python
number = int(input("Enter an integer: "))

# i. Even or odd
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# ii. Positive or negative
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# iii. Factorial
if number < 0:
    print("Factorial is not defined for negative integers.")
else:
    factorial = 1
    for value in range(1, number + 1):
        factorial = factorial * value
    print("Factorial:", factorial)

# iv. Multiplication table
print("Multiplication table:")
for multiplier in range(1, 11):
    print(number, "x", multiplier, "=", number * multiplier)

# v. Divisible by both 5 and 7
if number % 5 == 0 and number % 7 == 0:
    print("The number is divisible by both 5 and 7.")
else:
    print("The number is not divisible by both 5 and 7.")
```

Sample run:

```text
Enter an integer: 35
The number is odd.
The number is positive.
Factorial: 10333147966386144929666651337523200000000
Multiplication table:
35 x 1 = 35
35 x 2 = 70
35 x 3 = 105
35 x 4 = 140
35 x 5 = 175
35 x 6 = 210
35 x 7 = 245
35 x 8 = 280
35 x 9 = 315
35 x 10 = 350
The number is divisible by both 5 and 7.
```

**Logic**

- i. `number % 2` is the remainder after dividing by 2: `0` means even.
- ii. `if`–`elif`–`else` separates positive, negative and zero.
- iii. The factorial is the product `1 × 2 × … × n`, built up in a `for` loop starting from `factorial = 1`. For `0` the loop runs zero times, giving `0! = 1`; negative numbers have no factorial. Python integers have unlimited size, so even `35!` is exact.
- iv. `range(1, 11)` gives the multipliers 1 to 10.
- v. Both conditions are joined with `and` (equivalently, `number % 35 == 0`).

---

### Q16. Sum and average using a user-defined function

The student's [lec/oct_1/oct_1_q3.py](lec/oct_1/oct_1_q3.py) calculates the sum and average directly in the main program and **does not define a function**, which the question requires. The version below moves the calculation into a user-defined function that returns both values; the prompts and output are unchanged.

```python
def sum_and_average(numbers):
    total = 0
    for number in numbers:
        total = total + number
    average = total / len(numbers)
    return total, average          # two values returned as a tuple


count = int(input("How many numbers will you enter? "))

if count <= 0:
    print("Please enter at least one number.")
else:
    numbers = []
    for index in range(count):
        number = float(input("Enter a number: "))
        numbers.append(number)

    total, average = sum_and_average(numbers)   # function call
    print("Sum:", total)
    print("Average:", average)
```

Sample run:

```text
How many numbers will you enter? 4
Enter a number: 10
Enter a number: 20
Enter a number: 30
Enter a number: 45
Sum: 105.0
Average: 26.25
```

**Logic**

- `def sum_and_average(numbers):` — the parameter receives the whole list.
- The loop adds every element to `total`; `average = total / len(numbers)`.
- `return total, average` sends both results back as a tuple, which the call unpacks with `total, average = sum_and_average(numbers)`.
- The `count <= 0` check prevents a division by zero.
- Inside the function, `total = sum(numbers)` is a valid one-line replacement for the loop.

---

### Q17. Digits of a number using a while loop

Student's solution: [lec/oct_1/oct_1_q4.py](lec/oct_1/oct_1_q4.py) (part labels added as comments).

```python
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
        digit = remaining % 10                  # last digit
        print(digit)                            # i. display each digit
        digit_sum = digit_sum + digit           # ii. sum
        digit_product = digit_product * digit   # iii. product
        digit_count = digit_count + 1           # iv. count
        reverse = reverse * 10 + digit          # v. reverse
        remaining = remaining // 10             # drop the last digit

if number < 0:
    reverse = -reverse

print("Sum of digits:", digit_sum)
print("Product of digits:", digit_product)
print("Number of digits:", digit_count)
print("Reversed number:", reverse)
```

Sample run:

```text
Enter an integer: 12345
Digits:
5
4
3
2
1
Sum of digits: 15
Product of digits: 120
Number of digits: 5
Reversed number: 54321
```

**Dry run for 12345** (values after each pass of the loop)

| Pass | `remaining` before | `digit` | `digit_sum` | `digit_product` | `digit_count` | `reverse` |
|---|---|---|---|---|---|---|
| 1 | 12345 | 5 | 5 | 5 | 1 | 5 |
| 2 | 1234 | 4 | 9 | 20 | 2 | 54 |
| 3 | 123 | 3 | 12 | 60 | 3 | 543 |
| 4 | 12 | 2 | 14 | 120 | 4 | 5432 |
| 5 | 1 | 1 | 15 | 120 | 5 | 54321 |

**Logic**

- `remaining % 10` extracts the last digit and `remaining // 10` removes it; the loop stops when `remaining` reaches 0.
- Because the last digit comes out first, the digits are displayed from right to left.
- `reverse = reverse * 10 + digit` shifts the reversed number one place left and appends the digit.
- `abs()` lets negative input work (the sign is put back on the reverse at the end), and 0 is handled separately because the loop would not run for it.

---

### Q18. Display, largest, smallest, sum and average of a list

Student's solution: [lec/oct_1/oct_1_q5.py](lec/oct_1/oct_1_q5.py).

Item iii reads "Find the smallest element in the list function"; it is taken to mean *find it using the built-in `min()` function*. The student's file finds the smallest element with a loop (its header comment says "using a function", but the code uses a loop), so the version below uses `min()` for item iii and the loop approach is shown after it. The output is the same either way.

```python
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

if len(numbers) == 0:
    print("Please enter at least one number.")
else:
    largest = numbers[0]
    total = 0

    print("List elements:")                # i. display
    for number in numbers:
        print(number)
        total = total + number             # iv. sum
        if number > largest:               # ii. largest
            largest = number

    smallest = min(numbers)                # iii. built-in min() function
    average = total / len(numbers)         # v. average
    print("Largest element:", largest)
    print("Smallest element:", smallest)
    print("Sum of elements:", total)
    print("Average of elements:", average)
```

Sample run:

```text
Enter numbers separated by spaces: 42 7 19 88 3
List elements:
42
7
19
88
3
Largest element: 88
Smallest element: 3
Sum of elements: 159
Average of elements: 31.8
```

**Loop approach for iii** (as in the student's file), and the built-in shortcuts for every part:

```python
numbers = [42, 7, 19, 88, 3]

smallest = numbers[0]          # assume the first element is the smallest
for number in numbers:
    if number < smallest:
        smallest = number
print("Smallest (loop):", smallest)  # Smallest (loop): 3

print(max(numbers), min(numbers), sum(numbers), sum(numbers) / len(numbers))  # 88 3 159 31.8
```

**Logic**

- One loop displays each element, adds it to `total` and keeps the largest value seen so far (starting from the first element).
- `min()` returns the smallest element directly; the loop version compares every element with the smallest found so far.
- Average = `total / len(numbers)`; the empty-list check prevents a division by zero.

---

### Q19. Count and sum of even and odd elements

Student's solution: [lec/oct_1/oct_1_q6.py](lec/oct_1/oct_1_q6.py) (part labels added as comments).

```python
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

even_count = 0
odd_count = 0
even_sum = 0
odd_sum = 0

print("List elements:")
for number in numbers:
    print(number)                         # i. display using a loop
    if number % 2 == 0:
        even_count = even_count + 1       # ii. count even
        even_sum = even_sum + number      # iv. sum of even
    else:
        odd_count = odd_count + 1         # iii. count odd
        odd_sum = odd_sum + number        # v. sum of odd

print("Number of even elements:", even_count)
print("Number of odd elements:", odd_count)
print("Sum of even elements:", even_sum)
print("Sum of odd elements:", odd_sum)
```

Sample run:

```text
Enter numbers separated by spaces: 12 7 9 4 15 6
List elements:
12
7
9
4
15
6
Number of even elements: 3
Number of odd elements: 3
Sum of even elements: 22
Sum of odd elements: 31
```

**Logic**

- Four accumulators start at 0; a single loop visits every element once.
- `number % 2 == 0` decides even or odd; the matching counter is incremented and the number is added to the matching sum.
- Negative numbers are classified correctly too, because in Python `-7 % 2` is `1`.

---

## Quick revision sheet

| Q | One-line answer |
|---|---|
| 1 | Types: `int`, `float`, `complex`, `bool`, `str`, `list`, `tuple`, `range`, `set`, `frozenset`, `dict`, `NoneType`; variable = name bound to a value; identifier = name of letters/digits/`_`, no leading digit, not a keyword, case-sensitive; keywords = reserved words (`keyword.kwlist`); literal = fixed value in code |
| 2 | Lists are mutable; `b = a` is aliasing (same object, `a is b`); `a[:]`, `list(a)`, `a.copy()` clone (shallow); nested lists need `copy.deepcopy()` |
| 3 | `=`, `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=` and walrus `:=`; `in`/`not in` test presence (keys for a dict); `is`/`is not` test same object, `==` tests equal value |
| 4 | `/` float, `//` floor, `%` remainder, `**` power; relational operators return a bool and can chain; `and`/`or` short-circuit; recursion = base case + recursive case, `fact(n) = n * fact(n - 1)` |
| 5 | `def name(params):` + body + optional `return`; runs only when called; positional/default/keyword/`*args` arguments; no `return` → `None`; local vs global scope, `global` to modify |
| 6 | `s[i]` one character (`0…len-1` or `-1…-len`, else `IndexError`); `s[start:stop:step]` substring, stop excluded, no `IndexError`; `s[::-1]` reverses; strings are immutable |
| 7 | `mean`, `median`, `mode`, `multimode`; `variance`/`stdev` = sample (n − 1), `pvariance`/`pstdev` = population (n) |
| 8 | `for` over a sequence / `range()` (count known), `while` on a condition (count unknown); `break` exits, `continue` skips to the next iteration, `pass` does nothing |
| 9 | `import math`: `sqrt`, `pow` (float), `factorial`, `ceil`/`floor`, `fabs`, `gcd`/`lcm`, `log`/`log10`, `sin`/`cos` (radians), `radians`/`degrees`, `pi`, `e` |
| 10 | Positional = by order; default = `param=value` in the definition, used when omitted, placed last; keyword = `param=value` in the call, any order, after positional ones |
| 11 | `input()` always returns `str` → `int()`/`float()`, several values with `split()` + `map()`; `print(values, sep=" ", end="\n")`, f-strings, `format()` |
| 12 | Ordered, mutable, mixed, duplicates allowed; add (`append`, `insert`, `extend`), find (`in`, `index`, `count`), update (`l[i] = v`), nested (`m[r][c]`), loop (`for`/`while`), sort (`sort`, `sorted`), `+` joins, `[start:stop:step]` slices |
| 13 | `append`/`insert`/`extend` add, `remove` (value)/`pop` (index)/`clear` remove, `index`/`count` search, `sort`/`reverse` rearrange in place and return `None`, `copy` clones |
| 14 | `list(map(int, input().split()))` → `append()` → loop to find, `l[i] = new`, `break` → `for` to display → `sort()` |
| 15 | `% 2` for even/odd, `if`–`elif`–`else` for the sign, loop product for the factorial, `range(1, 11)` for the table, `n % 5 == 0 and n % 7 == 0` |
| 16 | `def sum_and_average(numbers): … return total, average`, then `total, average = sum_and_average(numbers)` |
| 17 | `while n > 0:` take `d = n % 10`, update sum, product, count and `rev = rev * 10 + d`, then `n //= 10` |
| 18 | One loop for display, sum and largest; `min(numbers)` for the smallest; average = sum / len |
| 19 | One loop with `if n % 2 == 0` updating two counters and two sums |

**Traps examiners like**

- `input()` returns a string: `"10" + "20"` is `"1020"`.
- `/` always gives a float (`10 / 2` is `5.0`); `//` rounds down, so `-7 // 2` is `-4`.
- `=` assigns, `==` compares values, `is` compares identity.
- `b = a` does not copy a list; `list.sort()` returns `None`.
- `append([4, 5])` adds one element; `extend([4, 5])` adds two.
- A slice's `stop` index is excluded, and slicing never raises `IndexError`.
- A recursive function without a base case ends in `RecursionError`.
- `math.pow(2, 3)` is `8.0`, while `2 ** 3` is `8`.
