#import lib

from bs4 import BeautifulSoup as bs

#using the srllib Lib for this

from urllib.request import urlopen as UReq

my_url='https://www.flipkart.com/search?q=iphones&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&sort=recency_desc'


uClient=UReq(my_url)

#open the urllib for the reading the file 'established 406

page_html=uClient.read()

#connection being stopped

uClient.close()

#creating the soup container

page_soup=bs(page_html,"html.parser")

containers=page_soup.findAll("div",{"class":"_3O0U0u"})


#Total mobile phone
print(len(containers))
# print(bs.prettify(container[0]))


print('-----------------------------------------------')

container=containers[0]
print(container.div.img['alt'])

print('--------------------price---------------------------')


price=container.findAll("div",{"class":"col col-5-12 _2o7WAb"})

print(price[0].text)

print('------------------rating--------------------------------')

rating=container.findAll("div",{"class":"hGSR34"})
print(rating[0].text)

print('--------------------------------------------------')

filename='flikart_iphones.csv'

f=open(filename,'w')


header="Products Name,Pricing,Ratings\n"

print(f.write(header))

for container in containers:
    product_name=container.div.img['alt']
    price_container=container.findAll('div',{'class':"col col-5-12 _2o7WAb"})
    price=price_container[0].text

    rating_container=container.findAll("div",{"class":"hGSR34"})
    rating=rating_container[0].text

    print('product_name'+product_name)
    print('price'+price)
    print('rating'+rating)


#moifying the output
    print('--------------------------------------------')

    trim_price=''.join(price.split(','))
    rm_rupee=trim_price.split("₹")
    add_rs_price="Rs." + rm_rupee[1]
    split_price=add_rs_price.split("E")
    final_price=split_price[0]
    split_rating=rating.split(" ")
    final_rating=split_rating[0]
    print(product_name.replace(",", "|")+ " ," + final_price + "," + final_rating + "\n")
    f.write(product_name.replace(",",'|')+","+final_price+","+final_price+'\n')
    
f.close()










