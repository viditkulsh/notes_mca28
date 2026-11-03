# Match a string that starts and ends with the letter A.

import re

pattern = r"^A.*A$"
strings = ["ANA", "AMBA", "Asia", "AA", "BANANA"]

print("Pattern:", pattern)
for s in strings:
    if re.search(pattern, s):
        print(repr(s), "-> Match")
    else:
        print(repr(s), "-> No match")
