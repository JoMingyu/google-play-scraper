import json
from datetime import datetime
from typing import Union

from google_play_scraper.constants.google_play import Sort

try:
    from urllib.error import HTTPError
except ImportError:
    from urllib2 import HTTPError

try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request

from .constants.element import ElementSpecs
from .constants.regex import Regex
from .constants.url import URLFormats
from .exceptions import (
    ContentNotFoundException,
    InvalidURLError,
    NotFoundError,
    ExtraHTTPError,
)


__version__ = "0.0.2.0"


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


def _post(url, data, headers):
    # type: (str, Union[str, bytes], dict) -> str

    return _urlopen(Request(url, data=data, headers=headers))


def _get(url):
    # type: (str) -> str

    return _urlopen(url)


def app(app_id, lang="en", country="us"):
    # type: (str, str, str) -> dict
    url = URLFormats.Detail.build_url(app_id=app_id, lang=lang, country=country)

    dom = _get(url)

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


def reviews(app_id, lang="en", country="us", sort=Sort.NEWEST, count=100):
    # type: (str, str, str, Sort, int) -> list
    # TODO filtering with rating
    # TODO filtering with device model
    # TODO reply data
    # TODO refactoring

    pagination_token = None

    def _fetch_review_items():
        nonlocal pagination_token

        if pagination_token is None:
            payload = f"f.req=%5B%5B%5B%22UsvDTd%22%2C%22%5Bnull%2Cnull%2C%5B2%2C{sort}%2C%5B{_count}%2Cnull%2Cnull%5D%2Cnull%2C%5B%5D%5D%2C%5B%5C%22{app_id}%5C%22%2C7%5D%5D%22%2Cnull%2C%22generic%22%5D%5D%5D".encode()
        else:
            payload = f"f.req=%5B%5B%5B%22UsvDTd%22%2C%22%5Bnull%2Cnull%2C%5B2%2C{sort}%2C%5B{_count}%2Cnull%2C%5C%22{pagination_token}%5C%22%5D%2Cnull%2C%5B%5D%5D%2C%5B%5C%22{app_id}%5C%22%2C7%5D%5D%22%2Cnull%2C%22generic%22%5D%5D%5D".encode()

        dom = _post(url, payload, {"content-type": "application/x-www-form-urlencoded"})

        match = json.loads(Regex.REVIEWS.findall(dom)[0])
        pagination_token = json.loads(match[0][2])[-1][-1]
        return json.loads(match[0][2])[0]

    url = URLFormats.Reviews.build_url(lang=lang, country=country)

    if count < 200:
        _count = count
    else:
        _count = 199

    result = []

    while True:
        review_items = _fetch_review_items()

        for review in review_items:
            try:
                user_name = review[1][0]
            except IndexError:
                user_name = None

            try:
                user_image = review[1][1][3][2]
            except IndexError:
                user_image = None

            try:
                content = review[4]
            except IndexError:
                content = None

            try:
                score = review[2]
            except IndexError:
                score = None

            try:
                thumbs_up_count = review[6]
            except IndexError:
                thumbs_up_count = None

            try:
                review_created_version = review[10]
            except IndexError:
                review_created_version = None

            try:
                at = datetime.fromtimestamp(review[5][0])
            except IndexError:
                at = None

            result.append(
                {
                    "userName": user_name,
                    "userImage": user_image,
                    "content": content,
                    "score": score,
                    "thumbsUpCount": thumbs_up_count,
                    "reviewCreatedVersion": review_created_version,
                    "at": at,
                }
            )

            if len(result) >= count:
                break
        else:
            continue
        break

    return result
