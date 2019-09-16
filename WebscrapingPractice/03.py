from bs4 import BeautifulSoup

HTMLFILEPATH="03.html"
with open(HTMLFILEPATH,'r')as organization:
    soup=BeautifulSoup(organization,'html.parser')
print(soup.contents)
