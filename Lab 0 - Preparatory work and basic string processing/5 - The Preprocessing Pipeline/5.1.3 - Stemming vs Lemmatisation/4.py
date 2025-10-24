# 4 - Lemmatisaton pt 3
    # Not done, as POS tags that the lemmatiser wants are differente from the ones the POS tagger provides
    # We now map the provided POS tags to POS tags that the WordNetLemmatizer takes as imput
        # a for adjectives, n for nouns, v for verbs and r for adverbs

    # Result isn't perfect, but recognises verbs and doesn't cut down nouns as much as the average stemmer. Takes more time though

import nltk
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import word_tokenize

nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng') # Additional line
nltk.download('universal_tagset')

lemmatiser = WordNetLemmatizer()
sentence = "I am writing a few words, and I am hoping they don't get chopped up too much"

posmap = {
    'ADJ': 'a',
    'ADV': 'r',
    'NOUN': 'n',
    'VERB': 'v'
}

post = nltk.pos_tag(word_tokenize(sentence), tagset='universal')
print(post)

for token in post:
    word = token[0]
    tag = token[1]

    if tag in posmap.keys():
        print(lemmatiser.lemmatize(word, posmap[tag]))
    else:
        print(lemmatiser.lemmatize(word))
    print("---")