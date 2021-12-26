import xkcd
import os
import sys
import time
import logging
import urllib
logging.CurrentLevel = -1 #change on distribution to 0, or 1

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
        if i == 404:
            continue
        try:
            logging.log(1,(xkcd.Comic(i).download("./comics", f"{i}")))
            time.sleep(0.1)
            logging.log(0,f"comic {i} downloaded")
        except urllib.error.HTTPError:
            logging.log(1, f"an error occured while downloading comic #{i}, skipping for now")
            continue
        