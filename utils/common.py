import time
from datetime import datetime

from utils import constant


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


# https://stackoverflow.com/questions/279561/what-is-the-python-equivalent-of-static-variables-inside-a-function
fps.frame = time.time()
