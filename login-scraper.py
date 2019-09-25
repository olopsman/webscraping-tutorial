from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver

options  = webdriver.ChromeOptions()
options.add_argument("headless")
driver = webdriver.Chrome(options=options)
driver.get("http://quotes.toscrape.com/js/")

login_element = driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/p/a")
login_element.click()

username = driver.find_element_by_xpath('//*[@id="username"]')
username.send_keys("myusername")

password = driver.find_element_by_xpath('//*[@id="password"]')
password.send_keys("mypassword")

submit = driver.find_element_by_xpath('//*[@type="submit"]')
submit.click()

driver.save_screenshot("screenshot.png")

driver.close()