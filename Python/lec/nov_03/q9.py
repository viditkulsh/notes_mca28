# Match any vowel (a, e, i, o, u).

import re

pattern = r"[aeiou]"
text = "regular expression"

matches = re.findall(pattern, text)

print("Pattern:", pattern)
print("Text:", text)
print("Matches:", matches)
