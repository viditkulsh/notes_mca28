# Match any uppercase vowel.

import re

pattern = r"[AEIOU]"
text = "An Elephant In Our Umbrella"

matches = re.findall(pattern, text)

print("Pattern:", pattern)
print("Text:", text)
print("Matches:", matches)
