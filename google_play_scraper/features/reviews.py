import json
from time import sleep

from typing import Optional, Tuple, List

from google_play_scraper import Sort
from google_play_scraper.constants.element import ElementSpecs
from google_play_scraper.constants.regex import Regex
from google_play_scraper.constants.request import Formats
from google_play_scraper.utils.request import post


class ContinuationToken:
    __slots__ = "token", "lang", "country", "sort", "count", "filter_score_with"

    def __init__(self, token, lang, country, sort, count, filter_score_with):
        self.token = token
        self.lang = lang
        self.country = country
        self.sort = sort
        self.count = count
        self.filter_score_with = filter_score_with


def _fetch_review_items(url: str, app_id: str, sort: int, count: int, filter_score_with: Optional[int], pagination_token: Optional[str]):
    dom = post(
        url,
        Formats.Reviews.build_body(
            app_id,
            sort,
            count,
            "null" if filter_score_with is None else filter_score_with,
            pagination_token,
        ),
        {"content-type": "application/x-www-form-urlencoded"},
    )

    match = json.loads(Regex.REVIEWS.findall(dom)[0])

    return json.loads(match[0][2])[0], json.loads(match[0][2])[-1][-1]


def reviews(
    app_id: str,
    lang: str='en',
    country: str='us',
    sort: int=Sort.NEWEST,
    count: int=100,
    filter_score_with: int=None,
    continuation_token: ContinuationToken=None,
) -> Tuple[List[dict], ContinuationToken]:
    if continuation_token is not None:
        token = continuation_token.token

        lang = continuation_token.lang
        country = continuation_token.country
        sort = continuation_token.sort
        count = continuation_token.count
        filter_score_with = (
            continuation_token.filter_score_with
        )
    else:
        token = None

    url = Formats.Reviews.build(lang=lang, country=country)

    if count < 200:
        _count = count
    else:
        _count = 199

    result = []

    while True:
        try:
            review_items, token = _fetch_review_items(
                url, app_id, sort, _count, filter_score_with, token
            )
        except (TypeError, IndexError):
            token = None
            break

        for review in review_items:
            result.append({k: spec.extract_content(review) for k, spec in ElementSpecs.Review.items()})

        remaining_count = count - len(result)

        if remaining_count == 0:
            break

        if isinstance(token, list):
            token = None
            break

        if remaining_count < 200:
            _count = remaining_count

    return (
        result,
        ContinuationToken(token, lang, country, sort, count, filter_score_with),
    )


def reviews_all(app_id: str, sleep_seconds: int=0, **kwargs) -> list:
    kwargs.pop("count", None)
    kwargs.pop("continuation_token", None)

    _count = 199
    _continuation_token = None

    result = []

    while True:
        _result, _continuation_token = reviews(
            app_id, count=_count, continuation_token=_continuation_token, **kwargs
        )

        result += _result

        if _continuation_token.token is None:
            break

        if sleep_seconds:
            sleep(sleep_seconds)

    return result
