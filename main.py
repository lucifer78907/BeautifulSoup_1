from bs4 import BeautifulSoup

with open("website.html") as file:
    data=file.read()

soup = BeautifulSoup(data,"html.parser")
all_anchor_tags=soup.find_all(name="a")
for tags in all_anchor_tags:
    # print(tags.getText())
    print(tags.get("href"))

heading= soup.find(name="h1",id="name")
print(heading)

section_head=soup.find(name="h3",class_="heading")
print(section_head.get("class"))

company_url=soup.select_one(selector="p a") # or use (#) as id selector like #name (its an id)
print(company_url)

heading=soup.select(".heading")
print(heading)