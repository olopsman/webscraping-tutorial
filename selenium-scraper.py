from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://quotes.toscrape.com/js/")
time.sleep(1)
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
quotes = soup.findAll("div",{"class":"quote"})

for quote in quotes:
    print(quote.find("span",{"class":"text"}).get_text())
driver.close()