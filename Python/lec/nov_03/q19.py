# Match a string ending with Python.

import re

pattern = r"Python$"
strings = ["I love Python", "Python is fun", "Learn Python", "python"]

print("Pattern:", pattern)
for s in strings:
    if re.search(pattern, s):
        print(repr(s), "-> Match")
    else:
        print(repr(s), "-> No match")
