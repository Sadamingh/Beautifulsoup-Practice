URL = 'http://www.catb.org/~esr/faqs/smart-questions.html'
ENCODING = 'utf-8'

import requests
from bs4 import BeautifulSoup

reqs = requests.get(URL)
reqs.encoding = ENCODING
soup = BeautifulSoup(reqs.text, 'html.parser')

for litag in soup.find_all('li'):
	print("{0}: {1}".format(litag.name, litag.text))