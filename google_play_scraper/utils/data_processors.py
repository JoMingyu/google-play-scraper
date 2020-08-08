try:
    from html import unescape
except ImportError:
    from html.parser import HTMLParser

    unescape = HTMLParser().unescape


def unescape_text(s):
    return unescape(s.replace("<br>", "\r\n"))
