import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from bs4 import BeautifulSoup
from urllib.parse import urlparse
import sys


class Fetcher:
  def __init__(self,url):
    self.driver = webdriver.PhantomJS()
    self.driver.wait = WebDriver(waitdriver, 5)
    self.url = url
    print(self.url)
   # self.lookup()


  def lookup(self):
    self.driver.get(self.url)
    try:
      ip = self.driver.wait.until(EC.presence_of_element_located(
        (By.CLASS_NAME, "gsfi")
      ))
      except:
        print ("Failed bruh")
    soup = BeautifulSoup(self.driver.page_source, "html.parser")
    answer = soup.find_all(class_="_sPg")
    #print (answer.get_text())

    with open("text.html", "w+") as f:
      f.write(str(soup))
      f.close()

    if not answer:
      answer=soup.find_all(class_="_m3b")

    if not answer:
      print("I don't know the answer!")

    self.driver.quit()
    return answer[0].get_text()
    #self.driver.quit()

      

    #google top sugestion box has class gffi
    #class of _fbg


