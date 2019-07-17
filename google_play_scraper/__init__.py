import json
from urllib.request import urlopen

from google_play_scraper.constants.extraction import ExtractionSpecs
from google_play_scraper.constants.regex import Regex
from google_play_scraper.constants.url import URLFormats


"""
  const scriptRegex = />AF_initDataCallback[\s\S]*?<\/script/g;
  const keyRegex = /(ds:.*?)'/;
  const valueRegex = /return ([\s\S]*?)}}\);<\//;
"""


def _build_url(url, qs):
    # type: (str, dict) -> str
    return "{}?{}".format(url, "&".join(["{}={}".format(k, v) for k, v in qs.items()]))


def list():
    pass


def app(app_id, lang="en", country="us"):
    url = URLFormats.Detail.build_url({"id": app_id, "hl": lang, "gl": country})
    resp = urlopen(url)

    dom = resp.read().decode()

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

    for k, spec in ExtractionSpecs.Detail.items():
        result[k] = spec.extract(res)

    return result
