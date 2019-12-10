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

    def test_fetch_comments(self):
        self.assertTrue(len(app("com.nianticlabs.pokemongo")["comments"]) >= 1)

    def test_fetch_adSupported(self):
        self.assertIsNone(app("com.nianticlabs.pokemongo")["adSupported"])
        self.assertTrue(app("com.sgn.pandapop.gp")["adSupported"])

    def test_fetch_containsAds(self):
        self.assertFalse(app("com.nianticlabs.pokemongo")["containsAds"])
        self.assertTrue(app("com.sgn.pandapop.gp")["containsAds"])

    def test_fetch_offersIAP(self):
        self.assertTrue(app("com.nianticlabs.pokemongo")["offersIAP"])
        self.assertFalse(app("com.google.android.calendar")["offersIAP"])
