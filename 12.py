from bs4 import BeautifulSoup
import requests

#simply add the website links

url='http://lohitbadiger.herokuapp.com'

#access the result through requests objects

store=requests.get(url)

#im checking the response of the website

print(store)

# load the page content
page_content=store.content

# print(page_content)

#create soup object
soup=BeautifulSoup(page_content,'html.parser')

#view the contents

print(soup)

print('----------------------------------')

print(soup.prettify())

print('----------------------------------')

#view the original encording of the website

print(soup.original_encoding)

print('----------------------------------')

#format the tag to a to xml

# print(soup.body.a.prettify(formatter='xml'))

print('----------------------------------')

#define a custom functions to convert string values to uppercase

def upperCaseFn(strt):
    return strt.upper()

print('-------------------------')

#format using custom function for outputting string texts in uppercase
print(soup.body.a.prettify(formatter=upperCaseFn()))








