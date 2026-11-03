# Match a 10-digit mobile number.

import re

pattern = r"^\d{10}$"
strings = ["9876543210", "98765", "98765432101", "98765abc10"]

print("Pattern:", pattern)
for s in strings:
    if re.search(pattern, s):
        print(repr(s), "-> Match")
    else:
        print(repr(s), "-> No match")
