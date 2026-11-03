# Match a sequence containing exactly 4 uppercase letters.

import re

pattern = r"\b[A-Z]{4}\b"
text = "Codes: ABCD, XYZ, PQRST, MITW, abcd"

matches = re.findall(pattern, text)

print("Pattern:", pattern)
print("Text:", text)
print("Matches:", matches)
