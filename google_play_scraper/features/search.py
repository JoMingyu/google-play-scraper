import json
from typing import Any, Dict, List
from urllib.parse import quote

from google_play_scraper.constants.element import ElementSpecs
from google_play_scraper.constants.regex import Regex
from google_play_scraper.constants.request import Formats
from google_play_scraper.exceptions import NotFoundError
from google_play_scraper.utils.request import get


def search(
    query: str, n_hits: int = 30, lang: str = "en", country: str = "us"
) -> List[Dict[str, Any]]:
    if n_hits <= 0:
        return []

    query = quote(query)
    url = Formats.Searchresults.build(query=query, lang=lang, country=country)
    try:
        dom = get(url)
    except NotFoundError:
        url = Formats.Searchresults.fallback_build(query=query, lang=lang)
        dom = get(url)

    matches = Regex.SCRIPT.findall(dom)  # take out script blocks from dom

    dataset = {}

    for match in matches:
        key_match = Regex.KEY.findall(match)
        value_match = Regex.VALUE.findall(match)

        if key_match and value_match:
            key = key_match[0]
            value = json.loads(value_match[0])

            dataset[key] = value

    try:
        top_result = dataset["ds:4"][0][1][0][23][16]
    except IndexError:
        top_result = None

    success = False
    # different idx for different countries and languages
    for idx in range(len(dataset["ds:4"][0][1])):
        try:
            dataset = dataset["ds:4"][0][1][idx][22][0]
            success = True
        except Exception:
            pass
    if not success:
        return []

    n_apps = min(len(dataset), n_hits)

    search_results = (
        [
            {
                k: spec.extract_content(top_result)
                for k, spec in ElementSpecs.SearchResultOnTop.items()
            }
        ]
        if top_result
        else []
    )

    for app_idx in range(n_apps - len(search_results)):
        app = {}
        for k, spec in ElementSpecs.SearchResult.items():
            content = spec.extract_content(dataset[app_idx])
            app[k] = content

        search_results.append(app)

    return search_results
