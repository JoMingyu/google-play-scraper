from typing import Union
from urllib.error import HTTPError
from urllib.request import Request
from typing import Optional

from google_play_scraper.exceptions import ExtraHTTPError, NotFoundError
from google_play_scraper.utils.proxies import Proxy

import requests

def _urlopen(obj, proxy: Optional[Proxy] = None):
    try:
        resp = requests.get(obj, proxies=proxy.get_proxy()).text
    except HTTPError as e:
        if e.code == 404:
            raise NotFoundError("App not found(404).")
        else:
            raise ExtraHTTPError(
                "App not found. Status code {} returned.".format(e.code)
            )
    print(resp)
    return resp


def post(url: str, data: Union[str, bytes], headers: dict) -> str:
    return _urlopen(Request(url, data=data, headers=headers))


def get(url: str, proxy: Optional[Proxy] = None) -> str:
    return _urlopen(url, proxy)
