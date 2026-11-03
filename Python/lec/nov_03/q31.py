# Match a word containing one or more lowercase letters.

import re

pattern = r"[a-z]+"
text = "Hello world PYTHON regex"

matches = re.findall(pattern, text)

print("Pattern:", pattern)
print("Text:", text)
print("Matches:", matches)
