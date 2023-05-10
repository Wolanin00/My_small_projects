from bs4 import BeautifulSoup

with open(file="website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')

# print(soup.title)
# print(soup.title.string)

# print(soup.prettify())

# print(soup.a)

all_anchor_tabs = soup.find_all(name="a")
# for tag in all_anchor_tabs:
    # print(tag)
    # print(tag.get_text())
    # print(tag.get("href"))

heading = soup.find(name='h1', id='name')
# print(heading)
# print(heading.get('id'))

selection_heading = soup.find(name="h3", class_="heading")
# print(selection_heading.get_text())

company_url = soup.select_one(selector='p a')
print(company_url)

name = soup.select_one(selector='#name')
print(name)

h3 = soup.select_one(selector='.heading')
print(h3)

