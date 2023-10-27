from enum import Enum


class Sort(int, Enum):
    NEWEST = 2
    MOST_RELEVANT = 1


class Device(int, Enum):
    MOBILE = 2
    TABLET = 3
    CHROMEBOOK = 5
    TV = 6
