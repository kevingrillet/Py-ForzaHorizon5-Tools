from enum import auto, Enum

from utils.constant import DebugLevel, Lang
from utils.superintenum import SuperIntEnum


class AlreadyOwnedChoice(SuperIntEnum):
    ADD_TO_GARAGE = auto()
    SELL = auto()


class Car(Enum):
    FORD = "ford"
    PONTIAC = "pontiac"
    PORSCHE = "porsche"


class RaceStep(SuperIntEnum):
    INIT = auto()
    PREPARING = auto()
    RACING = auto()
    REWARDS = auto()
    CHECK = auto()
    RESTART = auto()


CAR = Car.PONTIAC
DEBUG_LEVEL = DebugLevel.ALWAYS
DEV_MODE = False
LANG = Lang.FRENCH
SCALE = 1
OWNED = AlreadyOwnedChoice.SELL
WINDOW_NAME = "Forza Horizon 5"
