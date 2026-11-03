# Match the letter a.

import re

pattern = r"a"
text = "Aarav ate a banana"

matches = re.findall(pattern, text)

print("Pattern:", pattern)
print("Text:", text)
print("Matches:", matches)
