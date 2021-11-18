import time
from datetime import datetime

import pyautogui

from utils import constant


def click(location: (int, int) = (0, 0), sleep: float = .5):
    pyautogui.moveTo(location)
    pyautogui.mouseDown()
    time.sleep(sleep)
    pyautogui.mouseUp()
    pyautogui.moveTo(10, 10)


def debug(msg: str = "", debug_level: int = 0):
    """
        print debug if enough level
    """
    if debug_level >= constant.DEBUG_LEVEL:
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
    """
    pyautogui.press(key)
    # pydirectinput.press(key)
    time.sleep(sleep)


# https://stackoverflow.com/questions/279561/what-is-the-python-equivalent-of-static-variables-inside-a-function
fps.frame = time.time()
