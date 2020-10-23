from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as bs

print("Go to 'https://subslikescript.com/series/Attack_on_Titan-2560140' and select the episode to count")
myUrl = input()

client = ureq(myUrl)
pageHTML = client.read()
client.close()

page_soup = bs(pageHTML, "html.parser")
containers = page_soup.find("div", {"class":"full-script"})

containers = containers.text

count = containers.count("Titan")

print("In This episode, they say the word 'Titan' " +  (str)(count) + " times.")
