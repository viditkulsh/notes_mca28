# Match a word starting with M and ending with a.

import re

pattern = r"\bM\w*a\b"
text = "Meera Maya Mango Mumbai Ma Mona"

matches = re.findall(pattern, text)

print("Pattern:", pattern)
print("Text:", text)
print("Matches:", matches)
