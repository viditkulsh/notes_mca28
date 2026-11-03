# Match any lowercase consonant.

import re

pattern = r"[b-df-hj-np-tv-z]"
text = "regex practice"

matches = re.findall(pattern, text)

print("Pattern:", pattern)
print("Text:", text)
print("Matches:", matches)
