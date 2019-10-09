from bs4 import BeautifulSoup
from urllib.request import urlopen

url='https://www.simplilearn.com/resources'

webpage=urlopen(url)

sl_soup=BeautifulSoup(webpage,'html.parser')

webpage.close()

print(sl_soup.contents)

print(sl_soup.prettify())

print('-------------title----------------')

print(sl_soup.title)

print('----------------href-------------------')

for href in sl_soup.findAll('a',href=True):
    print(href["href"])


print('------------------find h2------------------------------')

for heading in sl_soup.findAll("h2"):
    print(heading.string)


for heading4 in sl_soup.findAll("h4"):
    print(heading4.string)


url2="https://www.simplilearn.com/what-is-tensorflow-article?source=frs_home"

webpage2=urlopen(url2)

sl_article=BeautifulSoup(webpage2,'html.parser')

test=sl_article.find(class_='desig_author empty-text')

print(type(test))

print(test.findAll("p"))

first_next_p=test.p
print(first_next_p)

find_next_sibling=first_next_p.next_sibling.next_sibling
print(find_next_sibling)

print('-----------------------------------')
print(find_next_sibling.previous_sibling.previous_sibling)