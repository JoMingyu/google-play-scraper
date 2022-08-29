from unittest import TestCase

from google_play_scraper.features.app import app


class TestApp(TestCase):
    def test_e2e_scenario_1(self):
        result = app("air.com.Tatsuki.CookieBreaker")

        self.assertEqual("Cookie Breaker!!!", result["title"])
        self.assertEqual("air.com.Tatsuki.CookieBreaker", result["appId"])
        self.assertEqual(
            "https://play.google.com/store/apps/details?id=air.com.Tatsuki.CookieBreaker&hl=en&gl=us",
            result["url"],
        )
        self.assertTrue(
            result["description"].startswith(
                "Cookie Breaker!!! Is an exhilarating game where you demolish cookies with heavy fire power. \r\n\r\nG"
            )
        )
        self.assertTrue(
            result["descriptionHTML"].startswith(
                "Cookie Breaker!!! Is an exhilarating game where you demolish cookies with heavy fire power. <br><br>G"
            )
        )
        self.assertEqual(
            "If you baked too many cookies…\nDestroy a bunch of them using fire power!",
            result["summary"],
        )
        self.assertEqual("100,000+", result["installs"])
        self.assertEqual(100000, result["minInstalls"])
        self.assertTrue(3.7 < result["score"] < 4.0)
        self.assertTrue(9500 <= result["ratings"])
        self.assertTrue(200 <= result["reviews"])
        self.assertTrue(result["reviews"] < result["ratings"])
        self.assertTrue(1500 <= result["histogram"][0])
        self.assertTrue(500 <= result["histogram"][1])
        self.assertTrue(400 <= result["histogram"][2])
        self.assertTrue(900 <= result["histogram"][3])
        self.assertTrue(5000 <= result["histogram"][4])
        # self.assertEqual(sum(result["histogram"]), result["ratings"])
        self.assertEqual(0, result["price"])
        self.assertTrue(result["free"])
        self.assertEqual("USD", result["currency"])
        self.assertTrue(result["offersIAP"])
        self.assertEqual("$0.99 - $2.99 per item", result["inAppProductPrice"])
        # self.assertEqual("Varies", result["androidVersion"])
        # self.assertEqual("Varies with device", result["androidVersionText"])
        self.assertEqual("Tatsuki", result["developer"])
        self.assertEqual("Tatsuki", result["developerId"])
        self.assertEqual("sskttk.android@gmail.com", result["developerEmail"])
        self.assertEqual("https://sskttk-app.com/", result["developerWebsite"])
        self.assertEqual(
            "Osaka-shi Chuo-ku Minamisenba 4-10-5", result["developerAddress"]
        )
        self.assertEqual("https://sskttk-app.com/?page_id=223", result["privacyPolicy"])
        # self.assertEqual("8524055825995721370", result["developerInternalID"])
        self.assertEqual("Simulation", result["genre"])
        self.assertEqual("GAME_SIMULATION", result["genreId"])
        self.assertEqual(
            "https://play-lh.googleusercontent.com/5nPD6fyJaa-EDLHdlBd9UsaAV8KkfrYvLB956eQsvIGNBWUrPeouYw8aa7kbCbY--6E",
            result["icon"],
        )
        self.assertEqual(
            "https://play-lh.googleusercontent.com/HVaR15hCrhTFeouDgocBaxJViXHA7TQ_sQfAHmb_zPs54CZQqo3Xgn78NgdrgnrnwTE",
            result["headerImage"],
        )
        self.assertTrue(result["screenshots"])
        for screenshot_url in result["screenshots"]:
            self.assertTrue(
                screenshot_url.startswith("https://play-lh.googleusercontent.com/")
            )

        self.assertIsNone(result["video"])
        self.assertIsNone(result["videoImage"])
        self.assertEqual("Everyone 10+", result["contentRating"])
        self.assertEqual("Fantasy Violence", result["contentRatingDescription"])
        self.assertTrue(result["adSupported"])
        self.assertTrue(result["containsAds"])
        self.assertEqual("Jan 7, 2014", result["released"])
        self.assertEqual(1636693903, result["updated"])
        self.assertEqual("Varies with device", result["version"])
        self.assertEqual(
            ("- Supports the newest devices."), result["recentChanges"],
        )
        self.assertEqual(
            "- Supports the newest devices.", result["recentChangesHTML"],
        )
        self.assertTrue(result["comments"])
        self.assertTrue(result["similarApps"])
        self.assertTrue(result["moreByDeveloper"])

    def test_e2e_scenario_2(self):
        """
        Testing for privacyPolicy, false value of adSupported, containsAds, offersIAP
        that excluded from scenario 1
        """
        res = app("com.google.android.calendar")

        self.assertEqual("http://www.google.com/policies/privacy", res["privacyPolicy"])
        self.assertFalse(res["adSupported"])
        self.assertFalse(res["containsAds"])
        self.assertFalse(res["offersIAP"])

    def test_e2e_scenario_3(self):
        """
        Testing for video, videoImage that excluded from scenario 1~2
        """
        res = app("com.sgn.pandapop.gp")

        self.assertEqual(
            "https://www.youtube.com/embed/lzthjLXbZr0?ps=play&vq=large&rel=0&autohide=1&showinfo=0",
            res["video"],
        )
        self.assertEqual(
            "https://play-lh.googleusercontent.com/spi_c6YT_E2yC4QwPC8oQpBGLyu2gTGj1BAvVhLDQJtRzGkR30kzmdKkajcCDDXrXsvS",
            res["videoImage"],
        )

    def test_e2e_scenario_4(self):
        """
        Testing for free, price that excluded from scenario 1~4
        """
        res = app("com.simplemobiletools.gallery.pro")

        self.assertFalse(res["free"])
        self.assertEqual(0.99, res["price"])

        # TODO free app / non free app 구분

    def test_e2e_scenario_5(self):
        """
        Testing for free, offersIAP, inAppProductPrice of free app
        """

        res = app("com.nhn.android.search")

        self.assertTrue(res["free"])
        self.assertFalse(res["offersIAP"])
        self.assertFalse(res["inAppProductPrice"])

        # TODO IAP, inAppProductPrice가 유효한 값인 경우에 대한 테스트
