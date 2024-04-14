import re

'''
1)Extract all twitter handles from following text.
Twitter handle is the text that appears after https://twitter.com/ and is a single word. 
Also it contains only alpha numeric characters i.e. A-Z a-z , o to 9 and underscore 
'''

text1 = '''
Follow our leader Elon musk on twitter here: https://twitter.com/elonmusk, more information 
on Tesla's products can be found at https://www.tesla.com/. Also here are leading influencers 
for tesla related news,
https://twitter.com/teslarati
https://twitter.com/dummy_tesla
https://twitter.com/dummy_2_tesla
'''
pattern1 = 'https://twitter\.com/([a-zA-Z0-9_]+)'

a=re.findall(pattern1, text1)
print(a)

#........................................................................................

'''
2. Extract Concentration Risk Types. 
It will be a text that appears after "Concentration Risk:", 
In below example, your regex should extract these two strings**

(1) Credit Risk

(2) Supply Rish
'''


text2 = '''
Concentration of Risk: Credit Risk
Financial instruments that potentially subject us to a concentration of credit risk consist of cash, cash equivalents, marketable securities,
restricted cash, accounts receivable, convertible note hedges, and interest rate swaps. Our cash balances are primarily invested in money market funds
or on deposit at high credit quality financial institutions in the U.S. These deposits are typically in excess of insured limits. As of September 30, 2021
and December 31, 2020, no entity represented 10% or more of our total accounts receivable balance. The risk of concentration for our convertible note
hedges and interest rate swaps is mitigated by transacting with several highly-rated multinational banks.
Concentration of Risk: Supply Risk
We are dependent on our suppliers, including single source suppliers, and the inability of these suppliers to deliver necessary components of our
products in a timely manner at prices, quality levels and volumes acceptable to us, or our inability to efficiently manage these components from these
suppliers, could have a material adverse effect on our business, prospects, financial condition and operating results.
'''
pattern2 = 'Concentration of Risk: ([^\n]*)'

b=re.findall(pattern2, text2)
print(b)


#........................................................................................

'''
3. Companies in europe reports their financial numbers of semi annual basis and 
you can have a document like this. To exatract quarterly and 
semin annual period you can use a regex as shown below

Hint: you need to use (?:) here to match everything enclosed
'''


text3 = '''
Tesla's gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
BMW's gross cost of operating vehicles in FY2021 S1 was $8 billion.
'''

pattern3 = 'FY(\d{4} (?:Q[1-4]|S[1-2]))'
matches = re.findall(pattern3, text3)
print(matches)