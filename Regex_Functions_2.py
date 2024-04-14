#The re.findall() method returns a list of strings containing all matches

# Program to extract numbers from a string

import re

string = 'hello 1 hi 89. Howdy 342324'
pattern = '\d+'

result = re.findall(pattern, string)
print(result)

# The re.split method splits the string where there is a match and returns a list of strings where the splits have occurred.




string = 'Twelve:12 Eighty nine:89.'
pattern = '\d+'

result = re.split(pattern, string)
print(result)

#You can pass maxsplit argument to the re.split() method. It's the maximum number of splits that will occur.
string = 'Twelve:12 Eighty nine:89 Nine:9.'
pattern = '\d+'

# maxsplit = 1
# split only at the first occurrence
result = re.split(pattern, string, 1)
print(result)

# re.sub() ,The method returns a string where matched occurrences are replaced with the content of replace variable.

# Program to remove all whitespaces

# multiline string
string = 'abc 12\
de 23 \n f45 6'

# matches all whitespace characters
pattern = '\s+'

# empty string
replace = ';'

new_string = re.sub(pattern, replace, string)
print(new_string)

#The re.subn() is similar to re.sub() except it returns a tuple of 2 items containing the new string and the number of substitutions made.

# multiline string
string = 'abc 12\
de 23 \n f45 6'

# matches all whitespace characters
pattern = '\s+'

# empty string
replace = ''

new_string = re.subn(pattern, replace, string)
print(new_string)

#re.search() The re.search() method takes two arguments: a pattern and a string. The method looks for the first location where the RegEx pattern produces a match with the string.

string = "Do u know?Python is fun"

# check if 'Python' is at the beginning
match = re.search('\APython', string)

if match:
  print("pattern found inside the string")
else:
  print("pattern not found")

#match.group(), The group() method returns the part of the string where there is a match.

string = '39801 356, 2102 1111'

# Three digit number followed by space followed by two digit number
pattern = '(\d{3}) (\d{2})'

# match variable contains a Match object.
match = re.search(pattern, string)

if match:
  print(match.group())
else:
  print("pattern not found")

'''

Here, match variable contains a match object.

Our pattern (\d{3}) (\d{2}) has two subgroups (\d{3}) and (\d{2}). You can get the part of the string of these parenthesized subgroups. Here's how:

>>> match.group(1)
'801'

>>> match.group(2)
'35'
>>> match.group(1, 2)
('801', '35')

>>> match.groups()
('801', '35')
match.start(), match.end() and match.span()
The start() function returns the index of the start of the matched substring. Similarly, end() returns the end index of the matched substring.

>>> match.start()
2
>>> match.end()
8
The span() function returns a tuple containing start and end index of the matched part.

>>> match.span()
(2, 8)
match.re and match.string
The re attribute of a matched object returns a regular expression object. Similarly, string attribute returns the passed string.

>>> match.re
re.compile('(\\d{3}) (\\d{2})')

>>> match.string
'39801 356, 2102 1111'
'''
'''
Using r prefix before RegEx
When r or R prefix is used before a regular expression, it means raw string. For example, '\n' is a new line whereas r'\n' means two characters: a backslash \ followed by n.

Backlash \ is used to escape various characters including all metacharacters. However, using r prefix makes \ treat as a normal character.
'''

import re

string = '\n and \r are escape sequences.'

result = re.findall(r'[\n\r]', string)
print(result)

