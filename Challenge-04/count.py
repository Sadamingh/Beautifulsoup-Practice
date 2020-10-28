FILENAME = 'index.html'

from bs4 import BeautifulSoup

with open(FILENAME) as f:
    text = f.read()
    soup = BeautifulSoup(text, 'html.parser')
    
    titles = soup.find_all('title')
    ps = soup.find_all('p')

print(f'The number of titles in {FILENAME} is:', len(titles))
print(f'The number of paragraphs in {FILENAME} is:', len(ps))