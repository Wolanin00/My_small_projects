import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

email = "szewczykmateusz64@gmail.com"
password = "REMOVED"
python_dev_url = "https://www.linkedin.com/jobs/search/?currentJobId=3603932760&f_AL=true&f_E=2&f_TPR=r86400&geoId=103263110&keywords=software%20engineer&location=Krak%C3%B3w%2C%20Woj.%20Ma%C5%82opolskie%2C%20Polska&refresh=true&sortBy=R"

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url=python_dev_url)

sign_in_button = driver.find_element(By.CLASS_NAME, "nav__button-secondary.btn-md.btn-secondary-emphasis")
sign_in_button.click()
time.sleep(3)

# Sign in page
sign_in_page_email_entry = driver.find_element(By.ID, "username")
sign_in_page_email_entry.send_keys(email)
sign_in_page_password_entry = driver.find_element(By.ID, "password")
sign_in_page_password_entry.send_keys(password)
sign_in_page_sign_in_button = driver.find_element(By.CLASS_NAME, "btn__primary--large.from__button--floating")
sign_in_page_sign_in_button.click()
time.sleep(3)

all_listings = driver.find_elements(By.CLASS_NAME, "job-card-container--clickable")
for listening in all_listings:
    listening.click()
    time.sleep(1)

    # Find Job page
    try:
        easy_apply_button = driver.find_element(By.CLASS_NAME, "jobs-apply-button artdeco-button artdeco-button--3 artdeco-button--primary ember-view".replace(' ', '.'))
        easy_apply_button.click()
        time.sleep(2)

        # Apply job modal
        for _ in range(3):
            try:
                sent_application_button = driver.find_element(By.CLASS_NAME, "artdeco-button artdeco-button--2 artdeco-button--primary ember-view".replace(' ', '.'))
                sent_application_button.click()
                time.sleep(1)
            except NoSuchElementException:
                pass
        time.sleep(3)

        cancel_button = driver.find_element(By.XPATH, "//button[@class='artdeco-modal__dismiss artdeco-button artdeco-button--circle artdeco-button--muted artdeco-button--2 artdeco-button--tertiary ember-view']/li-icon[@type='cancel-icon']")
        cancel_button.click()
        time.sleep(2)

        try:
            delete_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn artdeco-button artdeco-button--2 artdeco-button--secondary ember-view".replace(' ', '.'))
            delete_button.click()
        except NoSuchElementException:
            pass

    except NoSuchElementException:
        continue
