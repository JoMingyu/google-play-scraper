import re


class Regex:
    NOT_NUMBER = re.compile("[^\d]")
    SCRIPT = re.compile("AF_initDataCallback[\s\S]*?<\/script")
    KEY = re.compile("(ds:.*?)'")
    VALUE = re.compile("data:([\s\S]*?), sideChannel: {}}\);<\/")
    REVIEWS = re.compile("\)]}'\n\n([\s\S]+)")
