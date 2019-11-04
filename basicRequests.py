#HTTP Library
#pip3 install requests
import requests


#thingToSearch = {"#q" : "pizza"}
#r = requests.get("http://www.bing.co.uk/search", params = thingToSearch)


r = requests.get("http://www.google.co.uk")
print("Status:", r.status_code)

#print(r.url) prints the url

#grab the html of the website
print(r.text)

f = open("./page.html", "w+")
f.write(r.text)