import json

from google_play_scraper.constants.regex import Regex
from google_play_scraper.constants.request import Formats
from google_play_scraper.utils.request import post
from google_play_scraper.constants.element import ElementSpecs


def permissions(app_id, lang="en", country="us"):
    # type: (str, str, str) -> dict

    url = Formats.Permissions.build(lang=lang, country=country)
    payload = Formats.PermissionsBodyData.build(app_id)

    dom = post(
        url,
        payload,
        {"content-type": "application/x-www-form-urlencoded"}
    )

    matches = json.loads(Regex.PERMISSIONS.findall(dom)[0])
    container = json.loads(matches[0][2])

    result = list()

    for permission_items in container:
        if isinstance(permission_items, list) and len(permission_items[0]) == 2:
            #rearrange layout of to fit ElementSpecs
            permission_items = [["Uncategorized", None, permission_items, None]]

        if isinstance(permission_items, list):
            for permission in permission_items:
                group_dict = {}
                
                for k, spec in ElementSpecs.PermissionGroup.items():
                    group_dict[k] = spec.extract_content(permission)

                for permission in group_dict['permissions']:
                    result.append((group_dict['type'], permission))

    return result