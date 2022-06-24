from unittest import TestCase

from google_play_scraper import collection
from google_play_scraper.exceptions import NotFoundError


class TestDeveloper(TestCase):
    def test_Developer(self):
        result = collection("SjpqGFhBMmIrNHYwRm90S1pKTFpXTzRINkE9PcICHQoZChVjb20uZGVlemVyLmF1ZGlvYm9va3MQBxgI:S:ANO1ljKeuFQ", lang="en", country="us")

        self.assertEqual(len(result['apps']), 41)
        self.assertEqual(result['url'], 'https://play.google.com/store/apps/collection/cluster?gsr=SjpqGFhBMmIrNHYwRm90S1pKTFpXTzRINkE9PcICHQoZChVjb20uZGVlemVyLmF1ZGlvYm9va3MQBxgI:S:ANO1ljKeuFQ&hl=en&gl=us')

    def test_DeveloperNotFound(self):
        self.assertRaises(
            NotFoundError,
            lambda: collection("I_DO_NOT_EXIST", lang="en", country="us"),
        )