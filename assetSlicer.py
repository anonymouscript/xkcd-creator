from PIL import Image
import urllib
import os
import re
import xkcd

import log
import fetchXkcd
from matplotlib import pyplot as plt
import numpy as np



SOFT_THRESHOLD = 5
HARD_THRESHOLD = 50

openedImages = []


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
            #colors = img.getcolors()
            pass
def getImage(imgNum):
    img = Image.open(f"./comics/{imgNum}")

    openedImages.append(img)
    return img

def showColors(imgNum):
    with Image.open(f"./comics/{imgNum}") as img:
        img.convert('L')
        
        x = list(range(256))
        y = img.histogram()

        plt.plot(x,y)
        plt.show()
        print(x,y)
        #colors = img.getcolors()
        #print(colors)
        img.show()
def seperate(imgNum):
    image = getImage(imgNum) #open by self later
    image = image.convert('1')
    image.show() 
def cleanUp():
    for img in openedImages:
        img.close()            
            
            

seperate(1212)

cleanUp()