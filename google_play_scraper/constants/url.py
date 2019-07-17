from abc import abstractmethod


class URLFormat:
    @abstractmethod
    def build_url(self, qs):
        # type: (dict) -> str
        ...


class URLFormats:
    class _Detail(URLFormat):
        URL_FORMAT = (
            "https://play.google.com/store/apps/details?id={id}&hl={hl}&gl={gl}"
        )

        def build_url(self, qs):
            return self.URL_FORMAT.format(**qs)

    Detail = _Detail()
