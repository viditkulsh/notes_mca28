# Match a string containing only digits.

import re

pattern = r"^\d+$"
strings = ["12345", "123abc", "2026", ""]

print("Pattern:", pattern)
for s in strings:
    if re.search(pattern, s):
        print(repr(s), "-> Match")
    else:
        print(repr(s), "-> No match")
