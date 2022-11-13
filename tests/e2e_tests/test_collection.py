from unittest import TestCase

from google_play_scraper import collection
from google_play_scraper.exceptions import NotFoundError


class TestCollection(TestCase):
    def test_collection(self):
        result = collection(
            "SkRqGGlQZGZtdlRLclM2Qkh0NEFDcDFyZ0E9PbICJwolCiFjb20uTXlJbmRpZUFwcC5GcmVlQ2xhc3NpY2FsUmFkaW8QBw%3D%3D:S:ANO1ljKtgcA",
            lang="en",
            country="us",
        )

        self.assertGreaterEqual(len(result["apps"]), 27)
        self.assertIn(
            result["url"],
            "https://play.google.com/store/apps/collection/cluster?gsr=SkRqGGlQZGZtdlRLclM2Qkh0NEFDcDFyZ0E9PbICJwolCiFjb20uTXlJbmRpZUFwcC5GcmVlQ2xhc3NpY2FsUmFkaW8QBw%3D%3D:S:ANO1ljKtgcA&hl=en&gl=us",
        )

    def test_DeveloperNotFound(self):
        self.assertRaises(
            NotFoundError,
            lambda: collection("I_DO_NOT_EXIST", lang="en", country="us"),
        )
