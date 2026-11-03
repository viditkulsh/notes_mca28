# Match a string containing exactly 2 vowels.

import re

pattern = r"^[^aeiou]*[aeiou][^aeiou]*[aeiou][^aeiou]*$"
strings = ["cat", "hello", "rain", "banana", "sky", "music"]

print("Pattern:", pattern)
for s in strings:
    if re.search(pattern, s):
        print(repr(s), "-> Match")
    else:
        print(repr(s), "-> No match")
