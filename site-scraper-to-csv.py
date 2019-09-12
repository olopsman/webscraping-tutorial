from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

def crawl_url(pageUrl, writer):
    url = "http://books.toscrape.com/" + pageUrl
    html = urlopen(url)
    soup = BeautifulSoup(html, "html.parser")
    # grab each product
    books =  soup.findAll("article", {"class":"product_pod"})
    try:
        for book in books:
            title = book.h3.a.attrs['title']
            book_url = book.a.attrs['href']
            price = book.find("p",{"class":"price_color"}).get_text()
            availability = book.find("p",{"class":"instock availability"}).get_text().strip()
            writer.writerow((title, url + book_url, price, availability))
        try:
            new_url = soup.find("li",{"class":"next"})
            print("---" + new_url.a.attrs['href'])
            catalogue_str = "catalogue/"
            if catalogue_str in new_url.a.attrs['href']:
                crawl_url(new_url.a.attrs['href'], writer)
            else:
                crawl_url(catalogue_str + new_url.a.attrs['href'], writer)
        except AttributeError as e:
            print('Crawl Finished')
            return None
    finally:
        csvFile.close()


csvFile = open("books.csv", "w")
writer = csv.writer(csvFile)
writer.writerow(("Title", "URL","Price","Availability"))
crawl_url("", writer)
