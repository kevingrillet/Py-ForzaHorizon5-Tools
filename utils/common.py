import time
from datetime import datetime

import pyautogui

from game import constant
from utils.constant import DebugLevel


def click_then_sleep(location: (int, int) = (0, 0), sleep: float = .5, scale: float = 1):
    """
    click at location then sleep
    :param location:
    :param sleep:
    :param scale:
    :return:
    """
    if scale != 1:
        location = (int(location[0] * scale), int(location[1] * scale))
    pyautogui.moveTo(location)
    pyautogui.mouseDown()
    time.sleep(sleep)
    pyautogui.mouseUp()
    pyautogui.moveTo(10, 10)


def alt_f4():
    """
    send alt + f4
    """
    pyautogui.keyDown("alt")
    time.sleep(.125)
    pyautogui.press("f4")
    pyautogui.keyUp("alt")


def alt_tab():
    """
    send alt tab
    """
    pyautogui.keyDown("alt")
    time.sleep(.125)
    pyautogui.press("tab")
    pyautogui.keyUp("alt")


def debug(msg: str = "", debug_level: int = DebugLevel.ALWAYS):
    """
    print debug if enough level
    :param msg:
    :param debug_level:
    :return:
    """
    if debug_level <= constant.DEBUG_LEVEL:
        print("[DEBUG] " + str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")) + " - " + msg)


def fps() -> float:
    """
    return fps
    """
    new_frame = time.time()
    timer = 1 / (new_frame - fps.frame)
    fps.frame = new_frame
    return timer


def press_then_sleep(key: str, sleep: float = .5):
    """
    press key then sleep
    :param key:
    :param sleep:
    :return:
    """
    pyautogui.press(key)
    # pydirectinput.press(key)
    time.sleep(sleep)


# https://stackoverflow.com/questions/279561/what-is-the-python-equivalent-of-static-variables-inside-a-function
fps.frame = time.time()
