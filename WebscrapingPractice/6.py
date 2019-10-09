# #Iam scraping Amazonsite

# from bs4 import BeautifulSoup as bs

# from urllib.request import urlopen as UReq

# my_url='https://www.amazon.co.jp/s?k=macbook&__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&ref=nb_sb_noss'

# uClient=UReq(my_url)

# page_html=uClient.read()

# uClient.close()

# page_soup=bs(page_html,"html.parser")

# containers=page_soup.findAll("span")

# print(len(containers))

# print('-----------------------------------------------')
# price=containers.findAll("div",{"class":"sg-col-inner"})

# print(price[0].text)
# container=containers[0]



# print(container.div.img['alt'])


# print(container.findAll('div',{"class":"a-section aok-relative s-image-square-aspect"}))

# print('--------------------price---------------------------')


# price=container.findAll("span",{"class":"a-size-base-plus a-color-base a-text-normal"})

# print(price[0].text)

from bs4 import BeautifulSoup
from urllib.request import urlopen

url='https://www.amazon.co.jp/s?k=macbook&__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&ref=nb_sb_noss'

webpage=urlopen(url)

sl_soup=BeautifulSoup(webpage,'html.parser')

webpage.close()

print(sl_soup.contents)

print(sl_soup.prettify())

print('-------------title----------------')

print(sl_soup.title)

test=sl_soup.find(class_='sg-col-inner')

print(type(test))

print('----------------------------------------------------------')
print(test.findAll("div"))

print('---------------------------------------------------------')
containers=sl_soup.findAll('a')
container=containers[0]

price=container.find("a",{"class":"a-offscreen"})

print(price)

print(price[0].string)

# first_next_p=test.p
# print(first_next_p)

# find_next_sibling=first_next_p.next_sibling.next_sibling
# print(find_next_sibling)
