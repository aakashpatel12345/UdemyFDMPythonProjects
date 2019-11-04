from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO

search = input("You want to search for: ")
params = {"q": search}
r = requests.get("http://www.bing.com/image/search", params = params)

soup = BeautifulSoup(r.text, "html.parser")
links = soup.findAll("a", {"class": "thumb"})

for item in links:
  
  imageObject = requests.get(item.attrs["href"])
  print("Getting :", item.attrs["href"] )
  title = item.attrs["href"].split("/")[-1]
  img = Image.open(BytesIO(imageObject.content))
  img.save("./scrapedImages/" + title, img.format)