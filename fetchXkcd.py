import xkcd
import os
import sys
import time
import logging
import urllib
logger = logging.getLogger()
logger.setLevel(1)
os.chdir(os.path.dirname(os.path.realpath(__file__)))
latest = xkcd.getLatestComicNum()
cached = os.listdir("./comics")

for i in range(1, latest+1):
    if f"{i}" in cached:
        continue
    if i == 404:
        continue
    try:
        logger.log(1,(xkcd.Comic(i).download("./comics", f"{i}")))
        time.sleep(0.1)
        logger.log(1,f"comic {i} downloaded")
    except urllib.error.HTTPError:
        logger.log(2, f"an error occured while downloading comic #{i}, skipping for now")
        continue
    