# Match a sequence containing 3 to 5 digits.

import re

pattern = r"\b\d{3,5}\b"
text = "12 123 1234 12345 123456"

matches = re.findall(pattern, text)

print("Pattern:", pattern)
print("Text:", text)
print("Matches:", matches)
