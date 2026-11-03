# Match a word ending with ing.

import re

pattern = r"\b\w*ing\b"
text = "I am learning coding and singing, not ingest"

matches = re.findall(pattern, text)

print("Pattern:", pattern)
print("Text:", text)
print("Matches:", matches)
