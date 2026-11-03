# Match a word containing 3 to 6 characters.

import re

pattern = r"\b\w{3,6}\b"
text = "I am learning regex in Python today"

matches = re.findall(pattern, text)

print("Pattern:", pattern)
print("Text:", text)
print("Matches:", matches)
