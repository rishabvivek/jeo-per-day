from pickle import TRUE
import requests

from bs4 import BeautifulSoup


URL = "https://j-archive.com/"


page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

count = 0

extension = ""
for i in soup.find_all('td', {"class": "splash_clue_footer"}):

    if (count < 1) :
        extension = i.a['href']

    count += 1


newURL = "https://j-archive.com/" + extension

newPage = requests.get(newURL)

newSoup = BeautifulSoup(newPage.content, "html.parser")


for j in newSoup.find_all('td', {"class": "clue"}):
    print(j.div['onmouseout'])