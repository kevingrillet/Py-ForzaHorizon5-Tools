# Constant file to be clean
from enum import auto

from utils.constant import DebugLevel, Lang
from utils.superintenum import SuperIntEnum

DEBUG_LEVEL = DebugLevel.ALWAYS
DEV_MODE = False
LANG = Lang.FRENCH
SCALE = 1
WINDOW_NAME = "Forza Horizon 5"


class AutoLabReplayStep(SuperIntEnum):
    INIT = auto()
    PREPARING = auto()
    RACING = auto()
    REWARDS = auto()
    CHECK = auto()
    RESTART = auto()


class AutoSpinAlreadyOwnedChoice(SuperIntEnum):
    ADD_TO_GARAGE = auto()
    SELL = auto()
