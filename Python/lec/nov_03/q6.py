# Match any three-digit sequence.

import re

pattern = r"\d{3}"
text = "Room 101, Block 205, Lab 7"

matches = re.findall(pattern, text)

print("Pattern:", pattern)
print("Text:", text)
print("Matches:", matches)
