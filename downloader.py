import requests, os,bs4
from functions import *

link = input("link:")

response = download(link) 

# print(response)
bs = bs4.BeautifulSoup(response,"html.parser")

with open("tempdata.html","w",encoding="utf-8") as f:
    f.write(response)
    f.close()

title = bs.find("title").contents[0]
GN = title.split(" - ")
GN.pop()
GN.pop()
GN = " - ".join(GN)
# GN = GN[0]+" - "+GN[1]
content = bs.find("div",{"id":"main_contents"})

# print(content)
# print(len(content))

links = []

items = content.find_all("div")[4]
for i in items:
    # i = i.find("a")
    try:
        pglink = "https://hentai-cosplays.com"+i.find("a").attrs["href"]
        if pglink not in links:
            links.append(pglink)
    except Exception as ee:pass

try:
    import natsort
    links = natsort.natsorted(links)
except:
    links.sort()

from pprint import pprint
pprint(links)


def download_gallery(link):
    print(link)
    dl = download(link)
    bs = bs4.BeautifulSoup(dl,"html.parser")
    imglink = bs.find("div",{"id":"display_image_detail"}).find("a").attrs["href"]
    DownloadIMG(imglink,GN)

# for l in links:
#     download_gallery(l)