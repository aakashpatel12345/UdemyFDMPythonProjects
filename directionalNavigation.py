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
    #print("Parent: ", item.find("a").parent)
    #print("Summary: ", item.find("a").parent.parent.find("a").text)
    #children = item.children
    #for child in children:
      #print ("Child :", child)

    #children = item.children[0]#only grab the first child - doesn't work

    children = item.find("h2")

    print("Next Sibling of the h2 :", children.next_sibling)
    #can do next sibling and previous sibling

