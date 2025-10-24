# 3 - Lemmatisation pt2
    # FIGURE IN THE LAB EXPLAINS OUTPUT
    # Lemmatizer by default does badly on verbs, it needs part-of-speech tagging as the second argument of the lemmatize() method
        # We use average_perceptron_tagger to do this
    # Default behaviour assumes everything is a noun

import nltk
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import word_tokenize

nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng') # Additional line
nltk.download('universal_tagset')

lemmatiser = WordNetLemmatizer()
sentence = "This is a test sentence, and I am hoping it doesn't get chopped up too much."

post = nltk.pos_tag(word_tokenize(sentence), tagset='universal')
print(post)