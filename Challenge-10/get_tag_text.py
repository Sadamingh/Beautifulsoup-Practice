URL = 'http://www.catb.org/~esr/faqs/smart-questions.html'
ENCODING = 'utf-8'
CLASS = 'sect1'

import requests
from bs4 import BeautifulSoup

reqs = requests.get(URL)
reqs.encoding = ENCODING
soup = BeautifulSoup(reqs.text, 'html.parser')

classcontent = soup.find_all(class_=CLASS)

for item in classcontent:
	print(item.text)