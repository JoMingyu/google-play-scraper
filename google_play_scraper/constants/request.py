from abc import abstractmethod

from google_play_scraper import Sort

PLAY_STORE_BASE_URL = "https://play.google.com"


class Format:
    @abstractmethod
    def build(self, *args):
        raise NotImplementedError


class Formats:
    class _Detail(Format):
        URL_FORMAT = "{}/store/apps/details?id={{app_id}}&hl={{lang}}&gl={{country}}".format(
            PLAY_STORE_BASE_URL
        )

        def build(self, app_id, lang, country):
            # type: (str, str, str) -> str
            return self.URL_FORMAT.format(app_id=app_id, lang=lang, country=country)

    class _Reviews(Format):
        URL_FORMAT = "{}/_/PlayStoreUi/data/batchexecute?hl={{lang}}&gl={{country}}".format(
            PLAY_STORE_BASE_URL
        )

        def build(self, lang, country):
            # type: (str, str) -> str
            return self.URL_FORMAT.format(lang=lang, country=country)

    class _ReviewsBodyData(Format):
        PAYLOAD_FORMAT_FOR_FIRST_PAGE = "f.req=%5B%5B%5B%22UsvDTd%22%2C%22%5Bnull%2Cnull%2C%5B2%2C{sort}%2C%5B{count}%2Cnull%2Cnull%5D%2Cnull%2C%5Bnull%2C{score}%5D%5D%2C%5B%5C%22{app_id}%5C%22%2C7%5D%5D%22%2Cnull%2C%22generic%22%5D%5D%5D"
        PAYLOAD_FORMAT_FOR_PAGINATED_PAGE = "f.req=%5B%5B%5B%22UsvDTd%22%2C%22%5Bnull%2Cnull%2C%5B2%2C{sort}%2C%5B{count}%2Cnull%2C%5C%22{pagination_token}%5C%22%5D%2Cnull%2C%5Bnull%2C{score}%5D%5D%2C%5B%5C%22{app_id}%5C%22%2C7%5D%5D%22%2Cnull%2C%22generic%22%5D%5D%5D"

        def build(self, app_id, sort, count, filter_score_with, pagination_token):
            # type: (str, Sort, int, int, str) -> bytes
            if pagination_token is not None:
                result = self.PAYLOAD_FORMAT_FOR_PAGINATED_PAGE.format(
                    app_id=app_id,
                    sort=sort,
                    count=count,
                    score=filter_score_with,
                    pagination_token=pagination_token,
                )
            else:
                result = self.PAYLOAD_FORMAT_FOR_FIRST_PAGE.format(
                    app_id=app_id, sort=sort, score=filter_score_with, count=count
                )

            return result.encode()

    Detail = _Detail()
    Reviews = _Reviews()
    ReviewsBodyData = _ReviewsBodyData()
