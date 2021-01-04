from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/")

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

articles = soup.findAll(name="a", class_="storylink")
upvotes = soup.findAll(name="span", class_="score")

article_list = []

for tag in range(len(articles) - 1):
    article_title = articles[tag].getText()
    article_link = articles[tag].get("href")
    article_upvotes = int(upvotes[tag].getText().strip(" points"))

    article_list.append((article_title, article_link, article_upvotes))

highest_rated = ""
most_votes = 0
go_to = ""

for item in article_list:
    if item[2] > most_votes:
        most_votes = item[2]
        highest_rated = item[0]
        go_to = item[1]


print(f"{highest_rated}\nVotes: {most_votes}\nView it here: {go_to}")


article_list.sort(key=lambda tup: tup[2], reverse=True)

