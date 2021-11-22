from enum import auto

from utils.superintenum import SuperIntEnum


class DebugLevel(SuperIntEnum):
    ALWAYS = auto()
    INFO = auto()
    FUNCTIONS = auto()
    CLASS = auto()
    DEBUG = auto()
