# Match a string starting with Hello.

import re

pattern = r"^Hello"
strings = ["Hello World", "Say Hello", "Hello", "hello there"]

print("Pattern:", pattern)
for s in strings:
    if re.search(pattern, s):
        print(repr(s), "-> Match")
    else:
        print(repr(s), "-> No match")
