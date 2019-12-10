import re


class Regex:
    SCRIPT = re.compile("AF_initDataCallback[\s\S]*?<\/script")
    KEY = re.compile("(ds:.*?)'")
    VALUE = re.compile("return ([\s\S]*?)}}\);<\/")
    NOT_NUMBER = re.compile("[^\d]")
