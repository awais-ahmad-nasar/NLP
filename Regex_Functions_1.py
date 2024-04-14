import re

pattern = r'apple'
text = 'I have an apple and a banana'
match = re.search(pattern, text)
if match:
    print('Pattern found:', match.group())
else:
    print('Pattern not found')
pattern = r'apple'
text = 'apple and banana'
match = re.match(pattern, text)
if match:
    print('Pattern found at the beginning:', match.group())
else:
    print('Pattern not found at the beginning')

pattern = r'\d+'
text = 'I have 2 apples and 3 bananas'
matches = re.findall(pattern, text)
print('Matches:', matches)

pattern = r'\d+'
text = 'I have 2 apples and 3 bananas'
matches_iterator = re.finditer(pattern, text)
for match in matches_iterator:
    print('Match:', match.group())


pattern = r'\d+'
text = 'I have 2 apples and 3 bananas'
replacement = 'many'
new_text = re.sub(pattern, replacement, text)
print('New text:', new_text)


pattern = r'\s+'
text = 'I have many apples and bananas'
parts = re.split(pattern, text)
print('Parts:', parts)



pattern = r'(\d+)-(\d+)-(\d+)'
text = 'Date: 2022-01-01'
match = re.search(pattern, text)
if match:
    print('Entire match:', match.group(0))  # Output: '2022-01-01'
    print('Year:', match.group(1))          # Output: '2022'
    print('Month:', match.group(2))         # Output: '01'
    print('Day:', match.group(3))           # Output: '01'


