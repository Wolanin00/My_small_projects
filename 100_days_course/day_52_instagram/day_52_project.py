import time
from selenium import webdriver
from selenium.webdriver.common.by import By

email = "REMOVED"
password = "REMOVED"
instagram_url = "https://www.instagram.com/"
instagram_profile = "girls"


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def sign_in(self):
        self.driver.get(url=f"{instagram_url}accounts/login/")
        time.sleep(3)

        accept_cookie = self.driver.find_element(By.XPATH, "//button[contains(text(),'cookie')][1]")
        accept_cookie.click()
        time.sleep(3)

        email_entry = self.driver.find_element(By.XPATH, "//input[contains(@name,'username')]")
        email_entry.send_keys(email)
        password_entry = self.driver.find_element(By.XPATH, "//input[contains(@name,'password')]")
        password_entry.send_keys(password)
        sign_in_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        sign_in_button.click()
        time.sleep(4)
        not_enable_notifications = self.driver.find_element(By.XPATH, "//div[@role='dialog']//div/button[2]")
        not_enable_notifications.click()
        time.sleep(2)

    def open_first_page(self):
        time.sleep(5)
        self.driver.get(url=f"{instagram_url}{instagram_profile}")

    def follow(self):
        time.sleep(5)
        followers_button = self.driver.find_element(By.XPATH, '//div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]')
        followers_button.click()
        time.sleep(2)
        all_followers_to_follow = self.driver.find_elements(By.XPATH, "//div[@role='dialog']//div[contains(@style,'position')]/div//button[contains(@class,'acas')]")
        for users in all_followers_to_follow:
            users.click()
        time.sleep(3)
        new_account_to_follow = self.driver.find_element(By.XPATH, "//div[@role='dialog']//div[contains(@style,'position')]/div[1]//span//a")
        new_account_to_follow.click()
        time.sleep(3)
        self.follow()


bot = InstaFollower()
bot.sign_in()
bot.open_first_page()
bot.follow()
