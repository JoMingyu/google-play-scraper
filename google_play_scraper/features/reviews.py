import json

from google_play_scraper import Sort
from google_play_scraper.constants.element import ElementSpecs
from google_play_scraper.constants.regex import Regex
from google_play_scraper.constants.url import URLFormats
from google_play_scraper.utils.request import _post


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
