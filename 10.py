from bs4  import BeautifulSoup

data_SL="""

<ul class="content-col_discover">
    <h5>Discover</h5>
    <li><a href="http://community.simplilearn.com/" id="users">Free Resources</a></li>
    <li><a href="career-data-labs" id="lab">Career Data labs</a></li>
    <li><a href="/scholarships-for-veterans" id="scholarship">
    <li><a href="http://www.simplelearn.com/feed/" id="rss">RSS FEED</a></li>


</ul>"""

#<!--Create soup object-->
soup_SL=BeautifulSoup(data_SL,'html.parser')

#if i do this get all info
print(soup_SL)

#parse only part of the document,text values for tags using getText method

print('_______________________Get only req___________________')
print(soup_SL.get_text())

#import soupstrainer class for parsing the desied part of the web document
from bs4 import SoupStrainer

#create object to parse only the id (link) with lab
tags_with_LabLink=SoupStrainer(id='lab')

#print the part of the parsed document

print(BeautifulSoup(data_SL,'html.parser',parse_only=tags_with_LabLink))

print('--------------------------')

print(BeautifulSoup(data_SL,'html.parser',parse_only=tags_with_LabLink).prettify())