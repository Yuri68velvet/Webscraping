import requests
from bs4 import BeautifulSoup

res=requests.get('https://palette-in.jp/')
content=res.content

soup=BeautifulSoup(content,'html.parser')

title_tag=soup.title

title=title_tag.string

print(title_tag)

print(title)


print('-------------------------------------------')

# print(soup)
print(soup.prettify())
print('-----------------------------------------')
print(soup.original_encoding)

print('--------------------------------------------------')


test=soup.find(class_='gf')

print(type(test))
print('------------------------------------------------------')

print(test.find(""))