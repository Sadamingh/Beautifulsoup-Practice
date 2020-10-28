from bs4 import BeautifulSoup

with open('index.html') as f:
    text = f.read()
    soup = BeautifulSoup(text, 'html.parser')
    
    title = soup.find('title')

print(str(title)[7: len(title)-9])
