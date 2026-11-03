# Match a string containing exactly 4 characters.

import re

pattern = r"^.{4}$"
strings = ["Java", "Python", "C++", "Code", "ab c"]

print("Pattern:", pattern)
for s in strings:
    if re.search(pattern, s):
        print(repr(s), "-> Match")
    else:
        print(repr(s), "-> No match")
