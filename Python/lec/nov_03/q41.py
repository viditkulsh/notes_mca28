# Match a 6-digit PIN code.

import re

pattern = r"^[1-9]\d{5}$"
strings = ["411038", "011038", "41103", "4110381"]

print("Pattern:", pattern)
for s in strings:
    if re.search(pattern, s):
        print(repr(s), "-> Match")
    else:
        print(repr(s), "-> No match")
