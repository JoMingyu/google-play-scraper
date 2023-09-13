from typing import Union
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen, ProxyHandler, build_opener

from google_play_scraper.exceptions import ExtraHTTPError, NotFoundError, ExtraURLError


def _urlopen(obj, proxy: str = None):
    try:
        if proxy:
            proxy_handler = ProxyHandler({"https": proxy})
            opener = build_opener(proxy_handler)
            resp = opener.open(obj, timeout=10)
        else:
            resp = urlopen(obj, timeout=10)
    except HTTPError as e:
        if e.code == 404:
            raise NotFoundError("App not found (404).")
        else:
            raise ExtraHTTPError(
                "App not found. Status code {} returned.".format(e.code)
            )
    except URLError:
        raise ExtraURLError()

    return resp.read().decode("UTF-8")


def post(url: str, data: Union[str, bytes], headers: dict, proxy: str = None) -> str:
    return _urlopen(Request(url, data=data, headers=headers), proxy)


def get(url: str, proxy: str = None) -> str:
    return _urlopen(url, proxy)
