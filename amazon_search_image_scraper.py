import requests
from bs4 import *

link = input('Search Query URL: ')
req = requests.get(link)
soup = BeautifulSoup(req.text, 'lxml')

pagination = soup.find_all('span', {'class': 'pagnDisabled'})

last_pagination = int(pagination[0].get_text()) + 1

urls = []

for x in range (1, last_pagination):
    urls.append(link + '&page=' + str(x))

k = 1 
pag = 1
for x in urls:
    print('Pagination : ' + str(pag))
    req = requests.get(x)
    soup = BeautifulSoup(req.text, 'lxml')
    imgs = soup.find_all('img')
   
    for i in imgs:
        if str(i).find('src') != -1:
            url = i['src']
            name_image_folder = 'images/' + str(k) + '.jpg'
            image = requests.get(url).content
            
            with open(name_image_folder, 'wb') as handler:
                handler.write(image)
        k += 1
    pag += 1