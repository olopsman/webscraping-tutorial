from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
driver.get("http://quotes.toscrape.com/js/")
try:
    element = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((by.By.CLASS_NAME, "quote")))
finally:
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    quotes = soup.findAll("div",{"class":"quote"})

    for quote in quotes:
        print(quote.find("span",{"class":"text"}).get_text())
    driver.close()