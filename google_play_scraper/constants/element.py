from datetime import datetime

from google_play_scraper.utils.data_processors import unescape_text

try:
    from typing import Callable, List, Any, Optional
except ImportError:
    pass

from google_play_scraper.constants.regex import Regex
from google_play_scraper.utils import nested_lookup


class ElementSpec:
    def __init__(self, ds_num, data_map, post_processor=None, fallback_value=None):
        # type: (Optional[int], List[int], Callable, Any) -> None
        self.ds_num = ds_num
        self.data_map = data_map
        self.post_processor = post_processor
        self.fallback_value = fallback_value

    def extract_content(self, source):
        # type: (dict) -> Any

        try:
            if self.ds_num is None:
                result = nested_lookup(source, self.data_map)
            else:
                result = nested_lookup(
                    source["ds:{}".format(self.ds_num)], self.data_map
                )

            if self.post_processor is not None:
                result = self.post_processor(result)
        except:
            result = self.fallback_value

        return result


class ElementSpecs:
    Detail = {
        "title": ElementSpec(5, [0, 0, 0]),
        "description": ElementSpec(5, [0, 10, 0, 1], unescape_text),
        "descriptionHTML": ElementSpec(5, [0, 10, 0, 1]),
        "summary": ElementSpec(5, [0, 10, 1, 1], unescape_text),
        "summaryHTML": ElementSpec(5, [0, 10, 1, 1]),
        "installs": ElementSpec(5, [0, 12, 9, 0]),
        "minInstalls": ElementSpec(
            5, [0, 12, 9, 0], lambda s: int(Regex.NOT_NUMBER.sub("", s)) if s else 0
        ),
        "score": ElementSpec(6, [0, 6, 0, 1]),
        "ratings": ElementSpec(
            6, [0, 6, 1], lambda container: sum([item[1] for item in container[1:]])
        ),
        "reviews": ElementSpec(6, [0, 6, 3, 1]),
        "histogram": ElementSpec(
            6,
            [0, 6, 1],
            lambda container: [
                container[1][1],
                container[2][1],
                container[3][1],
                container[4][1],
                container[5][1],
            ],
            [0, 0, 0, 0, 0],
        ),
        "price": ElementSpec(
            3, [0, 2, 0, 0, 0, 1, 0, 0], lambda price: (price / 1000000) or 0
        ),
        "free": ElementSpec(3, [0, 2, 0, 0, 0, 1, 0, 0], lambda s: s == 0),
        "currency": ElementSpec(3, [0, 2, 0, 0, 0, 1, 0, 1]),
        "sale": ElementSpec(3, [0, 2, 0, 0, 0, 14, 0, 0], bool, False),
        "saleTime": ElementSpec(3, [0, 2, 0, 0, 0, 14, 0, 0]),
        "originalPrice": ElementSpec(
            3, [0, 2, 0, 0, 0, 1, 1, 0], lambda price: (price / 1000000) or 0
        ),
        "saleText": ElementSpec(3, [0, 2, 0, 0, 0, 14, 1]),
        "offersIAP": ElementSpec(5, [0, 12, 12, 0], bool, False),
        "inAppProductPrice": ElementSpec(5, [0, 12, 12, 0]),
        "size": ElementSpec(8, [0]),
        "androidVersion": ElementSpec(8, [2], lambda s: s.split()[0]),
        "androidVersionText": ElementSpec(8, [2]),
        "developer": ElementSpec(5, [0, 12, 5, 1]),
        "developerId": ElementSpec(5, [0, 12, 5, 5, 4, 2], lambda s: s.split("id=")[1]),
        "developerEmail": ElementSpec(5, [0, 12, 5, 2, 0]),
        "developerWebsite": ElementSpec(5, [0, 12, 5, 3, 5, 2]),
        "developerAddress": ElementSpec(5, [0, 12, 5, 4, 0]),
        "privacyPolicy": ElementSpec(5, [0, 12, 7, 2]),
        "developerInternalID": ElementSpec(5, [0, 12, 5, 0, 0]),
        "genre": ElementSpec(5, [0, 12, 13, 0, 0]),
        "genreId": ElementSpec(5, [0, 12, 13, 0, 2]),
        "icon": ElementSpec(5, [0, 12, 1, 3, 2]),
        "headerImage": ElementSpec(5, [0, 12, 2, 3, 2]),
        "screenshots": ElementSpec(
            5, [0, 12, 0], lambda container: [item[3][2] for item in container], []
        ),
        "video": ElementSpec(5, [0, 12, 3, 0, 3, 2]),
        "videoImage": ElementSpec(5, [0, 12, 3, 1, 3, 2]),
        "contentRating": ElementSpec(5, [0, 12, 4, 0]),
        "contentRatingDescription": ElementSpec(5, [0, 12, 4, 2, 1]),
        "adSupported": ElementSpec(5, [0, 12, 14, 0], bool),
        "containsAds": ElementSpec(5, [0, 12, 14, 0], bool, False),
        "released": ElementSpec(5, [0, 12, 36]),
        "updated": ElementSpec(5, [0, 12, 8, 0]),
        "version": ElementSpec(8, [1]),
        "recentChanges": ElementSpec(5, [0, 12, 6, 1], unescape_text),
        "recentChangesHTML": ElementSpec(5, [0, 12, 6, 1]),
        "comments": ElementSpec(
            19, [0], lambda container: [item[4] for item in container], []
        ),
        "editorsChoice": ElementSpec(5, [0, 12, 15, 0], bool, False),
    }

    Review = {
        "reviewId": ElementSpec(None, [0]),
        "userName": ElementSpec(None, [1, 0]),
        "userImage": ElementSpec(None, [1, 1, 3, 2]),
        "content": ElementSpec(None, [4]),
        "score": ElementSpec(None, [2]),
        "thumbsUpCount": ElementSpec(None, [6]),
        "reviewCreatedVersion": ElementSpec(None, [10]),
        "at": ElementSpec(None, [5, 0], lambda v: datetime.fromtimestamp(v)),
        "replyContent": ElementSpec(None, [7, 1]),
        "repliedAt": ElementSpec(None, [7, 2, 0], lambda v: datetime.fromtimestamp(v)),
    }
