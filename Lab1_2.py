from nltk.corpus import reuters
import matplotlib.pyplot as plt
from collections import Counter

# Download the Reuters dataset
#nltk.download('reuters')   // news article = reuters

# List of file IDs in the Reuters dataset
file_ids = reuters.fileids()

# Number of documents in the Reuters dataset
num_documents = len(file_ids)
print("Number of documents in the Reuters dataset : ", num_documents)

# Categories in the Reuters dataset
categories = reuters.categories()
num_categories = len(categories)
print("\nNumber of categories in the Reuters dataset : ", num_categories)
print("\n.............Categories..............\n", categories)

# Sample document
sample_doc_id = file_ids[0]
sample_doc_content = reuters.raw(sample_doc_id)
print("\n.....................Sample document content..................\n")
print(sample_doc_content[:1000])  # Displaying the first 500 characters of the sample document

# Distribution of document lengths
document_lengths = [len(reuters.raw(file_id)) for file_id in file_ids]
print("\n.......................Document Length........................\n",document_lengths)
max_length = max(document_lengths)
min_length = min(document_lengths)
avg_length = sum(document_lengths) / len(document_lengths)

# Print the results
print("\nMaximum document length : ", max_length)
print("Minimum document length : ", min_length)
print("Average document length : ", avg_length)
list_size = len(document_lengths)

# Print the size of the list
print("\nSize of the list (number of elements) : ", list_size)
# Plotting the distribution of document lengths
plt.figure(figsize=(10, 6))
plt.hist(document_lengths, bins=200, color='skyblue', edgecolor='black')
plt.title('Distribution of Document Lengths in Reuters Dataset')
plt.xlabel('Document Length')
plt.ylabel('Frequency')
plt.show()

# Top categories by document count
category_counts = Counter(reuters.categories())
top_categories = category_counts.most_common(10)
print("\n.................Top categories by document count................\n")
for category, count in top_categories:
    print(f"{category}: {count} documents")
