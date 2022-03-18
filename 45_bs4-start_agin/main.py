from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_we_page = response.text

soup = BeautifulSoup(yc_we_page, 'html.parser')
all_a = soup.find_all(name="a", class_="titlelink")
print(all_a)

article_titles = []
article_links = []
article_upvotes = []

for item in all_a:
    # all the texts in anchor tags
    article_titles.append(item.getText())
    #all the article links
    article_links.append(item.get("href"))

    #all the upvotes
all_upvotes = soup.find_all(class_="score")
for item in all_upvotes:
    string = item.getText()
    num = int(string.split(" ")[0])
    article_upvotes.append(num)

print(article_titles)
print(article_links)
print(article_upvotes)

largest_num = max(article_upvotes)
i = article_upvotes.index(largest_num)
print(article_titles[i])
print(article_links[i])
print(article_upvotes[i])