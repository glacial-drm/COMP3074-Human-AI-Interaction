# 3.1 - Accessing NTLK
from bs4 import BeautifulSoup as bsoup
import nltk

nltk.download_gui()
# nltk.download_shell()
nltk.download('gutenberg')
print(nltk.corpus.gutenberg.fileids())
