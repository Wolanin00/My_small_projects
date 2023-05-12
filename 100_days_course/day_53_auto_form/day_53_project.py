import re
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

form_link = "https://forms.gle/QwhB9yoZZhhyd7bv5"
zillow_url = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    "Accept-Language": "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7"
}

response = requests.get(url=zillow_url, headers=headers)
soup = BeautifulSoup(response.text, "lxml")

raw_all_links = soup.find_all('a', {'data-test': "property-card-link"})
all_links = [link.get('href') for link in raw_all_links]

raw_all_price = soup.find_all('span', {'data-test': "property-card-price"})
all_price = [re.split('/|\+', price.text)[0] for price in raw_all_price]

raw_all_address = soup.find_all('address', {'data-test': "property-card-addr"})
all_address = [address.text for address in raw_all_address]

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url=form_link)
time.sleep(3)

amount_of_property = min(len(all_address), len(all_price), len(all_links))

for i in range(amount_of_property):
    address_entry = driver.find_element(By.XPATH, "//div[@role='list']/div[1]//input")
    price_entry = driver.find_element(By.XPATH, "//div[@role='list']/div[2]//input")
    link_entry = driver.find_element(By.XPATH, "//div[@role='list']/div[3]//input")

    address_entry.send_keys(all_address[i])
    price_entry.send_keys(all_price[i])
    link_entry.send_keys(all_links[i])

    send_form = driver.find_element(By.XPATH, "//div[@role='list']/..//div[1]/div[@role='button']")
    send_form.click()
    time.sleep(1)
    send_next_form = driver.find_element(By.XPATH, "//div[@role='heading']/..//a")
    send_next_form.click()
    time.sleep(2)
