# Match a sequence containing zero or more digits.

import re

pattern = r"\d*"
text = "ab12c345"

# \d* can also match an empty string, so findall returns '' wherever there is no digit
matches = re.findall(pattern, text)

print("Pattern:", pattern)
print("Text:", text)
print("Matches:", matches)
