import ssl
import time
from typing import Union
from urllib.error import HTTPError
from urllib.request import Request, urlopen

from google_play_scraper.exceptions import ExtraHTTPError, NotFoundError

ssl._create_default_https_context = ssl._create_unverified_context

MAX_RETRIES = 3
RATE_LIMIT_DELAY = 5


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


def post(url: str, data: Union[str, bytes], headers: dict) -> str:
    last_exception = None
    rate_exceeded_count = 0
    for _ in range(MAX_RETRIES):
        try:
            resp = _urlopen(Request(url, data=data, headers=headers))
        except Exception as e:
            last_exception = e
            continue
        if "com.google.play.gateway.proto.PlayGatewayError" in resp:
            rate_exceeded_count += 1
            last_exception = Exception("com.google.play.gateway.proto.PlayGatewayError")
            time.sleep(RATE_LIMIT_DELAY * rate_exceeded_count)
            continue
        return resp
    raise last_exception


def get(url: str) -> str:
    return _urlopen(url)
