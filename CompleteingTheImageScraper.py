from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO
import os



def startSearch():

  search = input("You want to search for: ")
  params = {"q": search}
  directoryName = search.replace(" ", "_").lower()

  if not os.path.isdir(directoryName):
    os.makedirs(directoryName)


  r = requests.get("http://www.bing.com/image/search", params = params)

  soup = BeautifulSoup(r.text, "html.parser")
  links = soup.findAll("a", {"class": "thumb"})
  NumberOfLinks = len(links)


  print(NumberOfLinks)

  for item in links:
    try:

      imageObject = requests.get(item.attrs["href"])
      print("Getting :", item.attrs["href"] )
      title = item.attrs["href"].split("/")[-1]
      try: 

        img = Image.open(BytesIO(imageObject.content))
        img.save("./"+ directoryName +"/" + title, img.format)
      except:
        print("Could not save image")
    except:
      print ("Could not request Image")


  startSearch()

startSearch()

