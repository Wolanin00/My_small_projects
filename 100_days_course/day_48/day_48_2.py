from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get(url="https://www.python.org/")

data = driver.find_elements(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li')
events = {key: {'time': value[0], 'name': value[1]} for key, value in [[data.index(item), item.text.split('\n')] for item in data]}
print(events)
