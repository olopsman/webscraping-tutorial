from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
import mysql.connector

# Connect to the database
cnx = mysql.connector.connect(user='howto', password='howto@115',
                            host='localhost',
                            database='python_scraping')
cursor = cnx.cursor()                            
sql = "INSERT INTO `books` (`title`, `book_url`, `price`, `availability`) VALUES (%s, %s, %s, %s)"


def crawl_url(pageUrl, book_arr):
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
            #writer.writerow((title, url + book_url, price, availability))
            book_arr.append((title, url + book_url, price, availability))
        try:
            new_url = soup.find("li",{"class":"next"})
            print("---" + new_url.a.attrs['href'])
            catalogue_str = "catalogue/"
            if catalogue_str in new_url.a.attrs['href']:
                crawl_url(new_url.a.attrs['href'], book_arr)
            #else:
            #    crawl_url(catalogue_str + new_url.a.attrs['href'], book_arr)
        except AttributeError as e:
            print('Crawl Finished')
            return book_arr
    finally:
      return book_arr


#csvFile = open("books.csv", "w")
#writer = csv.writer(csvFile)
#writer.writerow(("Title", "URL","Price","Availability"))
book_arr = crawl_url("", [])
print(len(book_arr))
cursor.executemany(sql, book_arr)
cnx.commit()
cursor.close()
cnx.close()