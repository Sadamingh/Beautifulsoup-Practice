URL = 'https://en.wikipedia.org/wiki/Data_type'
ENCODING = 'utf-8'

import requests
from bs4 import BeautifulSoup

reqs = requests.get(URL)
reqs.encoding = ENCODING
soup = BeautifulSoup(reqs.text, 'html.parser')

tables = soup.find_all('table')

print(tables[1])