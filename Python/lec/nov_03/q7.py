# Match a word containing only lowercase letters.

import re

pattern = r"\b[a-z]+\b"
text = "python is Fun and regex101 rocks"

matches = re.findall(pattern, text)

print("Pattern:", pattern)
print("Text:", text)
print("Matches:", matches)
