
#run this file in jupiter
#import the BS4　Lib

from bs4 import BeautifulSoup

#import function

import requests

#url from the website which i want to scrape

url=requests.get('https://www.nytimes.com/interactive/2017/06/23/opinion/trumps-lies.html')

soup=BeautifulSoup(url.text,'html.parser')
# print(soup)

results=soup.find_all('span',attrs={'class':'short-desc'})

records=[]

for result in results:
    date=result.find('strong').text[0:-1]+', 2019'
    lie=result.contents[1][1:-2]
    explanation=result.find('a').text[1:-1]
    url=result.find('a')['href']
    records.append((date,lie,explanation,url))

#using the pandas as data framework foe easy listening
import pandas as pd

#creating the date in different format
df=pd.DataFrame(records,columns=['date','lie','explanation','url'])

df.to_csv('Trump_lies.csv',index=False,encoding='utf-8')

