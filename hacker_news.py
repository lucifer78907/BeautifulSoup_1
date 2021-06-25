from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page,"html.parser")

stories_list = soup.find_all(name="a",class_="storylink")
article_texts=[]
article_links=[]
for article_tag in stories_list:
    text = article_tag.getText()
    link = article_tag.get("href")
    article_texts.append(text)
    article_links.append(link)

stories_upvote_list = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

max_ele = max(stories_upvote_list)
index_ele = stories_upvote_list.index(max_ele)
index_ele += 1
print(f"Story is :{article_texts[index_ele]}")
print(f"Link is : {article_links[index_ele]}")
print(f"Upvotes are {max_ele}")


