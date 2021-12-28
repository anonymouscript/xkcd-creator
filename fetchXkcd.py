import xkcd
import os
import sys
import time
import log
import urllib
log.CurrentLevel = -1 #change on distribution to 0, or 1

os.chdir(os.path.dirname(os.path.realpath(__file__)))
try:
    latest = xkcd.getLatestComicNum()
    xkcd.getLatestComic()
    connection = True
except urllib.error.HTTPError:
    connection = False
except urllib.error.URLError:
    connection = False
cached = os.listdir("./comics")
if connection:
    for i in range(1, latest+1):
        if f"{i}" in cached:
            continue
        if i in [404,1608, 1663]:
            continue
        try:
            log.log(1,(xkcd.Comic(i).download("./comics", f"{i}")))
            time.sleep(0.1)
            log.log(0,f"comic {i} downloaded")
        except urllib.error.HTTPError:
            log.log(1, f"an error occured while downloading comic #{i}, skipping for now")
            continue
        