from bs4 import BeautifulSoup

HTMLFILEPATH='2.html'
with open(HTMLFILEPATH,'r')as organization:
    soup=BeautifulSoup(organization,'html.parser')

print(soup.contents)


print(soup)

print('-------------------------------')
tag_li=soup.find("li")

print(type(tag_li))

print('-------------------------------')
tag_div=soup.find("div")
print(type(tag_div))

print('-------------------------------')

print(tag_div)

print('-------------------------------')

find_id=soup.find(id='man')
print(find_id)

print(find_id.div.string)

print('-------------------------------')


search_for_stringonly=soup.find(text=['Yuri',"Naoki"])
print(search_for_stringonly)

print('-------------------------------')

search_for_stringonly=soup.findAll(text=['Yuri','Naoki','Keiko','Takato'])

print(search_for_stringonly)

print('---------------------------------------------')

class_search=soup.find(attrs={'class':'Female'})

print(class_search)

print('---------------------------------------------')

# def is_girl(tag):
#     return tag.has_attr("id")and tag.get("id")=='woman'
#     is_girl=soup.find(is_girl)

# print(is_girl.li.div.string)

print('---------------------------------------------')

for tag in soup.findAll(True):
    print(tag.name)

print('---------------------------------------------')

find_class=soup.findAll(class_="Male")
print(type(find_class))

print(find_class)

print('---------------------------------------------')

print(find_class[1])

print('---------------------------------------------')

print(find_class[0])

find_class=find_class[0]

find_parent=find_class.find_parents("ul")
print(find_parent)

print('---------------------------------------------')
find_class=soup.find(class_='Male')

print(type(find_class))
print(find_class)

print('---------------------------------------------')
do_it=soup.findAll(class_='Female')
find1=do_it[0]
print(find1)

print('---------------------------------------------')

find_para=find1.find_parents('ul')
print(find_para)

print('--------------------------------------------')

yyy=soup.find(id="man")

print(yyy)

print('--------------------------------------------')

next_sibling=yyy.findNextSiblings()
print(next_sibling)

print('--------------------------------------------')

next_sibling=yyy.findNextSibling()
print(next_sibling)

print('--------------------------------------------')

all_previous=yyy.findAllPrevious()
print(all_previous)
print('--------------------------------------------')

all_previous=yyy.findPrevious()
print(all_previous)


