from datetime import datetime
from unittest import TestCase

from google_play_scraper import Sort
from google_play_scraper.features.reviews import reviews


class TestApp(TestCase):
    def test_e2e_scenario_1(self):
        result = reviews("com.mojang.minecraftpe", sort=Sort.NEWEST, count=500)

        self.assertEqual(500, len(result))

        review_created_version_contained_review_count = 0

        for r in result:
            self.assertTrue(r["userName"])
            self.assertTrue(r["userImage"])
            self.assertTrue(r["content"])
            self.assertTrue(r["score"] >= 1)
            self.assertTrue(r["thumbsUpCount"] >= 0)
            self.assertTrue(datetime(2019, 12, 1) < r["at"] < datetime(2021, 1, 1))
            # TODO change when 2020-12-30

            if r["reviewCreatedVersion"]:
                review_created_version_contained_review_count += 1

        self.assertTrue(review_created_version_contained_review_count > 100)

        last_review_at = result[0]["at"]
        well_sorted_review_count = 0

        for r in result[1:]:
            review_at = r["at"]

            if review_at <= last_review_at:
                well_sorted_review_count += 1

            last_review_at = review_at

        self.assertTrue(well_sorted_review_count > 490)

    def test_e2e_scenario_2(self):
        result = reviews("com.mojang.minecraftpe", sort=Sort.MOST_RELEVANT, count=30)

        self.assertEqual(30, len(result))

        review_count_has_thumbs_up_count_over_0 = 0

        for r in result:
            if 0 < r["thumbsUpCount"]:
                review_count_has_thumbs_up_count_over_0 += 1

        self.assertTrue(review_count_has_thumbs_up_count_over_0 > 25)

    def test_e2e_scenario_3(self):
        result = reviews("com.mojang.minecraftpe", sort=Sort.RATING, count=100)

        self.assertEqual(100, len(result))

        for r in result:
            self.assertEqual(5, r["score"])

    def test_e2e_scenario_4(self):
        for score in {1, 2, 3, 4, 5}:
            result = reviews(
                "com.mojang.minecraftpe",
                sort=Sort.NEWEST,
                count=300,
                filter_score_with=score,
            )

            self.assertEqual(score * 300, sum([r["score"] for r in result]))

    def test_e2e_scenario_5(self):
        """
        tests reply
        """

        result = reviews(
            "com.ekkorr.endlessfrontier",
            lang="ko",
            country="kr",
            sort=Sort.MOST_RELEVANT,
        )

        review_count_has_reply = 0

        for r in result:
            reply_content = r["replyContent"]
            replied_at = r["repliedAt"]

            if reply_content is not None:
                self.assertIn("안녕하세요", reply_content)
                self.assertIn("EKKORR", reply_content)
                self.assertIn("입니다", reply_content)
                self.assertIn("감사합니다", reply_content)

                self.assertTrue(len(reply_content) > 100)
                self.assertIsInstance(replied_at, datetime)
                self.assertTrue(
                    datetime(2018, 1, 1) < replied_at < datetime(2021, 1, 1)
                )
                # TODO change when 2020-12-30

                review_count_has_reply += 1

        self.assertTrue(review_count_has_reply > 50)

    def test_e2e_scenario_6(self):
        """
        tests length of results of first request is lower than specified count argument
        """

        result = reviews("com.ekkorr.endlessfrontier")

        self.assertTrue(len(result) < 100)
