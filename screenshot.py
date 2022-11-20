import pyautogui
from load_properties import properties
from PIL import Image

def getScreenshot(topScreen=True):
    return pyautogui.screenshot(region=tuple(properties.topScreenBounds if topScreen else properties.bottomScreenBounds))