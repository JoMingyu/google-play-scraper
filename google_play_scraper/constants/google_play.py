from enum import Enum


class Sort(int, Enum):
    MOST_RELEVANT = 1
    NEWEST = 2
    RATING = 3


class Device(int, Enum):
    MOBILE = 2
    TABLET = 3
    CHROMEBOOK = 5
    TV = 6
