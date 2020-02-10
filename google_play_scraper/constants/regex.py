import re


class Regex:
    NOT_NUMBER = re.compile("[^\d]")
    SCRIPT = re.compile("AF_initDataCallback[\s\S]*?<\/script")
    KEY = re.compile("(ds:.*?)'")
    VALUE = re.compile("return ([\s\S]*?)}}\);<\/")
    REVIEWS = re.compile("\)]}'\n\n([\s\S]+)")
