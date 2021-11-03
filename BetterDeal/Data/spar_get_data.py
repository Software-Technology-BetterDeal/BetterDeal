

from bs4 import BeautifulSoup, NavigableString
import requests
import csv
import re
import os
from datetime import datetime

def get_name( s):
   
    r=s.split('/')
    return r[len(r)-1]
def get_unit_price( s):
    try:
        r=s[s.index("(")+1:s.index(")")]
    except:
        r=""
        pass
    return r

def del_spaces(s):
    return re.sub('\s+','',s)

csv_file = open('spar_discounts.csv', "w", encoding="Cp1250") 

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['product_name', 'price', 'unit_price', 'image_name','integration_date','supermarket'])

#for i in range(1,30):
source = requests.get('https://www.spar.hu/onlineshop/').text
soup = BeautifulSoup(source, 'lxml')


all = soup.find_all('div', class_='singleProductContainer')
for product in all:
    product_price = product.find('label',class_='priceInteger')
    if (product_price is not None):
       product_price=product_price.text
    else:
        product_price=None
   

    product_name = product.find('label',class_='productTitle')
    if (product_name is not None):
       #product_name=del_spaces(product_name.text)
        product_name=product_name.a.text

    product_unit = product.find('label',class_='extra-info-price__price')
    if (product_unit is not None):
        product_unit=re.sub('\s+','',product_unit.text)
#     product_unit_price = product.find('div',class_='product__secondary-text')
#     if (product_unit_price is not None):
#         product_unit_price=get_unit_price(re.sub('\s+','',product_unit_price.text))
#         #print(product_unit_price)
    product_img_name = product.find('img')
    product_img_name = del_spaces(get_name(product_img_name['src']))
    

#     if (product_img_name is not None):
#         product_img_name=get_name(product_img_name.img['src'])
#     elif (product_img_name_alt is not None):
#         product_img_name = get_name(product_img_name_alt.img['src'])
    
    integration_date=datetime.now()
    if (not product_name or not product_price):
        continue
    csv_writer.writerow([product_name, product_price, product_unit,product_img_name,integration_date,"spar"])


csv_file.close()
#os.system("python get_imgs.py spar")



