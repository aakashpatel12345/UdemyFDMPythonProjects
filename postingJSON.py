import requests
import simplejson as json


url = "https://googleblog.blogspot.com/2009/12/making-urls-shorter-for-google-toolbar.html"
payload = {"longUrl" :"http://example.com"}
headers = {"Content-Type": "application/json"}

r = requests.post(url, json=payload, headers=headers)

print(r.text)
#print(json.loads(r.text)["error"]["code"])