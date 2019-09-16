
from bs4 import BeautifulSoup
data_SL="""

<ul class="jambotron mt-5">
    <div>
            <h5>This is new Round of Tag</h5>
    </div>
            <li>
                    <a href="lohitbadiger.heroku" id="lohit">This is my personal website</a>
            </li>
            <li>
            <a href="googele.heroku" id="google">This is my search engine</a>
            </li>
            <li>
                    <a href="match_me.heroku" id="match">This is match me site</a>
            </li>
            <li>
                    <a href="okgoing.heroku" id="ok">This is ok and going</a>
            </li>
</ul>"""

soup_SL=BeautifulSoup(data_SL,'html.parser')

print(soup_SL)

print('--------------------------------------------')

print(soup_SL.get_text())


print('--------------------------------------------')

from bs4 import SoupStrainer
tags_with_LabLink=SoupStrainer(id='lohit')


print(BeautifulSoup(data_SL,'html.parser',parse_only=tags_with_LabLink))





