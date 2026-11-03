# Match any non-whitespace character.

import re

pattern = r"\S"
text = "Hi there !"

matches = re.findall(pattern, text)

print("Pattern:", pattern)
print("Text:", text)
print("Matches:", matches)
