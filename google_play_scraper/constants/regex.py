import re


class Regex:
    NOT_NUMBER = re.compile(r"\D")
    SCRIPT = re.compile(r"AF_initDataCallback[\s\S]*?</script")
    KEY = re.compile("(ds:.*?)'")
    VALUE = re.compile(r"data:([\s\S]*?), sideChannel: {}}\);<\/")
    REVIEWS = re.compile(r"\)]}'\n\n([\s\S]+)")
    PERMISSIONS = re.compile(r"\)]}'\n\n([\s\S]+)")
