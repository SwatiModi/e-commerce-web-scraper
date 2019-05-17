import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from urllib.request import urlopen 
import requests

headers_std = {
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
'Content-Type': 'text/html',
}

url = "https://www.amazon.in/Casual-Shoes-50-Off-or-more/s?rh=n%3A9780814031%2Cp_n_pct-off-with-tax%3A2665401031"
html = requests.get(url,headers=headers_std).text
soup = BeautifulSoup(html,'lxml')

#scraping using asin_number of the product
asin_number_list = soup.find_all("div", {"class":"s-result-item"})
# print(asin_number_list)
# print(asin_number_list[0])

# print(asin_number_list[0].get('data-asin'))

asins = []

# get data-asin for all products and save as a csv
for i in range(len(asin_number_list)):
	asins.append(asin_number_list[i].get('data-asin'))

print(len(asins))
print(asins)

asin_df = pd.DataFrame({'ASIN':asins})
asin_df.to_csv('ASINs.csv',index=False)