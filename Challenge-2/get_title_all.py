from bs4 import BeautifulSoup

with open('index.html') as f:
    text = f.read()
    soup = BeautifulSoup(text, 'html.parser')
    
    titles = soup.find_all('title')

for title in [str(title)[7: len(title)-9] for title in titles]:
	print(title)
