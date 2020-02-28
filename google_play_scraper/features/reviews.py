import json
from pprint import pprint
from typing import Optional

from google_play_scraper import Sort
from google_play_scraper.constants.element import ElementSpecs
from google_play_scraper.constants.regex import Regex
from google_play_scraper.constants.url import Formats
from google_play_scraper.utils.request import post


def _fetch_review_items(url, app_id, sort, count, filter_score_with, pagination_token):
    dom = post(
        url,
        Formats.ReviewPayload.build(
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
    app_id, lang="en", country="us", sort=Sort.NEWEST, count=100, filter_score_with=None
):
    # type: (str, str, str, Sort, int, Optional[int]) -> list

    url = Formats.Reviews.build(lang=lang, country=country)

    if count < 200:
        _count = count
    else:
        _count = 199

    result = []

    pagination_token = None

    while True:
        review_items, pagination_token = _fetch_review_items(
            url, app_id, sort, _count, filter_score_with, pagination_token
        )

        for review in review_items:
            review_dict = {}

            for k, spec in ElementSpecs.Review.items():
                review_dict[k] = spec.extract_content(review)

            result.append(review_dict)

        remaining_count_of_reviews_to_fetch = count - len(result)

        if remaining_count_of_reviews_to_fetch == 0:
            break

        if isinstance(pagination_token, list):
            break

        if remaining_count_of_reviews_to_fetch < 200:
            _count = remaining_count_of_reviews_to_fetch

        else:
            continue

    return result
