from bs4 import BeautifulSoup
import requests

url='https://www.simplilearn.com'

store=requests.get(url)

print(store)

page_content=store.content

soup=BeautifulSoup(page_content,'html.parser')

print(soup)


print(soup.prettify())

print('-----------------------------------------------')
print(soup.original_encoding)


print('----------------------------------------------')
# print(soup.body.a.prettify(formatter='xml'))


def upperCaseFn(lohit):
    return lohit.upper()

print(soup.body.a.prettify(formatter=upperCaseFn))

