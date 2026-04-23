import json
from typing import Any, Dict, List

from google_play_scraper.constants.element import ElementSpecs
from google_play_scraper.constants.element import resolve_specs
from google_play_scraper.constants.regex import Regex
from google_play_scraper.constants.request import Formats
from google_play_scraper.utils.request import post
from google_play_scraper.exceptions import NotFoundError


def data_safety(app_id: str, lang: str = "en", country: str = "us") -> Dict[str, Any]:
    """Fetch the data safety section for an app from Google Play.

    Args:
        app_id: The app package name (e.g. "com.spotify.music").
        lang: ISO 639-1 language code (default "en").
        country: ISO 3166-1 country code (default "us").

    Returns:
        A dict with keys: privacyPolicyUrl, sharedData, collectedData, securityPractices.

    Raises:
        NotFoundError: If the app does not exist on Google Play.
    """
    dom = post(
        Formats.DataSafety.build(lang=lang, country=country),
        Formats.DataSafety.build_body(app_id),
        {"content-type": "application/x-www-form-urlencoded;charset=UTF-8"},
    )

    return _parse_dom(dom)


def _parse_dom(dom: str) -> Dict[str, Any]:
    matches = json.loads(Regex.DATA_SAFETY.findall(dom)[0])
    container_json = matches[0][2]

    if container_json is None:
        raise NotFoundError("App not found.")

    container = json.loads(container_json)

    return resolve_specs(container, ElementSpecs.DataSafety)
