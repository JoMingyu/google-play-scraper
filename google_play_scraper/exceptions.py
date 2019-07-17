class GooglePlayScraperException(Exception):
    pass


class ContentNotFoundException(GooglePlayScraperException):
    pass


class InvalidURLError(GooglePlayScraperException):
    pass


class NotFoundError(GooglePlayScraperException):
    pass


class ExtraHTTPError(GooglePlayScraperException):
    pass
