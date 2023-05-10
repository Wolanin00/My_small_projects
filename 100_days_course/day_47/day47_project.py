from notification_manager import NotificationManager
from bs4 import BeautifulSoup
import requests
import lxml

'''
https://myhttpheader.com/
'''

product_url = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
target_price = 100
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    "Accept-Language": "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7"
}

response = requests.get(url=product_url, headers=headers)
soup = BeautifulSoup(response.text, "lxml")

product_title = soup.find(name="span", id="productTitle").text.strip()
product_price = float(soup.find(name="span", class_="a-offscreen").text[1:])
print(product_price)

if product_price < target_price:
    notification_manager = NotificationManager()
    notification_manager.send_email_message(price=product_price, url=product_url, title=product_title)
