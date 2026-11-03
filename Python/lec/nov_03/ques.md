# Regular Expression – Practice Questions

Each answer has its own program (`q1.py` – `q45.py`). Programs for "match a word / sequence" use
`re.findall()` on a sample sentence; programs for "match a string" use `^ ... $` anchors with
`re.search()` on a list of test strings and print Match / No match.

## Practice Set 1

| # | Question | Pattern | Meaning |
|---|---|---|---|
| 1 | Match the letter a. | `a` | The literal character `a` (case-sensitive) |
| 2 | Match the word Python. | `Python` | The literal text `Python` (case-sensitive) |
| 3 | Match any digit from 0 to 9. | `[0-9]` | One character from the range 0-9 (same as `\d`) |
| 4 | Match any lowercase letter. | `[a-z]` | One character from a to z |
| 5 | Match any uppercase letter. | `[A-Z]` | One character from A to Z |
| 6 | Match any three-digit sequence. | `\d{3}` | Exactly three digits in a row |
| 7 | Match a word containing only lowercase letters. | `\b[a-z]+\b` | Whole word (`\b` on both sides) made only of a-z |
| 8 | Match a sequence containing exactly 5 digits. | `\b\d{5}\b` | Exactly five digits, not part of a longer number |
| 9 | Match any vowel (a, e, i, o, u). | `[aeiou]` | One character from the set a, e, i, o, u |
| 10 | Match any digit or alphabet. | `[a-zA-Z0-9]` | One letter (either case) or digit |
| 11 | Match a word starting with P. | `\bP\w*` | Word boundary, `P`, then any word characters |
| 12 | Match a word ending with ing. | `\b\w*ing\b` | Any word characters followed by `ing` at the end of the word |
| 13 | Match a string containing exactly 4 characters. | `^.{4}$` | Start, exactly four of any character, end |
| 14 | Match a number containing at least 2 digits. | `\b\d{2,}\b` | Two or more digits (`{2,}` = minimum 2, no maximum) |
| 15 | Match a sequence containing 3 to 5 digits. | `\b\d{3,5}\b` | Between three and five digits |
| 16 | Match a word starting with A. | `\bA\w*` | Word boundary, `A`, then any word characters |
| 17 | Match a word ending with n. | `\b\w*n\b` | Any word characters followed by `n` at the end of the word |
| 18 | Match a string starting with Hello. | `^Hello` | `^` anchors `Hello` to the start of the string |
| 19 | Match a string ending with Python. | `Python$` | `$` anchors `Python` to the end of the string |
| 20 | Match a 10-digit mobile number. | `^\d{10}$` | Exactly ten digits and nothing else |

## Practice Set 2

| # | Question | Pattern | Meaning |
|---|---|---|---|
| 21 | Match any character except a digit. | `\D` | Any non-digit character (same as `[^0-9]`) |
| 22 | Match any whitespace character. | `\s` | Space, tab, newline, etc. |
| 23 | Match any non-whitespace character. | `\S` | Anything that is not whitespace |
| 24 | Match any uppercase vowel. | `[AEIOU]` | One character from A, E, I, O, U |
| 25 | Match any lowercase consonant. | `[b-df-hj-np-tv-z]` | a-z with the vowels cut out of the ranges |
| 26 | Match a word containing only alphabets. | `\b[a-zA-Z]+\b` | Whole word made only of letters |
| 27 | Match a sequence containing exactly 4 uppercase letters. | `\b[A-Z]{4}\b` | Exactly four capital letters as a separate word |
| 28 | Match a string containing only digits. | `^\d+$` | One or more digits from start to end |
| 29 | Match a word containing 3 to 6 characters. | `\b\w{3,6}\b` | Whole word of three to six word characters |
| 30 | Match a number containing exactly 6 digits. | `\b\d{6}\b` | Exactly six digits, not part of a longer number |
| 31 | Match a word containing one or more lowercase letters. | `[a-z]+` | `+` = one or more lowercase letters in a row |
| 32 | Match a sequence containing zero or more digits. | `\d*` | `*` = zero or more digits |
| 33 | Match a string containing exactly 2 vowels. | `^[^aeiou]*[aeiou][^aeiou]*[aeiou][^aeiou]*$` | Non-vowels, vowel, non-vowels, vowel, non-vowels |
| 34 | Match a word containing only uppercase and lowercase letters. | `^[A-Za-z]+$` | Only A-Z and a-z from start to end |
| 35 | Match a sequence containing 2 to 4 uppercase letters. | `\b[A-Z]{2,4}\b` | Two to four capital letters as a separate word |
| 36 | Match a word starting with M and ending with a. | `\bM\w*a\b` | `M`, any word characters, `a` at the end of the word |
| 37 | Match a string starting with a digit. | `^\d` | A digit right after the start of the string |
| 38 | Match a string ending with a digit. | `\d$` | A digit right before the end of the string |
| 39 | Match a word starting with S and containing any characters after it. | `\bS\w*` | Word boundary, `S`, then any word characters |
| 40 | Match a string that starts and ends with the letter A. | `^A.*A$` | `A` at the start, anything in between, `A` at the end |
| 41 | Match a 6-digit PIN code. | `^[1-9]\d{5}$` | Six digits; an Indian PIN code cannot start with 0 |
| 42 | Match an email ID (basic format). | `^[\w.+-]+@[\w-]+(\.[\w-]+)*\.[A-Za-z]{2,}$` | username `@` domain `.` extension of 2+ letters |
| 43 | Match a date in DD/MM/YYYY format (format only). | `^\d{2}/\d{2}/\d{4}$` | Two digits / two digits / four digits |
| 44 | Match a word containing only lowercase letters and digits. | `\b[a-z0-9]+\b` | Whole word made only of a-z and 0-9 |
| 45 | Match a username containing 5 to 10 characters. | `^\w{5,10}$` | Five to ten letters, digits or underscores |

## Notes

- `\b` is a word boundary. Use it when the question says *word*, so the pattern does not match part of a longer word or number.
- `^` and `$` anchor the pattern to the start and end of the whole string. Use them when the question says *string*.
- Q7 vs Q31: `\b[a-z]+\b` needs the whole word to be lowercase, while `[a-z]+` picks out any run of lowercase letters (e.g. `ello` from `Hello`).
- Q20: for Indian mobile numbers only, use `^[6-9]\d{9}$` (they start with 6, 7, 8 or 9).
- Q40: `^A.*A$` needs at least two characters. To also accept the single letter `A`, use `^A(.*A)?$`.
- Q42 and Q43 check the format only. They do not confirm that the email exists or that the date is real.
