# Match any uppercase letter.

import re

pattern = r"[A-Z]"
text = "Hello MCA World"

matches = re.findall(pattern, text)

print("Pattern:", pattern)
print("Text:", text)
print("Matches:", matches)
