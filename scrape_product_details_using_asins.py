import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from urllib.request import urlopen 
import requests

headers_std = {
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
'Content-Type': 'text/html',
}

asins_df = pd.read_csv('ASINs.csv')
# print(asins_df.head())

asin_list = asins_df['ASIN']
# print(asin_list)

image_list_span_class = 'a-button-text' #span containing the img tag
brand_name_class = 'bylineInfo'  #can get link of brand and name of brand from the a-link
product_name_class = 'productTitle' #span
rating_class = 'a-icon-alt'  #span
no_of_rat_class = 'acrCustomerReviewText' #span
# actual_price_class = 'priceBlockStrikePriceString'   # this discounted price is not presernt for all
sell_price_id = 'priceblock_saleprice'
sell_price_range_id = 'priceblock_ourprice'

# blank lists for storing the final data to be stored in the csv file
product_names = []
brand_names = []
ratings = []
no_of_ratings = []
product_images = []
product_prices = []

for asin in asin_list:
	url = "https://www.amazon.in/dp/" + str(asin)
	html = requests.get(url,headers=headers_std).text
	soup = BeautifulSoup(html,'lxml')

	#scrape the product details
	image_list = soup.find_all('span',{'class':image_list_span_class})
	brand_name = soup.find_all('a',{'id':brand_name_class})
	product_name = soup.find_all('span',{'id':product_name_class})
	rating = soup.find_all('span',{'class':rating_class})
	no_of_rat = soup.find_all('span',{'id':no_of_rat_class})
	# actual_price = soup.find_all('span',{'class':actual_price_class})
	# selling_price = soup.find_all('span',{'id':sell_price_id})
	sell_price_range = soup.find('span',{'id':sell_price_range_id})

	image_urls = []

	for image in image_list:
		try:
			image_url = image.find('img').get('src')
			# print(image_url)
			image_urls.append(image_url)
		except:
			# print('NoneType Object in soup')
			pass

	product_images.append(str(image_urls))

	# will use assert statements here later instead of print and along with error statement, will append a blank string
	try:
		# for some products brand_name is not present so try except is useful here
		# print(brand_name[0].text.strip())			
		brand_names.append(brand_name[0].text.strip())
	except:
		# print('brand_name problem')
		brand_names.append('')


	try:
		# print(product_name[0].text.strip())
		product_names.append(product_name[0].text.strip())
	except:
		# print('product name problem')
		product_names.append('')

	try:
		# print(rating[0].text.strip())
		ratings.append(rating[0].text.strip())
	except:
		# print('problem in product\'s rating')
		ratings.append('')

	try:
		# print(no_of_rat[0].text.strip())
		no_of_ratings.append(no_of_rat[0].text.strip())
	except:
		no_of_ratings.append('')
		# print('problem in no.of ratings')

	try:
		# print(sell_price_range.text.strip())
		product_prices.append(sell_price_range.text.strip())
	except:
		# print(url)
		# print('Problem here')
		product_prices.append('')

# print(len(product_images))
# print(len(brand_names))
# print(len(product_prices))
# print(len(product_images))
# print(len(ratings))
# print(len(no_of_ratings))

# make a dataframe for csv
df = pd.DataFrame({'product_name':product_names,'brand_name':brand_names,'images':product_images,'price':product_prices,'product_rating':ratings,'no. of ratings':no_of_ratings})
df.to_csv('ASIN_product_details.csv',index=False)