from bs4 import BeautifulSoup
import requests

search = input("What do you want to search for: ")
#search = search.replace(" ", "")

params = {"q": search.strip()}

r = requests.get("https://www.bing.com/search", params = params)

#r = requests.get("https://www.google.com/search", params = params)

soup = BeautifulSoup(r.text, "html.parser")

results = soup.find("ol", {"id": "b_results"})

links = results.findAll("li", {"class": "b_algo"})

for item in links:
  item_text = item.find("a").text
  item_href = item.find("a").attrs["href"]

  if item_text and item_href:
    print("\n")
    print(item_text)
    print(item_href)
    