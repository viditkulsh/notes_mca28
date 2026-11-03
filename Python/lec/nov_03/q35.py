# Match a sequence containing 2 to 4 uppercase letters.

import re

pattern = r"\b[A-Z]{2,4}\b"
text = "A, MCA, MIT, USA, INDIA, IT"

matches = re.findall(pattern, text)

print("Pattern:", pattern)
print("Text:", text)
print("Matches:", matches)
