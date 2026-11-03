# Match any digit from 0 to 9.

import re

pattern = r"[0-9]"
text = "MCA 2026-28"

matches = re.findall(pattern, text)

print("Pattern:", pattern)
print("Text:", text)
print("Matches:", matches)
