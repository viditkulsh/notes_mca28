# Match a number containing exactly 6 digits.

import re

pattern = r"\b\d{6}\b"
text = "OTPs: 482913, 12345, 1234567, 000111"

matches = re.findall(pattern, text)

print("Pattern:", pattern)
print("Text:", text)
print("Matches:", matches)
