from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
webpage = response.text

soup = BeautifulSoup(webpage,"html.parser")

# heading = soup.find_all(name="div",class_="jsx-3821216435 block-item listicle-container")

# print(heading)
main_div = soup.find(name="div",class_="jsx-3821216435 listicle-item")
tag = main_div.get("a")
print(tag)
print(main_div)
