# Match a word containing only lowercase letters and digits.

import re

pattern = r"\b[a-z0-9]+\b"
text = "user123 Admin pass word99 TEST 2026"

matches = re.findall(pattern, text)

print("Pattern:", pattern)
print("Text:", text)
print("Matches:", matches)
