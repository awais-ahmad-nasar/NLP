# import re
# pattern1='[0-9]'
# pattern2='[a-z]@gmail.com'
#
# test_string1='abcde@gmail.com'
# test_string2='0345678902'
#
# result2=re.match(pattern1,test_string2)
# result1=re.findall(pattern2,test_string1)
#
# if result2:
#     print("phone-Number Matched ")
# else:
#     print("phone-Number Not Matched")
# if result1:
#     print("Matched Email")
# else:
#     print(" Email Not Matched")


#.................. oper wala code simple neeche wala best .....................


import re

text = "i received the email from yesterday from javaid@gmail.com and tried to call your number 0321-5696893. However, I was not able to connect you. This email is incomplete and does not contain information about your date of birth. I just want to cross-check, is it 25/12/1982? Please write me an email on abbas@yahoo.com or return a call on 0333=5686793."

emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
print('Emails:', emails)

phone_numbers = re.findall(r'\b\d{4}[-=]?\d{7}\b', text)

for phone_number in phone_numbers:
    print('Phone number:', phone_number)

replacement_email = "new_email@example.com"
email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
new_text = re.sub(email_regex, replacement_email, text)
print('New text:', new_text)

