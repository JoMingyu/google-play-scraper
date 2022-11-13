from unittest import TestCase

from google_play_scraper import developer
from google_play_scraper.exceptions import NotFoundError


class TestDeveloper(TestCase):
    def test_developer(self):
        result = developer("8280508308326756579", lang="en", country="us")

        self.assertDictEqual(
            {
                "apps": [
                    "deezer.android.app",
                    "deezer.android.tv",
                    "com.deezer.analytics",
                ],
                "url": "https://play.google.com/store/apps/dev?id=8280508308326756579&hl=en&gl=us",
            },
            result,
        )

    def test_DeveloperNotFound(self):
        self.assertRaises(
            NotFoundError,
            lambda: developer("I_DO_NOT_EXIST", lang="en", country="us"),
        )
