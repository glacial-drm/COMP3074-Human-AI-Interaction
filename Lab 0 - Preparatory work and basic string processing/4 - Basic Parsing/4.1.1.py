# 4.1.1 Reading Online Files

import nltk
from urllib import request

url = "https://gutenberg.org/cache/epub/7241/pg7241.txt" # Furina de Fontaine :speaking_head: 
content = request.urlopen(url).read().decode('utf8', errors='ignore') # errors=ignore is so Python doesn't jump when there are characters it can't parse