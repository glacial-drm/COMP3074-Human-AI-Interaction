# 3.2 - Getting HTML code of webpage

from urllib import request
url = "http://google.com"
raw = request.urlopen(url).read().decode('utf8')
print(raw)