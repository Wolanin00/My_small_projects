from selenium import webdriver
from selenium.webdriver.common.by import By

op = webdriver.ChromeOptions()
op.add_argument('headless')
driver = webdriver.Chrome(options=op)
driver.get("https://www.afi.com/afis-100-years-100-movies/")

elements = driver.find_elements(By.XPATH, "//label[@class='container']/h6[contains(@class,'q_title')]")
films = [element.text for element in elements]
print(films)

with open("films.txt", 'w') as file:
    for film in films:
        file.write(f"{film}\n")
