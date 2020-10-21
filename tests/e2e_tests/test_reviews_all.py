from unittest import TestCase
from unittest.mock import patch

from google_play_scraper.features.reviews import reviews_all, reviews


class TestReviewsAll(TestCase):
    def test_request_once(self):
        with patch(
            "google_play_scraper.features.reviews.reviews", wraps=reviews
        ) as mock_reviews:
            result = reviews_all("co.kr.uaram.userdeliver_")
            self.assertEqual(1, mock_reviews.call_count)

        result_of_reviews, _ = reviews("co.kr.uaram.userdeliver_", count=10000)

        self.assertTrue(0 < len(result) < 10)
        self.assertEqual(len(result), len(result_of_reviews))

    def test_request_multiple_times(self):
        with patch(
            "google_play_scraper.features.reviews.reviews", wraps=reviews
        ) as mock_reviews:
            result = reviews_all("co.kr.uaram.userdeliver_", lang="ko", country="kr")
            self.assertEqual(3, mock_reviews.call_count)

        result_of_reviews, _ = reviews(
            "co.kr.uaram.userdeliver_", lang="ko", country="kr", count=10000
        )

        self.assertTrue(300 < len(result) < 500)
        self.assertEqual(len(result), len(result_of_reviews))

    def test_no_reviews(self):
        result = reviews_all("com.spotify.music", lang="sw", country="it")

        self.assertListEqual([], result)
