import requests
from io import BytesIO
from PIL import Image


r = requests.get("http://ichef.bbci.co.uk/news/976/cpsprodpb/8029/production/_86290823_xi_selfie.jpg")

print ("Status Code : ", r.status_code)

image = Image.open(BytesIO(r.content))



print(image.size, image.format, image.mode)

path = "./image." + image.format

try:
  image.save(path, image.format)
except IOError:
  print("Could not save image")