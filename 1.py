from bs4 import BeautifulSoup
# we will start building website
html_doc="""<!DOCTYPE html>
<html lang="en">
           <head>
           <meta charset="UTF-8">
           <meta name="viewport" content="width=device-width, inital-scale=1.0">
           <meta http-equiv="X-UA-Compatible" content="chorm">
           <title> Lohith Website  Document</title>
           </head>
<body>
           <h1> Heading Tag</h1>
                   <b>""This is 'comment' l""</b>
                   <p title="This is about me" class="test">My first website web scrape</p>
                       <div class="cities">
                           <h2>London</h2>
                           <h2>Mumbai</h2>
                       </div>
</body>
</html>"""
soup=BeautifulSoup(html_doc, 'html.parser')
print('---------Type of the soup------------------------')
print(type(soup))


print('---------------printing the soup---------------')
print(soup)

print('-----------------tag----------------------')

tag=soup.p
print(tag)

comment=soup.b.string

print(type(comment))

print('-------------Im printing comment-----------------')

print(comment)

print('---------print comment by slicing-------------')

print(comment[0:])
print('-----------------------------------------------')
print(comment[0:10])

print('______________print comment by slicing___________')
print(comment[0:6:2])

print('______________________________________________')

print(tag.string)
print('_____________________________________________')
print(tag.attrs)

print(tag.string)