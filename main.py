from bs4 import BeautifulSoup

with open("website.html") as file:
    data=file.read()

soup = BeautifulSoup()