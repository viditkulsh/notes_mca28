# Match any character except a digit.

import re

pattern = r"\D"
text = "A1b2 C3!"

matches = re.findall(pattern, text)

print("Pattern:", pattern)
print("Text:", text)
print("Matches:", matches)
