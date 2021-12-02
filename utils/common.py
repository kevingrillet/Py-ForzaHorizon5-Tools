import logging
import time
from datetime import datetime

import pyautogui

from game import constant
from utils.constant import DebugLevel
from utils.handlerwin32 import HandlerWin32


def alt_f4():
    """
    send alt + f4
    """
    keyDown('alt', .125)
    press('f4', 0)
    keyUp('alt')


def alt_tab():
    """
    send alt tab
    """
    keyDown('alt', .125)
    press('tab', 0)
    keyUp('alt')


def click(location: (int, int) = (0, 0), secs: float = .5, scale: float = 1):
    """
    click at location then sleep
    :param location:
    :param secs:
    :param scale:
    """
    if scale != 1:
        location = (int(location[0] * scale), int(location[1] * scale))
    moveTo(location)
    pyautogui.mouseDown()
    time.sleep(secs)
    pyautogui.mouseUp()
    moveTo((10, 10))


def convert_layout(inpt: str) -> str:
    """
    If keyboard is not in AZERTY, switch input to QWERTY
    :param inpt:
    :return:
    """
    if not ('France' or 'Belgium') in HandlerWin32.get_keyboard_language():
        inpt = inpt.translate(str.maketrans('z', 'w'))
    return inpt


def debug(msg: str = '', debug_level: int = DebugLevel.ALWAYS):
    """
    print debug if enough level
    :param msg:
    :param debug_level:
    """
    msg = '[DEBUG] ' + str(datetime.now().strftime('%d/%m/%Y %H:%M:%S')) + ' - ' + msg
    if debug_level <= constant.DEBUG_LEVEL:
        # print(msg)
        logging.debug(msg)


def fps() -> float:
    """
    :return: fps
    """
    new_frame = time.time()
    timer = 1 / (new_frame - fps.frame)
    fps.frame = new_frame
    return timer


def info(msg: str = ''):
    """
    print info
    :param msg:
    """
    msg = '[INFO ] ' + str(datetime.now().strftime('%d/%m/%Y %H:%M:%S')) + ' - ' + msg
    # print(msg)
    logging.info(msg)


def keyDown(key: str, secs: float = 0):
    """
    press key then sleep x secs
    :param key:
    :param secs:
    """
    pyautogui.keyDown(convert_layout(key))
    sleep(secs)


def keyUp(key: str):
    """
    release key
    :param key:
    """
    pyautogui.keyUp(convert_layout(key))


def moveTo(location: (int, int) = (0, 0), secs: float = 0, scale: float = 1):
    """
    move mouse to location then sleep
    :param location:
    :param secs:
    :param scale:
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
    pyautogui.press(convert_layout(key))
    sleep(secs)


def scroll(clicks: int = 1, location: (int, int) = (0, 0), secs: float = .5, scale=1):
    """
    Scroll at location then sleep x secs
    :param scale:
    :param clicks:
    :param location:
    :param secs:
    """
    if scale != 1:
        location = (int(location[0] * scale), int(location[1] * scale))
    moveTo(location)
    # for _ in range(abs(clicks)):
    #     pyautogui.scroll(1 if clicks > 0 else -1)
    #     sleep(.1)
    HandlerWin32.scroll(clicks, delay_between_ticks=.1)
    moveTo((10, 10), secs)


def sleep(secs: float = 0, msg: str = ''):
    """
    sleep for x secs
    :param msg:
    :param secs:
    """
    if msg:
        info(msg)
    time.sleep(secs)


def warn(msg: str = ''):
    """
    print warn
    :param msg:
    """
    msg = '[WARN ] ' + str(datetime.now().strftime('%d/%m/%Y %H:%M:%S')) + ' - ' + msg
    # print(msg)
    logging.warning(msg)


# https://stackoverflow.com/questions/279561/what-is-the-python-equivalent-of-static-variables-inside-a-function
fps.frame = time.time()
