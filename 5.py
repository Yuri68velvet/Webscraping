
# # I'm goone run this part in jupyter

from bs4 import BeautifulSoup
import re

email_example="""
abc@emailgmail.com
"""
soup_email=BeautifulSoup(email_example,"lxml")

email_ID_regexp=re.compile("/w+@/./w+")
email_id=soup_email.find(text=email_ID_regexp)
print(email_id)

#Im gone run this part in jupyter

from bs4 import BeautifulSoup
import re

email_example="""
abc@emailgmail.com
"""
soup_email=BeautifulSoup(email_example,"lxml")

email_ID_regexp=re.compile("\w+@\.\w+")
email_id=soup_email.find(text=email_ID_regexp)
print(email_id)


from bs4 import BeautifulSoup as bs

htmlfile="5.html"
with open(htmlfile,"r")as organization:
    soup=bs(organization,'html.parser')

print(soup.contents)

print('-----------------------------------')
table=soup.find("table")
print(table)

print('----------------------------------')
print(type(table))

print
print(table)('-----------------------------------')

print'-----------------------------------')name")

table=soup.find(id="(
print(table)

print('-----------------------------------')
print(table.find(id="lohit").string)
#same way
print(table.tr.td.string)

print('--------------------------------------')
print(table.find(attrs={"class":"lo"}))

print("---------------------------------------------")
search=soup.findAll(text=["whitefield","Bangalore"])
print(search)

# # ^=先頭の文字
# # ＄＝最後の文字

