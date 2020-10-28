URL = 'http://www.catb.org/~esr/'
ENCODING = 'utf-8'

import requests
from bs4 import BeautifulSoup

reqs = requests.get(URL)
reqs.encoding = ENCODING
soup = BeautifulSoup(reqs.text, 'html.parser')

images = soup.find_all('img')

for item in images:
	print(item.get('src'))