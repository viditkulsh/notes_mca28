# Match a word ending with n.

import re

pattern = r"\b\w*n\b"
text = "Python is fun when you learn"

matches = re.findall(pattern, text)

print("Pattern:", pattern)
print("Text:", text)
print("Matches:", matches)
