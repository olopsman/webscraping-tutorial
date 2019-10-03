from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

def crawl_url(pageUrl):
    main_url = "http://books.toscrape.com/"
    url = main_url + pageUrl
    html = urlopen(url)
    soup = BeautifulSoup(html, "html.parser")
    try:        
        try:    
            new_url = soup.find("li",{"class":"next"})
            print("--- " + new_url.a.attrs['href'])
            catalogue_str = "catalogue/"
            if catalogue_str in new_url.a.attrs['href']:
                htmlFile = open(new_url.a.attrs['href'], "w")
                crawl_url(new_url.a.attrs['href'])    
            else:
                htmlFile = open(catalogue_str + new_url.a.attrs['href'], "w")
                crawl_url(catalogue_str + new_url.a.attrs['href']) 
            htmlFile.write(str(soup))
            htmlFile.close()
        except AttributeError as e:
            print("Crawling finished")
            return None        
    finally:
        return None

crawl_url("")