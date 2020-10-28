FILENAME = 'index.html'
TAG = 'h2'

from bs4 import BeautifulSoup

with open(FILENAME) as f:
    text = f.read()
    soup = BeautifulSoup(text, 'html.parser')
    
    headers = soup.find_all(TAG)

content = ' '.join([str(header)[4:-5] for header in headers]).split()
print(f'The number of words in the {TAG} tag is:', len(content))