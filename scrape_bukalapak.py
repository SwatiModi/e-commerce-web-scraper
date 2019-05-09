
from bs4 import BeautifulSoup
import requests


def scrape():
    l = []
    for page in range(0, 3):
        page = page + 1
        base_url = 'https://www.bukalapak.com/promo/serba-serbu-produk-terlaris-bukalapak?from=old-popular-section-3&page=' + str(page)
        # print(base_url)

        r = requests.get(base_url)
        soup = BeautifulSoup(r.text, "html.parser")

        all_product = soup.find_all('div', class_="product-card")
        # print(len(all_product))

        for item in all_product:
            d = { }

            # image
            product_image = item.find("img", {"class":"product-media__img"})
            # image = image.text.replace('\n', "").strip()
            product_image = product_image['src']
            d['product_image'] = product_image

            # name & link
            product_name = item.find("a", {"class":"product__name"})
            product_link = 'https://www.bukalapak.com' + str(product_name.get('href'))
            product_name = product_name.text.replace('\n', "").strip()
            d['product_link'] = product_link
            d['product_name'] = product_name

            # price
            product_price = item.find("span", {"class":"amount"})
            product_price = product_price.text.replace('\n', "").strip()
            d['product_price'] = 'Rp' + product_price

            # review
            product_review = item.find("a", {"class":"review__aggregate"})
            try:
                product_review = product_review.text
                d['product_review'] = int(product_review)
            except:
                d['product_review'] = 0

            # link
            # product_link = item.find("a", {"class":"product-media__link"}, href=True)
            # product_link = 'https://www.bukalapak.com' + str(product_link.get('href'))
            # d['product_link'] = product_link

            l.append(d)

    return l


if __name__ == "__main__":
    print(scrape())