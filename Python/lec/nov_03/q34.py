# Match a word containing only uppercase and lowercase letters.

import re

pattern = r"^[A-Za-z]+$"
strings = ["Python", "MCA", "hello", "Python3", "hello_world"]

print("Pattern:", pattern)
for s in strings:
    if re.search(pattern, s):
        print(repr(s), "-> Match")
    else:
        print(repr(s), "-> No match")
