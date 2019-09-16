# import the required library

from bs4 import BeautifulSoup

#import the web scraping file which is 4.html

HTMLFILEPATH="4.html"
with open(HTMLFILEPATH,'r')as organization:
    soup=BeautifulSoup(organization,'html.parser')

#view the contents from the soup
print(soup.contents)

print('-------------------------------------------------')

# search the content of the soup object

tag_li=soup.find("li")

print(type(tag_li))

print('-------------------------------------------------')

#printing the object/element

print(tag_li)

print('-------------------------------------------------')

print('-----start  searching in the tree by find method---------')

#select the 'HR' id

find_id=soup.find(id='HR')
print(find_id)

print('-------------------------------------------------')
#print the string value

print(find_id.div.string)


print('---------------***----------------')

#search for the particular css attr

search_for_stringOnly=soup.find(text=['Lohit',"KOTA"])
print(search_for_stringOnly)

print('---------------------////----------------------------')
search_for_stringOnly=soup.findAll(text=['Lohit',"KOTA"])
print(search_for_stringOnly)

print('--------------------------------------------------')


#to get the 'class' of IT manager

css_class_search=soup.find(attrs={"class":"ITmanager"})

print(css_class_search)

print('--------------------------------------------------')

#create a function to search the document based on the name

def is_account_manager(tag):
    return tag.has_attr("id")and tag.get("id")=="Finance"

is_account_manager=soup.find(is_account_manager)


print(is_account_manager.li.div.string)

print('--------------------------------------------------')

#This will give you all the tag with there string names

for tag in soup.findAll(True):

    print(tag.name)

print('--------------------------------------------------')

print('---------------HR manager----------------------------')

#this step to get class of HRManager
#this is present as list

find_class=soup.findAll(class_="HRmanager")
print(type(find_class))

print('--------------------------------------------------')

#Now im printing the HRmanager Tag index of 0.

print(find_class)

print('--------------------------------------------------')
print(find_class[0])

print('--------------------------------------------------')
#this will give the index 1

print(find_class[1])
print('--------------------------------------------------')
#lets store find_class zero index in find_class variable

find_class=find_class[0]

find_parent=find_class.find_parents("ul")
print(find_parent)

print('--------------------------------------------------')


find_class=soup.find(class_="HR")
print(type(find_class))

print(find_class)



print('------------------------------------------')
do_it=soup.findAll(class_='HRManager1')
find1=do_it[0]

print(find1)

print('--------------------------------------------------')

find_para=find1.find_parents('ul')
print(find_para)

# #This will give the id="IT"

org=soup.find(id="IT")

print(org)
print('-----------------------------------------------------')
#all the next tags im getting

next_sibling=org.findNextSiblings()
print(next_sibling)

print('-----------------------------------------------------')

#only the text tag im getting
next_sibling=org.findNextSibling()
print(next_sibling)
print('-----------------------------------------------------')


#search all previous tags

all_previous=org.findAllPrevious()
print(all_previous)

print('-----------------------------------------------------')


all_previous=org.findPrevious()
print(all_previous)
