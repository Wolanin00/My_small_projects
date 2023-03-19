import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path='C:\ChromeDriver\chromedriver.exe')
driver.maximize_window()
driver.get('http://particle-clicker.web.cern.ch/')
time.sleep(2)
where_clik = driver.find_element(By.XPATH, "//canvas[contains(@id,'detector-events')]")
while True:
    if driver.find_element(By.XPATH, "//body").send_keys(Keys.TAB):
        break
    else:
        where_clik.click()

