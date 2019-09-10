from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

url = "http://books.toscrape.com/"
html = urlopen(url)
soup = BeautifulSoup(html, "html.parser")
# grab each product
books =  soup.findAll("article", {"class":"product_pod"})
csvFile = open("books.csv", "w")
try:
    writer = csv.writer(csvFile)
    writer.writerow(("Title", "URL","Price","Availability"))
    for book in books:
        title = book.h3.a.attrs['title']
        book_url = book.a.attrs['href']
        price = book.find("p",{"class":"price_color"}).get_text()
        availability = book.find("p",{"class":"instock availability"}).get_text().strip()
        writer.writerow((title, url + book_url, price, availability))
finally:
    csvFile.close()
