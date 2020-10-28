URL = 'https://www.gnu.org/gnu/byte-interview.html'
ENCODING = 'utf-8'
ID = 'content'

import requests
from bs4 import BeautifulSoup

reqs = requests.get(URL)
reqs.encoding = ENCODING
soup = BeautifulSoup(reqs.text, 'html.parser')

bypath = soup.select('html body div div div')

for item in bypath:
	if item.text:
		print(item.text)