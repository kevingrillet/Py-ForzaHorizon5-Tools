import time
from datetime import datetime

import pyautogui

from game import constant
from utils.constant import DebugLevel, Lang


def alt_f4():
    """
    send alt + f4
    """
    keyDown("alt", .125)
    press("f4", 0)
    keyUp("alt")


def alt_tab():
    """
    send alt tab
    """
    keyDown("alt", .125)
    press("tab", 0)
    keyUp("alt")


def click(location: (int, int) = (0, 0), secs: float = .5, scale: float = 1):
    """
    click at location then sleep
    :param location:
    :param secs:
    :param scale:
    :return:
    """
    if scale != 1:
        location = (int(location[0] * scale), int(location[1] * scale))
    moveTo(location)
    pyautogui.mouseDown()
    time.sleep(secs)
    pyautogui.mouseUp()
    moveTo((10, 10))


def debug(msg: str = "", debug_level: int = DebugLevel.ALWAYS):
    """
    print debug if enough level
    :param msg:
    :param debug_level:
    """
    if debug_level <= constant.DEBUG_LEVEL:
        print("[DEBUG] " + str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")) + " - " + msg)


def fps() -> float:
    """
    :return: fps
    """
    new_frame = time.time()
    timer = 1 / (new_frame - fps.frame)
    fps.frame = new_frame
    return timer


def keyDown(key: str, secs: float = 0):
    """
    press key then sleep x secs
    :param key:
    :param secs:
    """
    pyautogui.keyDown(key)
    sleep(secs)


def keyUp(key: str):
    """
    release key
    :param key:
    """
    pyautogui.keyUp(key)


def moveTo(location: (int, int) = (0, 0), secs: float = .5, scale: float = 1):
    """
    move mouse to location then sleep
    :param location:
    :param secs:
    :param scale:
    :return:
    """
    if scale != 1:
        location = (int(location[0] * scale), int(location[1] * scale))
    pyautogui.moveTo(location)
    sleep(secs)


def press(key: str, secs: float = .5):
    """
    press key then sleep x secs
    :param key:
    :param secs:
    """
    pyautogui.press(key)
    sleep(secs)


def sleep(secs: float = 0):
    """
    sleep for x secs
    :param secs:
    """
    time.sleep(secs)


def warn(msg: str = ""):
    """
    print warn
    :param msg:
    """
    print("[WARN ] " + str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")) + " - " + msg)


# https://stackoverflow.com/questions/279561/what-is-the-python-equivalent-of-static-variables-inside-a-function
fps.frame = time.time()
