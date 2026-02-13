from collections import Counter
import pandas as pd
import numpy as np
import itertools
from sklearn.metrics.pairwise import cosine_similarity

# 1. Documents
documents = {
    "d1": "machine learning is fun and machine learning is powerful",
    # "d2": "machine learning is fun and machine learning is powerful",
    "d2": "python is great for machine learning and data science",
    "d3": "data science uses machine learning and statistics",
    "d4": "machine learning models learn from data",
    "d5": "python and machine learning are widely used"
}

# 2. Build Vocabulary
vocabulary = sorted(set(
    word
    for text in documents.values()
    for word in text.lower().split()
))

# 3. Build Document-Term Matrix (Bag-of-Words)
data_matrix = []

for text in documents.values():
    words = text.lower().split()
    freq = Counter(words)
    row = [freq[word] for word in vocabulary]
    data_matrix.append(row)

df = pd.DataFrame(data_matrix, columns=vocabulary, index=documents.keys())

print("========== Document-Term Matrix ==========\n")
print(df)

# 4. Cosine Similarity (Manual Calculation)
# X = df.values

# dot_product = np.dot(X, X.T)
# norms = np.linalg.norm(X, axis=1)
# norm_matrix = np.outer(norms, norms)
# cosine_sim_manual = dot_product / norm_matrix
# similarity_manual_df = pd.DataFrame(
#     cosine_sim_manual,
#     index=df.index,
#     columns=df.index
# )

similarity = cosine_similarity(data_matrix)
sim_df = pd.DataFrame(similarity, index=documents.keys(), columns=documents.keys())
print("\nCosine similarity\n")
print(sim_df)

dissimilarity = 1 - similarity
dis_df = pd.DataFrame(dissimilarity, index=documents.keys(), columns=documents.keys())
print("\nDissimilarity Matrix\n")
print(dis_df)


max_score = -1
best_pair = None
for i, j, in itertools.combinations(range(len(df)),2):
    if similarity[i][j] > max_score:
        max_score = similarity[i][j]
        best_pair = (df.index[i], df.index[j])
        
print("\nMost similar documents: ", best_pair)
print("Similarity Score : ", max_score)

