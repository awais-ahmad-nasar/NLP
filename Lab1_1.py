import nltk
import pandas as pd
from nltk.corpus import reuters

# Download the Reuters corpus if not already downloaded
#nltk.download('reuters')    # news article = reuters

# Get a list of document IDs from the Reuters corpus
documents = reuters.fileids()

# Create an empty list to store document data
document_data = []

# Iterate through each document ID
for doc_id in documents:
    # Get the raw text of the document
    text = reuters.raw(doc_id)

    # Get the categories (topics) associated with the document
    categories = reuters.categories(doc_id)

    # Append document data to the list
    document_data.append({'doc_id': doc_id, 'text': text, 'categories': categories})

# Create a pandas DataFrame from the list of document data
dfDocument= pd.DataFrame(document_data)
all_reuters_words = []
for file_id in documents:
    file_words = reuters.words(file_id)
    output = " ".join(file_words)
    all_reuters_words.append(output)
json_data = {"all_words": all_reuters_words}
df_words = pd.DataFrame.from_dict(json_data)
# Display the DataFrame
print(dfDocument.head())
