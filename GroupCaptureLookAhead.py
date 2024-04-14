import re

#capture group
target_string = "The price of ice-creams PINEAPPLE 20 MANGO 30 CHOCOLATE 40"

# two groups enclosed in separate ( and ) bracket
# group 1: find all uppercase letter
# group 2: find all numbers
# you can compile a pattern or directly pass to the finditer() method
pattern = re.compile(r"(\b[A-Z]+\b).(\b\d+\b)")

# find all matches to groups
for match in pattern.finditer(target_string):
    print(match.group(0))
    # extract words
    print(match.group(1))
    # extract numbers
    print(match.group(2))

#named Caputer Group
s = 'news/2021/12/31 sports/2023/09/28'
pattern = '(?P<resource>\w+)/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})'

matches = re.finditer(pattern, s)
for match in matches:
    print(match.groupdict())

#look ahead
s = '01 Python is about 4    feet long'
pattern = '\d+(?=\s*feet)'

matches = re.finditer(pattern,s)
for match in matches:
    print(match.group())

#negative look ahead
#look ahead
s = '1 Python is about 4 feet long'
pattern = '\d+(?!\s*feet)'

matches = re.finditer(pattern,s)
for match in matches:
    print(match.group())

pattern=r'the (.*)er they (.*) , the \1er we \2'
str='the faster they ran , the faster we ran'
#The bigger they were, the faster they will be (NOT MATCH)

matches = re.finditer(pattern, str)
for match in matches:
    print(match.group(1))
    print(match.group(2))

# non capturing group
pattern=r"(?:some|a few) (people|cats) like some \1"
str='some people like some people'

matches = re.finditer(pattern, str)
for match in matches:
    print(match.group(1))


#non capture group another example
s = 'Python 3.10'
pattern = '(?:\d+)\.(\d+)'

match = re.search(pattern, s)

# show the whole match
print(match.group())

# show the groups
for group in match.groups():
    print(group)
