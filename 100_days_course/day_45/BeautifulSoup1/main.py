from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/news")

page_data = BeautifulSoup(response.text, 'html.parser')

all_article = page_data.select('tr.athing td.title a')
articles = [article for ind, article in enumerate(all_article) if ind % 2 == 0]

article_text = []
article_link = []

for article in articles:
    article_text.append(article.get_text())
    article_link.append(article.get('href'))

article_upvote = [score.get_text() for score in page_data.find_all(name='span', class_='score')]

print(article_text)
print(article_link)
print(article_upvote)
