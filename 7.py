from bs4 import BeautifulSoup as Bs

school="""<address>
    <head>
        <title>This is spiceup academy</title>


    </head>
    <body>
        
    </body>
    <schools>
<p class="title">
<b>This is located in the heart of Bangalore city Koramangara</b>
    </schools>
</p>
<classrooms>
    <classroom id="555F"></classroom>
        <teacher>Lohit</teacher>
        <subject>Pythin and Machine Learning</subject>
        <dob>30-10-1919</dob>
        <date>10-10-2019</date>
        <review>Amazing story ahead</review>


        </classroom>

    <good id="666F">
        <teacher>Susumu</teacher>
        <subject>Php and python</subject>
        <dob>02-10-2010</dob>
        <date>03-20-1099</date>
        <review>bangalore </review>
    
    </good>

    <bad id="777F">

        <teacher>KOyta</teacher>
        <subject>Ruby And Machine Learning</subject>
        <dob>20/10/1980</dob>
        <date>08-10-2018</date>
        <review>Good to meet you and to study with you</review>

    </bad>

    </classrooms>
    </schools>
    </body>
    </address>
    """


ss=Bs(school,'html.parser')
print(ss)

print('--------------------------------------')

print('-----------------contents---------------------')

print(ss.contents)

print('----------------address------------------')
print(ss.address)

print('------------------head-------------------')
print(ss.head)

print('--------------------------------------')

title_tag=ss.title

print(title_tag)
print('--------------------------------------')

#navigate down:in this im using descendants to get next tag

for me in ss.head.descendants:
    print(me)

print('----------------------------------------------')
#this will go to the next tag..
#Here there is no tag in after the <teacher>Tag so this will give me string

for me in ss.teacher.descendants:
    print(me)

#navigate down using the stripped string method

#now we will det all string value preset inside the html documents
for string in ss.stripped_strings:
    print(repr(string))


print('----------------------------------------------')

for values_without_quotes in ss.stripped_strings:
    print(values_without_quotes)

print('----------------------------------------------')
print('----------------------------------------------')

#navigate up using the method
print(title_tag.parent)


print('---------------------navigate_up---------------------')

#taking one parent

navigate_up=ss.subject
print(navigate_up)

#navigating element object to navigate back and forth

back_and_forth=ss.address.bad



print('----------------------------------------------')
ok=next_element=back_and_forth.next_element.next_element
print(ok)





