# from nltk.tokenize import word_tokenize
#
# # text=" NLP LAB 1 "
# #text=" NLPLAB1 "
# # text=" NLP , LAB , 1 "
# text=" NLP,LAB,1 "
#
# tokens=word_tokenize(text)
# print(tokens
#       )
#

##########################################################################3
from nltk.tokenize import sent_tokenize
# sentence=("NLP reffers to the brach of AI. It is concerned with giving computers ability to understand text and spoken words. which is similar to how humans do. ")

sentence=("NLP reffers to AI. How are you. ")  #Good ,  ce after dot
# sentence=("NLP reffers to AI .How are you .")  #Wrong


print(sent_tokenize(sentence))
