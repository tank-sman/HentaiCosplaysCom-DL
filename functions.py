from bs4 import BeautifulSoup
from time import sleep,ctime
from os import get_terminal_size
from settings import readSetting
import requests, json, os, re

invalid_chars = ["\\","/",":","*","?",'"',"<",">","|"]

imglimit=0

def replaceName(text):
    export = ""
    for i in text :
        if i in invalid_chars:
            export+="-"
        else:
            export+=i
    return export

datas = dict(json.load(open("./data.json")))
os.environ["proxy"] = json.dumps({"https": datas["proxy"]})

head = {
        "Cookie":"cf_clearance=wTrusoyp5WAAT82G2qgHxXyAKcdDrQ7R5BQD0MWl2Uk-1720028226-1.0.1.1-fSijIqo8DTkMN9iDJbd1ilfy1urv9lD.pHwFIpsUUgn7qv83eiq9vPS3hFBKWLr8h90dg8RRGtsP1kr2xSB3MA",
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Encoding":"gzip",
        "Accept-Language":"en-US,en;q=0.5",
        "Cache-Control":"no-cache",
        "Connection":"keep-alive",
        "DNT":"1",
        "Pragma":"no-cache",
        "Priority":"u=1",
        "Referer":"https://hentai-cosplays.com/",
        "Sec-Fetch-Dest":"document",
        "Sec-Fetch-Mode":"navigate",
        "Sec-Fetch-Site":"same-site",
        "Sec-Fetch-User":"?1",
        "TE":"trailers",
        "Upgrade-Insecure-Requests":"1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127"
    }

def download(link: str):
    req = requests.get(link, headers=head, proxies= {"https": datas["proxy"],"http":datas["proxy"]})
    return req.text

# def send_download_request(link, filename):
#     response = requests.get(link, stream=True, headers=head)
#     response.raise_for_status()  # Raise error if download fails
#     with open(filename, "wb") as f:
#         for chunk in response.iter_content(1024):
#             f.write(chunk)


def DownloadIMG(link,GN):
    HEAD = json.loads(os.environ["HEAD"])
    filename = link.split("/")[-1]
    try:
        os.mkdir(GN)
    except:
        pass
    if filename in os.listdir(GN):
        print(filename)
        return
    downloadAnimation=["―","\\","|","/"]
    chunkSize=128
    TX = os.get_terminal_size().columns
    text_style="$n - $p [$f] $a"
    response = requests.get(link, stream=True,headers=HEAD)
# print(response.headers)
    response_size = int(response.headers["Content-Length"])
    response.raise_for_status()  # Raise error if download fails
    print()
    with open(GN+"/"+filename, "wb") as f:
        m=0
        for chunk in response.iter_content(chunkSize):
        #write data
            f.write(chunk)
        #jiguli miguli  
            m=m+1
        #############
            percent = m*chunkSize/response_size*100
            partsize = percent*(TX-len(text_style)-3)/100
        ######################
        ##############
            percentData = str(int(percent)).zfill(2)+"%"
            filler = int(partsize)*"="+f"{'>' if int(percent)!=100 else ''}"+int(TX-len(text_style)-4-partsize)*" "
            Animation = f"{downloadAnimation[m%len(downloadAnimation)]}"
        ################
            text = text_style.replace("$p",percentData).replace("$f",filler).replace("$a",Animation).replace("$n",filename)
            print(text,end="\r")
        print()
        return
    
def complete_list(link, pages):
    page_numbers = set()
    for url in pages:
        match = re.search(r"p=(\d+)", url)
        if match:
            page_numbers.add(int(match.group(1)))

    complete_urls = [link]
    for page_number in range(1, max(page_numbers) + 1):
        complete_urls.append(f"{link}?p={page_number}")

    return complete_urls


if __name__ == "__main__":
    # print(checkIMGlimit())
    pass