htmltext = '<html><body><div class=1>Hello<p>This</p><a href="www.google.com">is a bad formatted<li>code</li></a></div></body></html>'

from bs4 import BeautifulSoup

soup = BeautifulSoup(htmltext, 'html.parser')

print(soup.prettify())