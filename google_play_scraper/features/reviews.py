import json

from google_play_scraper import Sort
from google_play_scraper.constants.element import ElementSpecs
from google_play_scraper.constants.regex import Regex
from google_play_scraper.constants.url import Formats
from google_play_scraper.utils.request import post


def _fetch_review_items(url, app_id, sort, count, pagination_token):
    dom = post(
        url,
        Formats.ReviewPayload.build(app_id, sort, count, pagination_token),
        {"content-type": "application/x-www-form-urlencoded"},
    )

    match = json.loads(Regex.REVIEWS.findall(dom)[0])

    return json.loads(match[0][2])[0], json.loads(match[0][2])[-1][-1]


def reviews(app_id, lang="en", country="us", sort=Sort.NEWEST, count=100):
    # type: (str, str, str, Sort, int) -> list
    # TODO filtering with rating
    # TODO filtering with device model
    # TODO reply data
    # TODO refactoring

    pagination_token = None

    url = Formats.Reviews.build(lang=lang, country=country)

    if count < 200:
        _count = count
    else:
        _count = 199

    result = []

    while True:
        review_items, pagination_token = _fetch_review_items(
            url, app_id, sort, _count, pagination_token
        )

        for review in review_items:
            review_dict = {}

            for k, spec in ElementSpecs.Review.items():
                review_dict[k] = spec.extract_content(review)

            result.append(review_dict)

            if len(result) >= count:
                break
        else:
            continue
        break

    return result
