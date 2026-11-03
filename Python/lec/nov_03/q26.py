# Match a word containing only alphabets.

import re

pattern = r"\b[a-zA-Z]+\b"
text = "Python3 is Fun and regex101 is Cool"

matches = re.findall(pattern, text)

print("Pattern:", pattern)
print("Text:", text)
print("Matches:", matches)
