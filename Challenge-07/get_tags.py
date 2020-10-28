URL = 'http://www.catb.org/~esr/faqs/smart-questions.html'
ENCODING = 'utf-8'

import requests
from bs4 import BeautifulSoup

reqs = requests.get(URL)
reqs.encoding = ENCODING
soup = BeautifulSoup(reqs.text, 'html.parser')

tags = set()

for child in soup.recursiveChildGenerator():
    if child.name:
    	if child.name != 'div':
        	tags.add(child.name)

ord_tags = list(tags)
ord_tags.sort()

print(ord_tags)