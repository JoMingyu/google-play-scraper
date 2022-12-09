from html import unescape


def unescape_text(s):
    return unescape(s.replace("<br>", "\r\n"))
