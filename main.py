from enum import Enum
from screenshot import *
from PIL import Image, ImageDraw
import pyautogui
import time

bombTextures = []
boundsTextures = []
boundsLocations = []
boundsLocationsCenters = []

class BombColor(Enum):
    Black = 0
    Pink = 1

if __name__ == "__main__":
    properties.loadFile("./properties.txt")
    field = Image.open(f"./assets/field.png")

    for bombColor in BombColor:
        im = Image.open(f"./assets/bomb_{bombColor.name}.png")
        bombTextures.append(im)

        bound = Image.open(f"./assets/bounds_{bombColor.name}.png")
        boundsTextures.append(bound)

        loc = pyautogui.locate(bound, field, confidence=0.75)

        if loc is not None:
            boundsLocations.append(loc)
            boundsLocationsCenters.append(pyautogui.center(loc))

    closeApplication = False
    while not closeApplication:

        ss = getScreenshot(topScreen=False)
        drawing = ImageDraw.Draw(ss)
        for bound in boundsLocations:
            drawing.rectangle(((bound[0], bound[1]), (bound[0] + bound[2], bound[1] + bound[3],)), fill=(1, 1, 1))

        for bombColor in BombColor:
            bomb = pyautogui.locate(bombTextures[bombColor.value], ss, confidence=0.9)

            if bomb is not None:
                center = pyautogui.center(bomb)
                x = properties.bottomScreenBounds[0] + center.x
                y = properties.bottomScreenBounds[1] + center.y
                pyautogui.moveTo(x, y, _pause=False)
                pyautogui.mouseDown(_pause=False)
                time.sleep(0.04)
                pyautogui.moveTo(boundsLocationsCenters[bombColor.value].x + properties.bottomScreenBounds[0], boundsLocationsCenters[bombColor.value].y + properties.bottomScreenBounds[1], _pause=False)
                time.sleep(0.04)
                pyautogui.mouseUp(_pause=False)
                break