import time
from selenium import webdriver
from selenium.webdriver.common.by import By

ACCOUNT_NAME = "REMOVED"
EMAIL = "szewczykmateusz64@gmail.com"
PASSWORD = "REMOVED"
PROMISED_DOWNLOAD = 100
PROMISED_UPLOAD = 25


class InternetSpeedTestBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.download = 0
        self.upload = 0

    def get_internet_speed(self):
        self.driver.get(url="https://www.speedtest.net/")
        accept_privacy = self.driver.find_element(By.ID, "onetrust-accept-btn-handler")
        accept_privacy.click()
        start_test = self.driver.find_element(By.CLASS_NAME, "start-text")
        start_test.click()
        time.sleep(60)
        self.download = self.driver.find_element(By.CLASS_NAME, "result-data-large number result-data-value download-speed".replace(' ', '.')).text
        self.upload = self.driver.find_element(By.CLASS_NAME, "result-data-large number result-data-value upload-speed".replace(' ', '.')).text

    def tweet_at_provider(self):
        self.driver.get(url="https://twitter.com/login/")
        time.sleep(3)
        email_entry = self.driver.find_element(By.XPATH, "//input")
        email_entry.send_keys(EMAIL)
        next_button = self.driver.find_element(By.XPATH, "//span[text()='Dalej']")  # PL XPATH
        next_button.click()
        time.sleep(1)
        account_name_entry = self.driver.find_element(By.XPATH, "//input[contains(@data-testid,'ocfEnterTextTextInput')]")
        account_name_entry.send_keys(ACCOUNT_NAME)
        next_button = self.driver.find_element(By.XPATH, "//span[text()='Dalej']")  # PL XPATH
        next_button.click()
        time.sleep(1)
        password_entry = self.driver.find_element(By.NAME, "password")
        password_entry.send_keys(PASSWORD)
        sign_in_button = self.driver.find_element(By.XPATH, "//span[text()='Zaloguj się']")  # PL XPATH
        sign_in_button.click()
        time.sleep(5)
        make_tweet_button = self.driver.find_element(By.XPATH, "//*[contains(@data-testid,'SideNav_NewTweet_Button')]")
        make_tweet_button.click()
        time.sleep(1)
        tweet_area = self.driver.find_element(By.XPATH, "//div[@id='layers']//div[contains(@class,'public-DraftStyleDefault-block public-DraftStyleDefault-ltr')]/span")
        message = f"Hey Internet Provider, why is my internet speed {self.download} down/{self.upload} up " \
                  f"when I pay for {PROMISED_DOWNLOAD} down/{PROMISED_UPLOAD} up?"
        tweet_area.send_keys(message)
        tweet_button = self.driver.find_element(By.XPATH, "//*[contains(@data-testid,'tweetButton')]")
        tweet_button.click()
        time.sleep(5)


bot = InternetSpeedTestBot()
bot.get_internet_speed()
bot.tweet_at_provider()
