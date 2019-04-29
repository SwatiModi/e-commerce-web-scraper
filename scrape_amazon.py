import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from urllib.request import urlopen 
from nltk import clean_html
import requests

url = "https://www.amazon.in/Casual-Shoes-50-Off-or-more/s?rh=n%3A9780814031%2Cp_n_pct-off-with-tax%3A2665401031"

r = requests.get(url)
# html = urlopen(url)
# print(html)
# soup = BeautifulSoup(html,"html.parser")
# print(type(BeautifulSoup))

soup = BeautifulSoup(r.content,"html.parser")

title = soup.title
# print(title.string)
# print(soup.prettify())

# product_name_class = "a-size-base-plus a-color-base a-text-normal"
# description_class = "_2mylT6"
# discount_price_class = "a-price" 
# actual_price_class = "a-price-whole"
# product_image_class = "_3togXc"
# discount_percent_class = "VGWI6T"
# footware_size_class = "o_gtXB"
# main_product_page = "_3dqZjq"
asin_number = ""

asin_number_list = soup.find_all("div", {"class":"sg-col-4-of-24"})

# product_name_1 = soup.find_all("span", {"class":product_name_class})
# product_desc_1 = soup.find_all("a",{"class":description_class})
# product_dis_price_1 = soup.find_all("span", {"class":discount_price_class})
# product_actual_price_1 = soup.find_all("span",{"class":actual_price_class})
# discount_percent = soup.find_all("div",{"class":discount_percent_class})
# product_image = soup.find_all("img",{"class": product_image_class})
# size = soup.find_all("div",{"class":footware_size_class})
# main_product_page_1 = soup.find_all("a",{"class":main_product_page})

print(asin_number_list)