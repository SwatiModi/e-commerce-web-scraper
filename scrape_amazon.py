import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from urllib.request import urlopen 
import requests

headers_std = {
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
'Content-Type': 'text/html',
}

url = "https://www.amazon.in/s?k=stilleto+heels&page=2&qid=1557851935&ref=sr_pg_2"
html = requests.get(url,headers=headers_std).text
soup = BeautifulSoup(html,'lxml')

product_name_class = "a-size-base-plus a-color-base a-text-normal"
discount_price_class = "a-price" 
actual_price_class = "a-price-whole"
rating_class = "a-icon-alt"
no_of_rat_class = 'a-size-base'
main_page_url_class ="a-link-normal a-text-normal"

#scrape the product details
product_names = soup.find_all("span", {"class":product_name_class})
product_prices = soup.find_all("span",{"class":actual_price_class})
ratings = soup.find_all("span",{"class":rating_class})
no_of_ratings = soup.find_all('span',{'class':no_of_rat_class})
main_page_urls = soup.find_all("a",{'class': main_page_url_class})

print(product_names[0].text.strip())
print(product_prices[0].text.strip())
print(ratings[0].text.strip())
# print(no_of_ratings[0].content)
print('amazon.in'+ main_page_urls[0].get('href').strip())

print(len(product_names))
print(len(product_prices))
print(len(ratings))
print(len(main_page_urls))

product_names_df = []
product_prices_df = []
ratings_df = []
main_page_urls_df = []

#make a dataframe
for i in range(len(product_names)):

	product_names_df.append(product_names[i].text.strip())
	product_prices_df.append(product_prices[i].text.strip())
	main_page_urls_df.append("amazon.in" + main_page_urls[i].get('href').strip())

	try:
		ratings_df.append(ratings[i].text.strip())
	except:
		ratings_df.append(None)

df = pd.DataFrame({'product_name':product_names_df,'price (INR)':product_prices_df,'rating':ratings_df,'product_page':main_page_urls_df})
print(df.head())

df.to_csv('amazon_main_page_scraping.csv',index=False)