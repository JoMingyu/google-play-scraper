from typing import Union

from google_play_scraper.exceptions import NotFoundError, ExtraHTTPError

try:
    from urllib.error import HTTPError
except ImportError:
    from urllib2 import HTTPError

try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request


def _urlopen(obj):
    try:
        resp = urlopen(obj)
    except HTTPError as e:
        if e.code == 404:
            raise NotFoundError("App not found(404).")
        else:
            raise ExtraHTTPError(
                "App not found. Status code {} returned.".format(e.code)
            )

    return resp.read().decode("UTF-8")


def post(url, data, headers):
    # type: (str, Union[str, bytes], dict) -> str

    return _urlopen(Request(url, data=data, headers=headers))


def get(url):
    # type: (str) -> str

    return _urlopen(url)
