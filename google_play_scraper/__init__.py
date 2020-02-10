import json
from urllib.error import HTTPError
from urllib.request import urlopen

from .constants.element import ElementSpecs
from .constants.regex import Regex
from .constants.url import URLFormats
from .exceptions import (
    ContentNotFoundException,
    InvalidURLError,
    NotFoundError,
    ExtraHTTPError,
)


__version__ = "0.0.1.7"


def _request(url):
    # type: (str) -> str

    try:
        resp = urlopen(url)
    except HTTPError as e:
        if e.code == 404:
            raise NotFoundError("App not found(404).")
        else:
            raise ExtraHTTPError(
                "App not found. Status code {} returned.".format(e.code)
            )

    return resp.read().decode()


def app(app_id, lang="en", country="us"):
    url = URLFormats.Detail.build_url({"id": app_id, "hl": lang, "gl": country})

    dom = _request(url)

    matches = Regex.SCRIPT.findall(dom)

    res = {}

    for match in matches:
        key_match = Regex.KEY.findall(match)
        value_match = Regex.VALUE.findall(match)

        if key_match and value_match:
            key = key_match[0]
            value = json.loads(value_match[0])

            res[key] = value

    result = {}

    for k, spec in ElementSpecs.Detail.items():
        content = spec.extract_content(res)

        result[k] = content
        result["appId"] = app_id
        result["url"] = url

    return result
