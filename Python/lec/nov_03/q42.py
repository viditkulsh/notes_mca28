# Match an email ID (basic format).

import re

pattern = r"^[\w.+-]+@[\w-]+(\.[\w-]+)*\.[A-Za-z]{2,}$"
strings = ["student@gmail.com", "first.last@mitwpu.edu.in", "abc@com", "@gmail.com", "abc gmail.com"]

print("Pattern:", pattern)
for s in strings:
    if re.search(pattern, s):
        print(repr(s), "-> Match")
    else:
        print(repr(s), "-> No match")
