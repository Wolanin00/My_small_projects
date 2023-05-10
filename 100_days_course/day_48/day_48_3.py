from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get(url="https://en.wikipedia.org/wiki/Main_Page")

number_of_articles = driver.find_element(By.XPATH, "//div[@id='articlecount']/a[@title='Special:Statistics']")
# number_of_articles.click()

search_box = driver.find_element(By.NAME, "search")
search_box.send_keys("Python")
search_box.send_keys(Keys.ENTER)
