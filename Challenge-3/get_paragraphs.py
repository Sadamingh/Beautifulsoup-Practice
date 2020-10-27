from bs4 import BeautifulSoup

with open('index.html') as f:
    text = f.read()
    soup = BeautifulSoup(text, 'html.parser')
    
    ps = soup.find_all('p')

for p in [str(p)[3: -4] for p in ps]:
	print(p)