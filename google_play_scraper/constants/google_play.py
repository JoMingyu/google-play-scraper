from enum import Enum


class Sort(int, Enum):
    NEWEST = 2
    MOST_RELEVANT = 1


class PageType(int, Enum):
    DEVELOPER = 1
    COLLECTION = 2
