from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
# print(soup)

articles = [element for element in soup.select(selector=".titleline a") if not element.find(name="span")]

article_texts = [article.getText() for article in articles]
article_links = [article.get("href") for article in articles]
article_upvotes = [int(element.getText().split()[0]) for element in soup.findAll(class_="score")]

# print(article_texts)
# print(article_links)
# print(article_upvotes)

max_index = article_upvotes.index(max(article_upvotes))
print(article_texts[max_index])
