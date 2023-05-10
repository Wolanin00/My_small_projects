import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get(url="http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")

upgrade_every = 4
timeout_for_upgrade = time.time() + upgrade_every  # seconds
timeout_to_end = time.time() + 5 * 60  # seconds

while True:
    cookie.click()
    if time.time() > timeout_for_upgrade:
        try:
            el_possible_to_upgrade = driver.find_elements(By.XPATH,
                                                          '//*[@id="store"]/div[not(contains(@class,"grayed"))]')
            el_possible_to_upgrade[-1].click()
            timeout_for_upgrade = time.time() + upgrade_every
        except:
            pass
    if time.time() > timeout_to_end:
        cookie_per_sec = driver.find_element(By.ID, "cps")
        print(cookie_per_sec.text)
        break
