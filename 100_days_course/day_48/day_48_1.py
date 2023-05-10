from selenium import webdriver
from selenium.webdriver.common.by import By

product_url = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

driver = webdriver.Chrome()
driver.get(url=product_url)

price_raw = driver.find_element(By.XPATH, '//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[1]')
price = price_raw.text.replace('\n', '.')[1:]
print(price)

a_text = driver.find_element(By.CLASS_NAME, "a-size-large.a-spacing-none")
print(a_text.get_attribute("outerHTML"))

driver.quit()
