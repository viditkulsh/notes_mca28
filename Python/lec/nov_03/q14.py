# Match a number containing at least 2 digits.

import re

pattern = r"\b\d{2,}\b"
text = "Scores: 7, 45, 100, 3, 2026"

matches = re.findall(pattern, text)

print("Pattern:", pattern)
print("Text:", text)
print("Matches:", matches)
