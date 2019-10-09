# I'm scraping wikipedia

from bs4 import BeautifulSoup
from urllib.request import urlopen

url='https://en.wikipedia.org/wiki/India'


webpage=urlopen(url)

sl_soup=BeautifulSoup(webpage,'html.parser')

webpage.close()

# print(sl_soup.contents)

# print(sl_soup.prettify())

# print('-------------title----------------')

# print(sl_soup.title)

print('----------------href-------------------')

# for href in sl_soup.findAll('a',href=True):
#     print(href["href"])

print('--------------------------------------------------------')


title=sl_soup.find("tbody")
print(title.text)

print('-------------------------------------------------')
rerigion=title.find("td")
print(rerigion)


print('----------------------------------------------------------')
rerigion1=rerigion.find("div",{"class":"plainlist"})
print(rerigion1)


print('---------------------------------------------------')
# sl_soup.findAll({"class":"plainlist"})
# print(sl_soup.string)

# for heading in sl_soup.findAll("a"):
#     print(heading.string)



# print('------------------------------------------------')

# containers=sl_soup.find("table",{"class":"infobox geography vcard"})


# container=containers

# rerigion=container.findAll("div",{"class":"plainlist"})

# print(rerigion.text)


# test=sl_soup.find(class_='plainlist')

# print(type(test))

# print(test.findAll("ul"))

