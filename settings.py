import sys, os, json


def resource_path():
    """Get absolute path to resource, works for dev and for PyInstaller"""
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path)


settingsfilename = resource_path() + "/data.json"
datas = {
    # "savePath": "Downloads/",
    "rewriteInfo" : True,
    "proxy":"",
    "core":"1"
}


def readSetting(datas=datas) -> dict:
    try:
        export = json.load(open(settingsfilename))
        datas = export
    except Exception as e:
        json.dump(datas, open(settingsfilename, "x"), indent=4)
    os.environ["userdata"]=json.dumps(datas)
    # return datas
    
    os.environ["HEAD"]=json.dumps({
        "Cookie":"cf_clearance=wTrusoyp5WAAT82G2qgHxXyAKcdDrQ7R5BQD0MWl2Uk-1720028226-1.0.1.1-fSijIqo8DTkMN9iDJbd1ilfy1urv9lD.pHwFIpsUUgn7qv83eiq9vPS3hFBKWLr8h90dg8RRGtsP1kr2xSB3MA",
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Encoding":"gzip, deflate, br, zstd",
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
    })

readSetting()


def editsettings(key, newValue):
    print(key,newValue)
    datas=json.loads(os.environ["userdata"])
    datas[key] = newValue
    json.dump(datas, open(settingsfilename, "w"), indent=4)
    readSetting()
