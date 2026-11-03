# Match a word starting with P.

import re

pattern = r"\bP\w*"
text = "Python and Perl are Popular programming languages"

matches = re.findall(pattern, text)

print("Pattern:", pattern)
print("Text:", text)
print("Matches:", matches)
