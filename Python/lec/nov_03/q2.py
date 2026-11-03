# Match the word Python.

import re

pattern = r"Python"
text = "I love Python. Python is easy, python is fun."

matches = re.findall(pattern, text)

print("Pattern:", pattern)
print("Text:", text)
print("Matches:", matches)
