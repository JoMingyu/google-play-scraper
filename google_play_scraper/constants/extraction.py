from typing import Callable, List, Type


def nested_lookup(source, indexes):
    if len(indexes) == 1:
        return source[indexes[0]]
    return nested_lookup(source[indexes[0]], indexes[1::])


class ExtractionSpec:
    def __init__(self, ds_num, extraction_map, post_processor=None):
        # type: (int, List[int], Callable) -> None
        self.ds_num = ds_num
        self.extraction_map = extraction_map
        self.post_processor = post_processor

    def extract(self, source):
        return nested_lookup(source["ds:{}".format(self.ds_num)], self.extraction_map)


class ExtractionSpecs:
    Detail = {
        "title": ExtractionSpec(5, [0, 0, 0]),
        "description": ExtractionSpec(5, [0, 10, 0, 1]),
        "descriptionHTML": ExtractionSpec(5, [0, 10, 0, 1]),
        "summary": ExtractionSpec(5, [0, 10, 1, 1]),
        "installs": ExtractionSpec(5, [0, 12, 9, 0]),
        "minInstalls": ExtractionSpec(5, [0, 12, 9, 0]),
        "score": ExtractionSpec(7, [0, 6, 0, 1]),
        "scoreText": ExtractionSpec(7, [0, 6, 0, 0]),
        "ratings": ExtractionSpec(7, [0, 6, 2, 1]),
        "reviews": ExtractionSpec(7, [0, 6, 3, 1]),
        "histogram": ExtractionSpec(7, [0, 6, 1]),
        "price": ExtractionSpec(3, [0, 2, 0, 0, 0, 1, 0, 0]),
        "free": ExtractionSpec(3, [0, 2, 0, 0, 0, 1, 0, 0]),
        "currency": ExtractionSpec(3, [0, 2, 0, 0, 0, 1, 0, 1]),
        "priceText": ExtractionSpec(3, [0, 2, 0, 0, 0, 1, 0, 2]),
        "offersIAP": ExtractionSpec(5, [0, 12, 12, 0]),
        "size": ExtractionSpec(8, [0]),
        "androidVersion": ExtractionSpec(8, [2]),
        "androidVersionText": ExtractionSpec(8, [2]),
        "developer": ExtractionSpec(5, [0, 12, 5, 1]),
        "developerId": ExtractionSpec(5, [0, 12, 5, 5, 4, 2]),
        "developerEmail": ExtractionSpec(5, [0, 12, 5, 2, 0]),
        "developerWebsite": ExtractionSpec(5, [0, 12, 5, 3, 5, 2]),
        "developerAddress": ExtractionSpec(5, [0, 12, 5, 4, 0]),
        "privacyPolicy": ExtractionSpec(5, [0, 12, 7, 2]),
        "developerInternalID": ExtractionSpec(5, [0, 12, 5, 0, 0]),
        "genre": ExtractionSpec(5, [0, 12, 13, 0, 0]),
        "genreId": ExtractionSpec(5, [0, 12, 13, 0, 2]),
        # "familyGenre": ExtractionSpec(5, [0, 12, 13, 1, 0]),
        # "familyGenreId": ExtractionSpec(5, [0, 12, 13, 1, 2]),
        "icon": ExtractionSpec(5, [0, 12, 1, 3, 2]),
        "headerImage": ExtractionSpec(5, [0, 12, 2, 3, 2]),
        "screenshots": ExtractionSpec(5, [0, 12, 0]),
        "video": ExtractionSpec(5, [0, 12, 3, 0, 3, 2]),
        "videoImage": ExtractionSpec(5, [0, 12, 3, 1, 3, 2]),
        "contentRating": ExtractionSpec(5, [0, 12, 4, 0]),
        # "contentRatingDescription": ExtractionSpec(5, [0, 12, 4, 2, 1]),
        "adSupported": ExtractionSpec(5, [0, 12, 14, 0]),
        "released": ExtractionSpec(5, [0, 12, 36]),
        "updated": ExtractionSpec(5, [0, 12, 8, 0]),
        "version": ExtractionSpec(8, [1]),
        "recentChanges": ExtractionSpec(5, [0, 12, 6, 1]),
        "comments": ExtractionSpec(15, [0]),
    }
