# 5.1.4 String Processing and Pattern Matching
    # Following example is counting the number of geruns in a document
        # Simple but naive

from nltk.tokenize import word_tokenize

sentence = "This is a test sentence, and I am hoping it doesn't get chopped up too much."
tokens = word_tokenize(sentence)

count = 0
for token in tokens:
    if token.endswith("ing"):
        count += 1
print(count)