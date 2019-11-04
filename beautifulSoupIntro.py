#install pip3 install bs4
#web scraping is getting data from the internet

from bs4 import BeautifulSoup
import requests


search = input("Enter search terms: ")
params = {"q" : search}

r = requests.get("https://www.bing.com/search", params = params)

soup = BeautifulSoup(r.text, "html.parser")

print(soup.prettify())