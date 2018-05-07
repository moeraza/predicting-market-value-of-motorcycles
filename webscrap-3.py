import bs4
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import pandas

l = [] #create empty list

for page in range(0,15,1):
    my_url = 'https://www.kijiji.ca/b-sport-bikes/ontario/page-' + str(page) + '/c304l9004?ad=offering&for-sale-by=ownr'
    #opening up connection and grabbing the page
    uClient = urlopen(my_url)
    #stores html data in variable
    page_html = uClient.read()
    uClient.close()
    #call soup function to parse page_html, store it in a vairable
    page_soup = BeautifulSoup(page_html, "html.parser")
    #grabs each product
    containers = page_soup.findAll("div", {"class":"info-container"})

    for container in containers:
        d = {} # create empty dictionary

        title = container.findAll("div", {"class":"title"})
        d["title"] = title[0].text.strip()

        kms = container.findAll("div", {"class":"details"})
        d["kilometers"] = kms[0].text.strip()

        price = container.findAll("div", {"class":"price"})
        d["price"] = price[0].text.replace("\n","").replace(" ","").replace("$","").replace(",","")

        description = container.findAll("div", {"class":"description"})
        d["description"] = description[0].text.strip()

        l.append(d)

df = pandas.DataFrame(l)
df
df.to_csv("motorcycles.csv")
