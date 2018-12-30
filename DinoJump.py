from PIL import ImageGrab, ImageOps
import pyautogui
import time
from numpy import *

class coordinates:
    replaybtn = (480,290)
    dino = (188,302)

def RestartGame():
    pyautogui.click(coordinates.replaybtn)

def spacekey():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    pyautogui.keyUp('space')

def controlvol() :
    box = (coordinates.dino[0] + 100, coordinates.dino[1] , coordinates.dino[0] + 130 , coordinates.dino[1] + 40)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    totsum = a.sum()
    return (totsum)

def detectReset():
    box = (460, 280, 500, 315)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    return (a.sum())

def main():
    stat = True
    RestartGame()
    while stat:
        if controlvol() > 2500:
            spacekey()
            time.sleep(0.1)
        if detectReset() >= 10000:
            RestartGame()
            time.sleep(0.1)
            #stat = False

main()
