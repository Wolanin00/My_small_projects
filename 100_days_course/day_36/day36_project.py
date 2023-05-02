import requests
from datetime import datetime, timedelta
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

Stock_Endpoint = "https://www.alphavantage.co/query"
stock_api_key = "REMOVED"  # TO ADD
stock_parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": stock_api_key
}

News_Endpoint = "https://newsapi.org/v2/everything"
news_api_key = "REMOVED"  # TO ADD
news_parameters = {
    "q": COMPANY_NAME,
    "sortBy": "publishedAt",
    "apiKey": news_api_key
}

twilio_account_sid = "REMOVED"
twilio_auth_token = "REMOVED"
trial_number = "REMOVED"


# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock_response = requests.get(Stock_Endpoint, params=stock_parameters)
stock_response.raise_for_status()
stock_data = stock_response.json()

yesterday = datetime.today() - timedelta(days=1)
if yesterday.weekday() == 0:
    day_before_yesterday = datetime.today() - timedelta(days=4)
else:
    day_before_yesterday = datetime.today() - timedelta(days=2)

yesterday_format = str(yesterday).split(' ')[0]
day_before_yesterday_format = str(day_before_yesterday).split(' ')[0]
yesterday_stock_data = stock_data['Time Series (Daily)'][yesterday_format]
day_before_yesterday_stock_data = stock_data['Time Series (Daily)'][day_before_yesterday_format]
yesterday_close_data = float(yesterday_stock_data["4. close"])
day_before_yesterday_close_data = float(day_before_yesterday_stock_data["4. close"])

difference = yesterday_close_data - day_before_yesterday_close_data
up_down = None
if difference > 0:
    up_down = "⬆️"
else:
    up_down = "⬇️"

diff_percentage = round((difference / yesterday_close_data) * 100)
print(diff_percentage)

# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

if abs(diff_percentage) > 1:
    print("Get News")
    news_response = requests.get(News_Endpoint, params=news_parameters)
    news_response.raise_for_status()
    three_news_data = news_response.json()['articles'][:3]
    print(three_news_data)

# STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.

    formatted_article = [f"{STOCK}: {up_down}{abs(diff_percentage)}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_news_data]
    client = Client(twilio_account_sid, twilio_auth_token)
    for article in formatted_article:
        message = client.messages.create(
            body=article,
            from_=trial_number,
            to='YOUR NUMBER'  # TO ADD
        )
        print(message.status)
