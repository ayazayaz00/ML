from collections import Counter
import pandas as pd

documents = {
    "d1": "machine learning is fun and machine learning is powerful",
    "d2": "python is great for machine learning and data science",
    "d3": "data science uses machine learning and statistics",
    "d4": "machine learning models learn from data",
    "d5": "python and machine learning are widely used"
}

top_words = {}

for doc, text in documents.items():
    words = text.lower().split()
    freq = Counter(words)
    top_words[doc] = [word for word, count in freq.most_common(5)]

vocabulary = sorted(set(word for words in top_words.values() for word in words))

data_matrix = []

for doc, text in documents.items():
    words = text.lower().split()
    freq = Counter(words)
    row = [freq[word] if word in top_words[doc] else 0 for word in vocabulary]
    data_matrix.append(row)

df = pd.DataFrame(data_matrix, columns=vocabulary, index=documents.keys())

print("Data Matrix:\n")
print(df)