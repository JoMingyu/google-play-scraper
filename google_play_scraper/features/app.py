import json
from typing import Any, Dict, Optional

from google_play_scraper.constants.element import ElementSpecs
from google_play_scraper.constants.regex import Regex
from google_play_scraper.constants.request import Formats
from google_play_scraper.exceptions import NotFoundError
from google_play_scraper.utils.request import get
from google_play_scraper.utils.proxies import Proxy


def app(app_id: str, lang: str = "en", country: str = "us", proxy: Optional[Proxy] = None) -> Dict[str, Any]:
    url = Formats.Detail.build(app_id=app_id, lang=lang, country=country)

    try:
        dom = get(url, proxy)
    except NotFoundError:
        url = Formats.Detail.fallback_build(app_id=app_id, lang=lang)
        dom = get(url, proxy)
    return parse_dom(dom=dom, app_id=app_id, url=url)


def parse_dom(dom: str, app_id: str, url: str) -> Dict[str, Any]:
    matches = Regex.SCRIPT.findall(dom)

    dataset = {}

    for match in matches:
        key_match = Regex.KEY.findall(match)
        value_match = Regex.VALUE.findall(match)

        if key_match and value_match:
            key = key_match[0]
            value = json.loads(value_match[0])

            dataset[key] = value

    result = {}

    for k, spec in ElementSpecs.Detail.items():
        content = spec.extract_content(dataset)

        result[k] = content

    result["appId"] = app_id
    result["url"] = url

    return result
