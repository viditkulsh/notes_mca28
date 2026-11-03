# Match a word starting with A.

import re

pattern = r"\bA\w*"
text = "Aarav and Ananya ate an Apple"

matches = re.findall(pattern, text)

print("Pattern:", pattern)
print("Text:", text)
print("Matches:", matches)
