# Match a word starting with S and containing any characters after it.

import re

pattern = r"\bS\w*"
text = "Sam sells Sea shells on the Seashore"

matches = re.findall(pattern, text)

print("Pattern:", pattern)
print("Text:", text)
print("Matches:", matches)
