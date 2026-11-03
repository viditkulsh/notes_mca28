# Match a string ending with a digit.

import re

pattern = r"\d$"
strings = ["Room 5", "MCA", "Version 3.14", "Lab"]

print("Pattern:", pattern)
for s in strings:
    if re.search(pattern, s):
        print(repr(s), "-> Match")
    else:
        print(repr(s), "-> No match")
