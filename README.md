# e-commerce-web-scraper

**File** : *_amazon_search_image_scraper.py_*<br>
**Description** : Get images of available products on amazon for a particular search query <br>
**Steps** 
1. Go to Amazon.in
2. Enter the search query for product 
3. Copy the `URL` 
4. Execute `amazon_search_image_scraper.py` file
``` console
$ python amazon_search_image_scraper.py
  Search Query URL: 
   ```
**Result** : Get the images of products saved in `images/` folder 

**Example** :
![](/ReadmeImages/eg1img1.png)

![](/ReadmeImages/eg1img2.png)

**Usecase** : 
It can be useful for creating dataset for training Machine learning or Deep learning models on Fashion data.

<br>
<br>

**File** : *_asin_scraper.py_*<br>
**Description** : Get ASIN of available products on amazon for a particular search query<br>
**Steps** 
1. Go to Amazon.in
2. Enter the search query for product 
3. Copy the `URL` 
4. Execute `asin_scraper.py` file
``` console
$ python asin_scraper.py 
  URL for scraping
   ```
**Result** : Get the ASIN numbers of the products in `ASINs.csv`

**Example** :
![](/ReadmeImages/eg2img1.png)

![](/ReadmeImages/eg2img2.png)

**Usecase** : 
It is useful later for scraping all details of the product using `scrape_product_details_using_asins.py`

**_What is ASIN_** - ASIN stands for Amazon Standard Identification Number. It's a 10-charcter alphanumeric unique identifier that's assigned by Amazon.com and its partners. It's used for product-identification within Amazon.com organization. ASINs are only guaranteed unique within a marketplace.

<br>
<br>

**File** : *_scrape_product_details_using_asins.py_*<br>
**Description** : Get the product details like _product_name, brand_name, product_image_urls, price, rating and no_of_reviews<br>
**Steps** 
1. Go to Amazon.in
2. Enter the search query for product 
3. Copy the `URL` 
4. Execute `scrape_product_details_using_asins.py` file
``` console
$ python asin_scraper.py 
   ```
**Result** : Get the products details for all the ASIN numbers from input file `ASINs.csv` and store details in `ASIN_product_details.csv`

**Example** :
![](/ReadmeImages/eg3img1.png)

![](/ReadmeImages/eg3img2.png)

**Usecase** : 
It gets data which can be useful for various applications like price analysis, Market Analysis, Price Comparison gaining rich insights to help them develop strategies to compete against their competitors and also save time and cost in the process, 
