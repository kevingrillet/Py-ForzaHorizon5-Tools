# Constant file to be clean
from enum import auto

from utils.superintenum import SuperIntEnum

DEBUG_LEVEL = 0
WINDOW_NAME = "Forza Horizon 5"


class AutoSpinAlreadyOwnedChoice(SuperIntEnum):
    ADD_TO_GARAGE = auto()
    SELL = auto()


class AutoSpinStep(SuperIntEnum):
    INIT = auto()
    WAITING = auto()
    SPINNING = auto()
    REWARD = auto()
    END = auto()
