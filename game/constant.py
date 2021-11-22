# Constant file to be clean
from enum import auto, Enum

from utils.superintenum import SuperIntEnum

DEBUG_LEVEL = 0
DEV_MODE = False
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


class Lang(Enum):
    FRENCH = "fr"


LANG = Lang.FRENCH
