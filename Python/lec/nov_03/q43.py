# Match a date in DD/MM/YYYY format (format only).

import re

pattern = r"^\d{2}/\d{2}/\d{4}$"
strings = ["03/11/2026", "3/11/2026", "03-11-2026", "99/99/2026"]

# Only the format is checked, so 99/99/2026 is accepted
print("Pattern:", pattern)
for s in strings:
    if re.search(pattern, s):
        print(repr(s), "-> Match")
    else:
        print(repr(s), "-> No match")
