import requests


myData =  {"field-keywords": "Earphones"}
r = requests.post("http://www.amazon.co.uk", data=myData)

f = open("myFile.html", "w+")
f.write(r.text)