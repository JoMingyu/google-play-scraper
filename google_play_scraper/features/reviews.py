import json
from time import sleep

try:
    from typing import Optional, Tuple
except ImportError:
    pass

from google_play_scraper import Sort
from google_play_scraper.constants.element import ElementSpecs
from google_play_scraper.constants.regex import Regex
from google_play_scraper.constants.request import Formats
from google_play_scraper.utils.request import post


LANG_DEFAULT = "en"
COUNTRY_DEFAULT = "us"
SORT_DEFAULT = Sort.NEWEST
COUNT_DEFAULT = 100


class ContinuationToken:
    __slots__ = "token", "lang", "country", "sort", "count", "filter_score_with"

    def __init__(self, token, lang, country, sort, count, filter_score_with):
        self.token = token
        self.lang = lang
        self.country = country
        self.sort = sort
        self.count = count
        self.filter_score_with = filter_score_with

    def unpack(self):
        return (
            self.token,
            self.lang,
            self.country,
            self.sort,
            self.count,
            self.filter_score_with,
        )


def _fetch_review_items(url, app_id, sort, count, filter_score_with, pagination_token):
    dom = post(
        url,
        Formats.ReviewsBodyData.build(
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
    app_id,
    lang=None,
    country=None,
    sort=None,
    count=None,
    filter_score_with=None,
    continuation_token=None,
):
    # type: (str, str, str, int, int, Optional[int], Optional[ContinuationToken]) -> Tuple[list, ContinuationToken]

    if continuation_token is not None:
        token = continuation_token.token

        lang = continuation_token.lang if lang is None else lang
        country = continuation_token.country if country is None else country
        sort = continuation_token.sort if sort is None else sort
        count = continuation_token.count if count is None else count
        filter_score_with = (
            continuation_token.filter_score_with
            if filter_score_with is None
            else filter_score_with
        )
    else:
        token = None

    if lang is None:
        lang = LANG_DEFAULT

    if country is None:
        country = COUNTRY_DEFAULT

    if sort is None:
        sort = SORT_DEFAULT

    if count is None:
        count = COUNT_DEFAULT

    if count < 200:
        _count = count
    else:
        _count = 199

    url = Formats.Reviews.build(lang=lang, country=country)

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
            review_dict = {}

            for k, spec in ElementSpecs.Review.items():
                review_dict[k] = spec.extract_content(review)

            result.append(review_dict)

        remaining_count_of_reviews_to_fetch = count - len(result)

        if remaining_count_of_reviews_to_fetch == 0:
            break

        if isinstance(token, list):
            token = None
            break

        if remaining_count_of_reviews_to_fetch < 200:
            _count = remaining_count_of_reviews_to_fetch

    return (
        result,
        ContinuationToken(token, lang, country, sort, count, filter_score_with),
    )


def reviews_all(app_id, sleep_milliseconds=0, **kwargs):
    kwargs.pop("count", None)
    kwargs.pop("continuation_token", None)

    _count = 199
    _continuation_token = None
    result = []

    while True:
        result_, _continuation_token = reviews(
            app_id, count=_count, continuation_token=_continuation_token, **kwargs
        )

        result += result_

        if _continuation_token.token is None:
            break

        if sleep_milliseconds:
            sleep(sleep_milliseconds / 1000)

    return result
