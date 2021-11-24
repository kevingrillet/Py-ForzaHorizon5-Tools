from enum import auto, Enum

from utils.superintenum import SuperIntEnum


class DebugLevel(SuperIntEnum):
    ALWAYS = auto()
    INFO = auto()
    FUNCTIONS = auto()
    CLASS = auto()
    DEBUG = auto()


class Lang(Enum):
    ENGLISH = "en"
    FRENCH = "fr"
