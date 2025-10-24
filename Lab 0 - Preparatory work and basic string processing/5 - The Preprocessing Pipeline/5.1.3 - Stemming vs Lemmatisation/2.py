# 2 - Lemmatisation pt1

import nltk
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('wordnet') # These two lines only need to be run once

lemmatiser = WordNetLemmatizer()
sentence = "I am writing a few words, and I am hoping they don't get chopped up too much."
print(sentence)

for token in word_tokenize(sentence):
    print(lemmatiser.lemmatize(token))