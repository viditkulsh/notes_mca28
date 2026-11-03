# Match a sequence containing exactly 5 digits.

import re

pattern = r"\b\d{5}\b"
text = "Codes: 12345, 1234, 123456, 54321"

matches = re.findall(pattern, text)

print("Pattern:", pattern)
print("Text:", text)
print("Matches:", matches)
