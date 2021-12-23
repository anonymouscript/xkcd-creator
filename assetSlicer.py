from PIL import Image
import urllib
import os
import re
import xkcd

import logging
connection = False  

SOFT_THRESHOLD = 5
HARD_THRESHOLD = 50
try:
    latest = xkcd.getLatestComicNum()
    connection = True
except urllib.error.URLError as e:
    logging.log(logging.ERROR, "Connection Failed, skipping import")
    currentLevel = logging.CurrentLevel
    logging.CurrentLevel = logging.ERROR
    import fetchXkcd
    logging.CurrentLevel = currentLevel

if connection:
    import fetchXkcd



def verifyXkcd():
    cached = os.listdir("./comics")
    comics = []
    for entry in cached:
        if re.fullmatch("[0-9]*",entry) != None:
            comics.append(entry)
    for comic in comics:
        with Image.open(f"./comics/{comic}") as img:
            #todo: append metadata to the Image
            #identify if an image is to grayscale to work or try extraction
            colors = img.getcolors()
            
            
            
