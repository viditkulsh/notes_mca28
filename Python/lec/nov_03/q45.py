# Match a username containing 5 to 10 characters.

import re

pattern = r"^\w{5,10}$"
strings = ["rahul", "user_2026", "abc", "thisusernameistoolong", "user name"]

print("Pattern:", pattern)
for s in strings:
    if re.search(pattern, s):
        print(repr(s), "-> Match")
    else:
        print(repr(s), "-> No match")
