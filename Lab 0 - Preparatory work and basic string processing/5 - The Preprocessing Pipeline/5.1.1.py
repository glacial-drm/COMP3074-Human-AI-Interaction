# 5.1.1 Dealing with HTML

from bs4 import BeautifulSoup

# Remove HTML tags from text, assuming it contains them
content = BeautifulSoup(htmlString, 'html.parser').get_text()