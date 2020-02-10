from abc import abstractmethod

PLAY_STORE_BASE_URL = "https://play.google.com"


class URLFormat:
    @abstractmethod
    def build_url(self, *args):
        raise NotImplementedError


class URLFormats:
    class _Detail(URLFormat):
        URL_FORMAT = "{}/store/apps/details?id={{app_id}}&hl={{lang}}&gl={{country}}".format(
            PLAY_STORE_BASE_URL
        )

        def build_url(self, app_id, lang, country):
            # type: (str, str, str) -> str
            return self.URL_FORMAT.format(app_id=app_id, lang=lang, country=country)

    class _Reviews(URLFormat):
        URL_FORMAT = "{}/_/PlayStoreUi/data/batchexecute?hl={{lang}}&gl={{country}}".format(
            PLAY_STORE_BASE_URL
        )

        def build_url(self, lang, country):
            # type: (str, str) -> str
            return self.URL_FORMAT.format(lang=lang, country=country)

    Detail = _Detail()
    Reviews = _Reviews()
