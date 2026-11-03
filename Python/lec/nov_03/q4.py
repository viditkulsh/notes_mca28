# Match any lowercase letter.

import re

pattern = r"[a-z]"
text = "Hello MCA World"

matches = re.findall(pattern, text)

print("Pattern:", pattern)
print("Text:", text)
print("Matches:", matches)
