import HTMLParser

from google_play_scraper.constants.request import PLAY_STORE_BASE_URL


def unescape_text(s):
    parser = HTMLParser.HTMLParser()
    return parser.unescape(s.replace("<br>", "\r\n"))


def prepend_playstore_base_url(url):
    return ''.join([PLAY_STORE_BASE_URL, url])
