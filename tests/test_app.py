from unittest import TestCase

import validators

from google_play_scraper import app


class TestApp(TestCase):
    def test_happypath(self):
        result = app("com.sgn.pandapop.gp")

        self.assertEqual("com.sgn.pandapop.gp", result["appId"])
        self.assertEqual(
            "Panda Pop! Bubble Shooter Saga & Puzzle Adventure", result["title"]
        )
        self.assertEqual(
            "https://play.google.com/store/apps/details?id=com.sgn.pandapop.gp&hl=en&gl=us",
            result["url"],
        )
        validators.url(result["icon"])
