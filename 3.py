from bs4 import BeautifulSoup
html_doc="""<!DOCTYPE html>

<html>
    <body>
        <div class="organizationlist">
            <ul id="HR">
                <li class="HR">
                    <div class="HRmanager">
                    <div class="ID">101</div>
                </li>
                <li class="ITmanager">
                    <div class="name">Daren</div>
                    <div clas="ID">65</div>
                </li>
            </ul>
        </div>
    </body>
</html>
"""

soup=BeautifulSoup(html_doc,'html.parser')

print(type(soup))

print('____________________')
tag=soup.div
print(tag.string)

for ("div",attrs={"class":"HRmanager_name"})

