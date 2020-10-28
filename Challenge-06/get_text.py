URL = 'http://www.catb.org/~esr/faqs/smart-questions.html'
ENCODING = 'utf-8'

import requests
from bs4 import BeautifulSoup

reqs = requests.get(URL)
reqs.encoding = ENCODING
soup = BeautifulSoup(reqs.text, 'html.parser')

print(soup.get_text())