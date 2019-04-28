import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from urllib.request import urlopen 
from nltk import clean_html
import requests

url = "https://www.flipkart.com/mens-footwear/pr?sid=osp%2Ccil&p%5B%5D=facets.serviceability%5B%5D%3Dtrue&p%5B%5D=facets.price_range.from%3D99&p%5B%5D=facets.price_range.to%3DMax&sort=popularity&offer=nb:mp:034eb2ea22&fm=neo%2Fmerchandising&iid=M_4a64b86f-6af0-4455-9387-0054eecdc9c4_2.1X7HZZD1MVSM&ppt=Homepage&ppn=Homepage&otracker=hp_omu_Deals%2Bof%2Bthe%2BDay_2_1X7HZZD1MVSM_0&otracker1=hp_omu_PINNED_neo%2Fmerchandising_Deals%2Bof%2Bthe%2BDay_NA_dealCard_cc_2_NA_view-all_0&cid=1X7HZZD1MVSM"

r = requests.get(url)
# html = urlopen(url)
# print(html)
# soup = BeautifulSoup(html,'html.parser')
# print(type(BeautifulSoup))

soup = BeautifulSoup(r.content,'html.parser')

title = soup.title
# print(title.string)
# print(soup.prettify())

product_name_class = "_2B_pmu"
description_class = "_2mylT6"
discount_price_class = "_1vC4OE"
actual_price_class = "_3auQ3N"
product_image_class = "_3togXc"
discount_percent_class = "VGWI6T"
footware_size_class = "o_gtXB"
main_product_page = "_3dqZjq"

product_name_1 = soup.find_all("div", {"class":product_name_class})
product_desc_1 = soup.find_all("a",{"class":description_class})
product_dis_price_1 = soup.find_all("div", {"class":discount_price_class})
product_actual_price_1 = soup.find_all("div",{"class":actual_price_class})
discount_percent = soup.find_all("div",{"class":discount_percent_class})
product_image = soup.find_all("img",{"class": product_image_class})
size = soup.find_all("div",{"class":footware_size_class})
main_product_page_1 = soup.find_all("a",{"class":main_product_page})

print(product_name_1[0].text.strip())
print(product_desc_1[0].text.strip())
print(product_dis_price_1[0].text.strip())
print(product_actual_price_1[0].text.strip())
print(discount_percent[0].text.strip())
# print(product_image[0]['src'])
# print(size[0])
print("www.flipkart.com"+ main_product_page_1[0]['href'])

print(len(product_name_1))

# url2 = url + "&page=2" 
# r = requests.get(url2)
# soup = BeautifulSoup(r.content,'html.parser')

# product_name_2 = soup.find_all("div", {"class":product_name_class})
# product_dis_price_2 = soup.find_all("div", {"class":discount_price_class})
# product_actual_price_2 = soup.find_all("div",{"class":actual_price_class})

# print(product_2[0].text.strip())
# print(product_dis_price_2[0].text.strip())
# print(product_actual_price_2[0].text.strip())

# print(len(product_2))

# url3 = url + "&page=3" 
# r = requests.get(url3)
# soup = BeautifulSoup(r.content,'html.parser')

# product__name_3 = soup.find_all("div", {"class":product_name_class})
# product_dis_price_3 = soup.find_all("div", {"class":discount_price_class})
# product_actual_price_3 = soup.find_all("div",{"class":actual_price_class})

# print(product_3[0].text.strip())
# print(product_dis_price_3[0].text.strip())
# print(product_actual_price_3[0].text.strip())

# print(len(product_3))