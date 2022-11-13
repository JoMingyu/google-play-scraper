import re


class Regex:
    NOT_NUMBER = re.compile(r"[^\d]")
    SCRIPT = re.compile(r"AF_initDataCallback[\s\S]*?<\/script")
    KEY = re.compile(r"(ds:.*?)'")
    VALUE = re.compile(r"data:([\s\S]*?), sideChannel: {}}\);<\/")
    REVIEWS = re.compile(r"\)]}'\n\n([\s\S]+)")
    PERMISSIONS = re.compile(r"\)]}'\n\n([\s\S]+)")
