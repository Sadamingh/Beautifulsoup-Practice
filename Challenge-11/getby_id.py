URL = 'https://www.gnu.org/gnu/byte-interview.html'
ENCODING = 'utf-8'
ID = 'content'

import requests
from bs4 import BeautifulSoup

reqs = requests.get(URL)
reqs.encoding = ENCODING
soup = BeautifulSoup(reqs.text, 'html.parser')

idcontent = soup.find_all(id=ID)

for item in idcontent:
	print(item.text)

# we can also use
# print(soup.select_one('#content').text) 