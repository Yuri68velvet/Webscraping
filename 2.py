from bs4 import BeautifulSoup as bs

store="""
<!DOCTYPE>

<html lang="en">
            <head>
                        <meta charset="UTF-8">

                        <title>This is 2nd one</title>

            </head>

<body>
<p class="new">Lohit</p>
<h1 class="new">Lohit badiger </h1>

<h2>London</h2>
<h2>Mumbai</h2>

<b> <!--"New Comment line"--></b>
</body>
</html>
"""

soup=bs(store,'html.parser')
print(type(soup))

tag=soup.p
print('__________________________________')
print(tag)

print('_________________________________')
comment=soup.b.string
print(type(soup))

print('__________________________________')
print(tag.string)

print('____________________________________')
b_tag=soup.b
print(b_tag)