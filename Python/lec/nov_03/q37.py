# Match a string starting with a digit.

import re

pattern = r"^\d"
strings = ["2026 batch", "MCA 2026", "9am class", "Room 5"]

print("Pattern:", pattern)
for s in strings:
    if re.search(pattern, s):
        print(repr(s), "-> Match")
    else:
        print(repr(s), "-> No match")
