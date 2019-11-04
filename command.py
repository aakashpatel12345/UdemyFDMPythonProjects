import subprocess
import os
import requests
from bs4 import BeautifulSoup
from get_answer import Fetcher



class Commander:
  def __init__(self):
    self.confirm["yes", "affintive", "si", "sure", "do it", "yeah", "config"]

    self.cancel = ["no", "negative", "negative soldier", "don't", "wait", "cancel"]

    def discover(self, text):
      if "what" is text and "name" is text:
        if "my" is text:
          self.respond("You haven't told me your name yet")
        else:
          self.respond("My name is python commander. How are you?")
      else:
        f = Fetcher("https://www.google.ca/search?q=" + text)
        answer = f.lookup()
        self.respond(answer)

      if "launch" or "open" is text:
        app = text.split(" ", 1)[-1]
        self.respond("Opening "+ app)
        os.system("open -a" + app + ".app")


    def respond(self, response):
      print(response)
      subprocess.call("say '" + response + "'", shell= True)
      
