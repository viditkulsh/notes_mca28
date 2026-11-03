# Match any whitespace character.

import re

pattern = r"\s"
text = "Hello World\tPython\nRegex"

matches = re.findall(pattern, text)

print("Pattern:", pattern)
print("Text:", text)
print("Matches:", matches)
