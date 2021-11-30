from enum import auto, Enum

from utils.superintenum import SuperIntEnum


class DebugLevel(SuperIntEnum):
    ALWAYS = auto()
    INFO = auto()
    CLASS = auto()
    FUNCTIONS = auto()
    DEBUG = auto()


class Lang(Enum):
    ENGLISH = 'en'
    FRENCH = 'fr'
