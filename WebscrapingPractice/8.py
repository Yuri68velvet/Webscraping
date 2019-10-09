#I'm scraping Yahoo News

from bs4 import BeautifulSoup as bs

import requests

html=requests.get('https://news.yahoo.co.jp')

yahoo=bs(html.content,'html.parser')

print(html)



# results=soup.find_all('span',attrs={'class':'short-desc'})

# records=[]

# for result in results:
#     date=result.find('time').text[0:-1]+', 2019'
#     topic=result.contents[1][1:-2]
#     explanation=result.find('a').text[1:-1]
#     url=result.find('a')['href']
#     records.append((date,topic,explanation,url))


# print(date)