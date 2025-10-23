# 5.3.2 Implementation in Python
    # Using a dictionary to implement inverted index for obvious reasons
from collections import defaultdict

corpus = {
"doc1 ": ["rejoic ", "hear ", "disast ", "enterpris ", "rejoic "],
"doc2 ": ["six ", "year ", "great ", "enterpris ", "dedic "],

"doc3 ": ["rejoic ", "great ", "disast ", "year "]
}

# Use a defaultdict for convenience to handle new terms automatically .
# The index will map a term to another dictionary , which maps a
# doc_id to its term frequency .
inverted_index = defaultdict ( lambda : defaultdict ( int ))

for doc_id , tokens in corpus . items () :
    for token in tokens :
        inverted_index [ token ][ doc_id ] += 1

# The resulting index is a dict of dicts . To view it as a
# standard dict for printing :
final_index = { term : dict ( postings ) for term , postings in inverted_index . items () }

# Example postings for "rejoic ":
# "rejoic ": { " doc1 ": 2, "doc3 ": 1}

# Example postings for "enterpris ":
# "enterpris ": {" doc1 ": 1, "doc2 ": 1}