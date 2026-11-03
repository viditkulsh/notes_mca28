# Match any digit or alphabet.

import re

pattern = r"[a-zA-Z0-9]"
text = "A1-b2_c3!"

matches = re.findall(pattern, text)

print("Pattern:", pattern)
print("Text:", text)
print("Matches:", matches)
