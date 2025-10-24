# 5.1.2 Tokenisation, Stopword Removal and Casing Normalisation
    # word.lower() forcing lower case is important to make tokens consistent
import nltk
nltk.download('stopwords')
nltk.download('punkt_tab') # Additional download not in lab

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

text = "Artificial intelligence is cool but I am not too keen on Skynet"

text_tokens = word_tokenize(text)
tokens_without_sw = [word.lower() for word in text_tokens if not word in stopwords.words()]
print(tokens_without_sw) # array of tokens without stopwords

filtered_sentence = (" ").join(tokens_without_sw)
print(filtered_sentence) # string (object type Text) of tokens without stopwords

text = nltk.Text(tokens_without_sw)
print(text.count("cool")) # print total occurrences of some string