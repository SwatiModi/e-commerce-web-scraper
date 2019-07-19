import urllib.request
from bs4 import BeautifulSoup
import re
from time import sleep
import os
from sys import exit
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC  
from selenium.webdriver.common.by import By  
from selenium import webdriver
import pandas as pd

sleep_time = 1

def download_items(url_set,dest_dir,item_category,website):
    
    """
    This function download the items referred by URL in given set of url.

    Parameters :
    arg1 - url_set (Set): A set containing URL to items
    arg2 - dest_dir (string): Path to Destination Directory where items are to be downloaded
    arg3 - item_category (string ) : A string specifying the category to which the item belongs

    Returns:
        NONE
    """

    
    for index,url in enumerate(url_set):
        path = dest_dir + website + "_" + item_category + "_" + str(index) + ".jpg"
        print(path)
        try:
            urllib.request.urlretrieve(url, path)
        except :
            print("An excpetion occured during downloading data \n")
            continue
    return

def get_html_page(url,headers):
    try:
        html = urllib.request.Request(url=url,headers=headers)
        response = urllib.request.urlopen(html)
        page = response.read()
    except :
        print("An error occured while connection setup.")
        print("Terminating the program.... ")
        exit()
        
    return page

def get_items_from_amazon(item_category):
    url_set = set()
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
        }
    item_name = item_category.replace(" ", "+")
    print(" Going TO Dig Amazon India ... ")
    root_url = "https://www.amazon.in/s?k=" + item_name

    page = get_html_page(root_url,headers)
    bs = BeautifulSoup(page,'html.parser')     
    
    '''# Get the total number of pages available related to this particular search
    page_count_list = bs.find_all('li',class_="a-disabled")
    tempList =  page_count_list[-1].contents
    total_pages = int(tempList[0])'''

    images = bs.find_all('img', {'src':re.compile('.jpg')})
    for image in images: 
        url_set.add(image['src'])

    #for page_number in range(2,total_pages+1):
    page_number = 1
    old_url_set_len = len(url_set)
    minimum_expected_items_per_page = 10
    while True:
        page_number += 1
        sleep(1)
        url = root_url + "&page=" + str(page_number)
        page = get_html_page(url,headers)
        bs = BeautifulSoup(page,'html.parser')

        images = bs.find_all('img', {'src':re.compile('.jpg')})
        for image in images: 
            url_set.add(image['src'])
         
        current_url_set_len = len(url_set)
        if ( current_url_set_len - old_url_set_len ) < minimum_expected_items_per_page :
            break
        else:
            old_url_set_len = current_url_set_len

    return url_set

def get_items_from_myntra(item_category):
    url_set = set()
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
        }
    item_name = item_category.replace(" ", "-")
    print(" Going TO Dig myntra ... ")

    root_url ="https://www.myntra.com/amp/" + item_name + "?rows=50&p="
    url  = root_url + str(1)
    print(url)
    page = get_html_page(url,headers)
    print("page retrieved")
    bs = BeautifulSoup(page,'html.parser') 
    images = bs.find_all('amp-img', {'src':re.compile('.jpg')})
    for image in images: 
        url_set.add(image['src'])
    
    page_count = 2
    print("50 images exist per page : ")
    print("would you like to set a limit on the number of pages to be retrieved(y/n): ")
    response = input("Enter your response : ") 
    
    forceStop = False
    if response == 'y':
        forceStopVal = int(input("Enter the maximum limit on the number of pages to be retrieved : "))
        forceStop = True

    while True:  
        if forceStop is True and forceStopVal == page_count:
            break

        url = root_url + str(page_count)
        page = get_html_page(url,headers)
        bs = BeautifulSoup(page,'html.parser')
        images = bs.find_all('amp-img', {'src':re.compile('.jpg')})
        
        if len(images) < 6 :
            break
        else :
            for image in images:
                 url_set.add(image['src'])    
        page_count += 1

    return url_set
    

def get_items_from_koovs(item_category):
    url_set = set()
    driver =  webdriver.Chrome()

    item_name = item_category.replace(" ", "-")
    root_url ="https://www.koovs.com/" + item_name

    print(root_url)
    driver.get(root_url)
    
    

    max_page = int(input("Enter the number of pages you want to scrap : "))
    
    current_page_index = 0
    page = driver.page_source 
    bs = BeautifulSoup(page,'html.parser')   
    images = bs.find_all('img', {'src':re.compile('.jpg')})      
    for image in images:
        url_set.add(image['src'])

    while True:     
        if current_page_index == max_page :
            print("Total images retrieved " + str(len(url_set))  )
            extra_page_count = int(input("Enter the extra number of pages you want to scrap ( 0 if no more to scrap) : "))
            if extra_page_count == 0:
                break
            else:
                max_page = max_page + extra_page_count
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);") 
        driver.execute_script("scrollBy(0,-500);")
        try:
            lm = driver.find_element_by_class_name("list-load-more")
            lm.click()
        except:
            break

        sleep(sleep_time)
        
        page = driver.page_source 
        bs = BeautifulSoup(page,'html.parser')   
        images = bs.find_all('img', {'src':re.compile('.jpg')})      
        for image in images:
            url_set.add(image['src'])
    
        current_page_index += 1

    driver.quit()
    return url_set

def get_items_from_ajio(item_category):
    url_set = set()
    driver =    webdriver.Chrome()

    item_name = item_category.replace(" ", "%20")
    root_url ="https://www.ajio.com/search/?text=" + item_name

    print(root_url)
    driver.get(root_url)

   
    max_page = int(input("Enter the number of pages you want to scrap : "))
    
    current_page_index = 0
    page = driver.page_source 
    bs = BeautifulSoup(page,'html.parser')   
    images = bs.find_all('img', {'src':re.compile('.jpg')})      
    for image in images:
        url_set.add(image['src'])

    while True:     
        if current_page_index == max_page :
            print("Total images retrieved " + str(len(url_set))  )
            extra_page_count = int(input("Enter the extra number of pages you want to scrap ( 0 if no more to scrap) : "))
            if extra_page_count == 0:
                break
            else:
                max_page = max_page + extra_page_count
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);") 
        driver.execute_script("scrollBy(0,-500);")


        sleep(sleep_time)

        page = driver.page_source 
        bs = BeautifulSoup(page,'html.parser')   
        images = bs.find_all('img', {'src':re.compile('.jpg')})      
        for image in images:
            url_set.add(image['src'])

        current_page_index += 1

    page = driver.page_source 
    bs = BeautifulSoup(page,'html.parser')   
    images = bs.find_all('img', {'src':re.compile('.jpg')})      
    for image in images:
        url_set.add(image['src'])

    driver.quit()
    return url_set

def get_items_from_fynd(item_category):
    url_set = set()
    driver =    webdriver.Chrome()

    item_name = item_category.replace(" ", " ")
    root_url =" https://www.fynd.com/products-list?q=" + item_name 

    print(root_url)
    driver.get(root_url)


    max_page = int(input("Enter the number of pages you want to scrap : "))

    current_page_index = 0
    page = driver.page_source
    bs = BeautifulSoup(page,'html.parser')
    images = bs.find_all('img', {'src':re.compile('.jpg')})
    for image in images:
        url_set.add(image['src'])

    while True:
        print("Total images retrieved " + str(len(url_set))  )

        if current_page_index == max_page :
            print("Max pages retrieved")
            print("Total images retrieved " + str(len(url_set))  )
            extra_page_count = int(input("Enter the extra number of pages you want to scrap ( 0 if no more to scrap) : "))
            if extra_page_count == 0:
                break
            else:
                max_page = max_page + extra_page_count
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        driver.execute_script("scrollBy(0,-500);")


        sleep(1)

        page = driver.page_source
        bs = BeautifulSoup(page,'html.parser')
        images = bs.find_all('img', {'src':re.compile('.jpg')})
        for image in images:
            url_set.add(image['src'])
        current_page_index += 1

    page = driver.page_source
    bs = BeautifulSoup(page,'html.parser')
    images = bs.find_all('img', {'src':re.compile('.jpg')})
    for image in images:
        url_set.add(image['src'])

    driver.quit()
    return url_set

def get_items_from_alibaba(item_category):
    url_set = set()
    driver =    webdriver.Chrome()

    root_url = input('Search Query URL: ')
    

    print(root_url)
    driver.get(root_url)

    # current_page_index = 0
    page = driver.page_source
    bs = BeautifulSoup(page,'html.parser')
    images = bs.find_all('img', {'src':re.compile('.jpg')})
    for image in images:
        url_set.add(image['src'])

    # print(url_set)

    while True:     
        if current_page_index == max_page :
            print("Total images retrieved " + str(len(url_set))  )
            extra_page_count = int(input("Enter the extra number of pages you want to scrap ( 0 if no more to scrap) : "))
            if extra_page_count == 0:
                break
            else:
                max_page = max_page + extra_page_count
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);") 
        driver.execute_script("scrollBy(0,-500);")
        try:
            lm = driver.find_element_by_class_name("list-load-more")
            lm.click()
        except:
            break

        sleep(sleep_time)
        
        page = driver.page_source 
        bs = BeautifulSoup(page,'html.parser')   
        images = bs.find_all('img', {'src':re.compile('.jpg')})      
        for image in images:
            url_set.add(image['src'])
    
        current_page_index += 1

    driver.quit()
    return url_set


def scrapper(item_category,dest_dir,website):
    url_set = set()
    if website == "amazon" :
        url_set = get_items_from_amazon(item_category)
    elif website == "myntra":
        url_set = get_items_from_myntra(item_category)
    elif website == "ajio":
        url_set = get_items_from_ajio(item_category)
    elif website == "koovs":
        url_set = get_items_from_koovs(item_category)
    elif website == "fynd":
        url_set = get_items_from_fynd(item_category)
    elif website == "alibaba":
        url_set = get_items_from_alibaba()
    elif website == "all":
        url_set = []
        # url_set.extend(get_items_from_amazon(item_category))
        url_set.extend(get_items_from_myntra(item_category))
        url_set.extend(get_items_from_fynd(item_category))
        url_set.extend(get_items_from_ajio(item_category))
        url_set.extend(get_items_from_koovs(item_category))


    # download_items(url_set,dest_dir,item_category,website)
    print(str(len(url_set)) + "items downloaded" )
    print(item_category)

    urls =  list(url_set)
    categories = [item_category] * len(urls)

    try:
        df1 = pd.read_csv('data.csv')
    except:
        df1 = pd.DataFrame()

    df2 = pd.DataFrame({'url' : urls, 'category':categories})

    # concat both the dataframes
    df = pd.concat([df1, df2])

    print(len(df1))
    print(len(df2))
    print(len(df))
    df.to_csv('data.csv',index=False)

    return url_set