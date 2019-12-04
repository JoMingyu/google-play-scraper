from contextlib import contextmanager
from pprint import pprint
from unittest import TestCase
from unittest.mock import patch, MagicMock

import validators

from google_play_scraper import app


class TestApp(TestCase):
    @contextmanager
    def _mock_urlopen(self, mock_file_path):
        with patch("google_play_scraper.urlopen") as mock_urlopen:
            cm = MagicMock()

            with open(mock_file_path, encoding="UTF-8") as f:
                cm.read.return_value = f.read().encode("UTF-8")
                mock_urlopen.return_value = cm

            yield

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

    def test_issue_16(self):
        """
        https://github.com/JoMingyu/google-play-scraper/issues/16

        - ’com.trixi.bike.stunts.driving‘ cannot be grabbed
        - AttributeError: 'NoneType' object has no attribute 'replace' on unescape_text function
        - Some fields do not match the value, but they are not processed.
        """

        with self._mock_urlopen("mocks/com.trixi.bike.stunts.driving.html"):
            result = app("com.trixi.bike.stunts.driving")

            self.assertDictEqual(
                {
                    "title": "Bike Games: Bike Racing Games",
                    "appId": "com.trixi.bike.stunts.driving",
                    "url": "https://play.google.com/store/apps/details?id=com.trixi.bike.stunts.driving&hl=en&gl=us",
                    "description": "Do you like stunt bike games? Play bike games: bike racing games to make stunt on bike and cross all obstacles in new games 2019: free games make dangerous stunts on new bike and show impressive experience by playing stunt bike racing all games. Stunt on thrilling stunt ramp in bike stunt games: bike rider. Make extremely fantastic stunt in bike games: bike racing games to win trophy.\r\n\r\nNew games 2019: free games is one of the best bike stunt games you will ever see. Enjoy street racing with new bikes, bikes are available in stunt scooter games: bike games 2019. Slow down or reduce your bike speed, don't over speed motor bike because your level will be failed in bike stunt games: bike rider and you will slip on the narrow tracks of stunt scooter bike game and you may fall from the sky tracks into the deep ocean while playing bike games 3d: stunt games. You have to race your bike in city and make real stunts in stunt bike racing game just like bike stunts game in bike driving games: motorcycle games you will race your bike, reach the destination point successfully and jump carefully to complete the levels in motorcycle games: bike parking games. To make you expert bike rider, bike driving games: motorcycle games provides multiple levels in thrilling environment.\r\n\r\nStunt scooter spiele: new games 2019 is one of the stunt racing game in difficult stunt area with bike offline: stunt of bike game. Stunt spiele new bike games 2019 3d control is design by very unique great controls. Race on a super bike in an action-packed motorbike stunts game. Be a rooftop stunt bike driver! Drive your top stunt bike and speed through some challenging levels of bike jumping game: bike stunt 2019 like in rooftop games. Each level of new biker game: new bike games 2019 is thrilling than the previous level of bike simulator stunt bike games. Perform some serious crazy stunts in stunt bike games freestyle and race to the finish line really fast to win stunt games motorcycle!\r\n\r\nCome and play new stunt bike game: bike jump games on a rooftop bike. In new stunt game 2019: free bike games you will feel like a real stuntman in bike games: bike racing games! Experience the fastest 3d stunts racing actions on stunt driving games: stunt jumping games. Stunt motorcycle games: bike wali game allows you to choose from many exciting bikes. Each new bike is more powerful and thrilling to ride new games 2019: free games. Complete various challenging missions to earn game coins & cash. Cash can be used to unlock new bikes of bike driving games: bike stunt games to excel in bike wala game: bike ki game.\r\nBecome an extra ordinary bike stunt driver by playing stunt bike freestyle games, show your tricky stunt driving skills in bike stunt games: bike rider! Bike and scooter games is filled with free style stunts on tricky tracks. Utilize your free time to entertain yourself to complete all levels of bike jump game: stunt scooter games.\r\nMultiple tracks are arranged according bike jumping games: stunt racing games scenarios which carry multiple bike stunt levels from easy bike trials to difficult and impossible levels. So, are you bike stunt racer?? Let’s ﬁnd out what you want, use your motorcycle driving tricks and ﬁnish all challenges of bike wala game: bike ki game.\r\n\r\nFeatures:\r\n-- stunning 3d graphics of stunt bike racing all games\r\n-- realistic environment of stunt bike racing game\r\n-- different game modes in stunt scooter bike game\r\n-- superb bikes to choose from\r\n-- smooth and realistic bike handling of bike games 3d: stunt games\r\n\r\nMotorcycle games: bike parking games is best physics-based bike, most close to the realistic physical effects on your bike wheels. So, download bike driving games: bike stunt games for free.",
                    "descriptionHTML": "Do you like stunt bike games? Play bike games: bike racing games to make stunt on bike and cross all obstacles in new games 2019: free games make dangerous stunts on new bike and show impressive experience by playing stunt bike racing all games. Stunt on thrilling stunt ramp in bike stunt games: bike rider. Make extremely fantastic stunt in bike games: bike racing games to win trophy.<br><br>New games 2019: free games is one of the best bike stunt games you will ever see. Enjoy street racing with new bikes, bikes are available in stunt scooter games: bike games 2019. Slow down or reduce your bike speed, don&#39;t over speed motor bike because your level will be failed in bike stunt games: bike rider and you will slip on the narrow tracks of stunt scooter bike game and you may fall from the sky tracks into the deep ocean while playing bike games 3d: stunt games. You have to race your bike in city and make real stunts in stunt bike racing game just like bike stunts game in bike driving games: motorcycle games you will race your bike, reach the destination point successfully and jump carefully to complete the levels in motorcycle games: bike parking games. To make you expert bike rider, bike driving games: motorcycle games provides multiple levels in thrilling environment.<br><br>Stunt scooter spiele: new games 2019 is one of the stunt racing game in difficult stunt area with bike offline: stunt of bike game. Stunt spiele new bike games 2019 3d control is design by very unique great controls. Race on a super bike in an action-packed motorbike stunts game. Be a rooftop stunt bike driver! Drive your top stunt bike and speed through some challenging levels of bike jumping game: bike stunt 2019 like in rooftop games. Each level of new biker game: new bike games 2019 is thrilling than the previous level of bike simulator stunt bike games. Perform some serious crazy stunts in stunt bike games freestyle and race to the finish line really fast to win stunt games motorcycle!<br><br>Come and play new stunt bike game: bike jump games on a rooftop bike. In new stunt game 2019: free bike games you will feel like a real stuntman in bike games: bike racing games! Experience the fastest 3d stunts racing actions on stunt driving games: stunt jumping games. Stunt motorcycle games: bike wali game allows you to choose from many exciting bikes. Each new bike is more powerful and thrilling to ride new games 2019: free games. Complete various challenging missions to earn game coins &amp; cash. Cash can be used to unlock new bikes of bike driving games: bike stunt games to excel in bike wala game: bike ki game.<br>Become an extra ordinary bike stunt driver by playing stunt bike freestyle games, show your tricky stunt driving skills in bike stunt games: bike rider! Bike and scooter games is filled with free style stunts on tricky tracks. Utilize your free time to entertain yourself to complete all levels of bike jump game: stunt scooter games.<br>Multiple tracks are arranged according bike jumping games: stunt racing games scenarios which carry multiple bike stunt levels from easy bike trials to difficult and impossible levels. So, are you bike stunt racer?? Let’s ﬁnd out what you want, use your motorcycle driving tricks and ﬁnish all challenges of bike wala game: bike ki game.<br><br>Features:<br>-- stunning 3d graphics of stunt bike racing all games<br>-- realistic environment of stunt bike racing game<br>-- different game modes in stunt scooter bike game<br>-- superb bikes to choose from<br>-- smooth and realistic bike handling of bike games 3d: stunt games<br><br>Motorcycle games: bike parking games is best physics-based bike, most close to the realistic physical effects on your bike wheels. So, download bike driving games: bike stunt games for free.",
                    "summary": "Only 1% can complete all levels of bike stunt game.",
                    "summaryHTML": "Only 1% can complete all levels of bike stunt game.",
                    "installs": "1,000+",
                    "minInstalls": 1000,
                    "score": 0.0,
                    "ratings": 0,
                    "reviews": 0,
                    "histogram": None,
                    "price": 0,
                    "free": True,
                    "currency": "USD",
                    "offersIAP": None,
                    "size": "20M",
                    "androidVersion": "4.1",
                    "androidVersionText": "4.1 and up",
                    "developer": "Trixi Craft",
                    "developerId": "Trixi+Craft",
                    "developerEmail": "trixidrey@gmail.com",
                    "developerWebsite": None,
                    "developerAddress": None,
                    "privacyPolicy": "https://sites.google.com/view/trixidrey/home",
                    "developerInternalID": "8542601964486645528",
                    "genre": "Simulation",
                    "genreId": "GAME_SIMULATION",
                    "familyGenre": None,
                    "familyGenreId": None,
                    "icon": "https://lh3.googleusercontent.com/5oMzAueTwPeqTxjg7diWoAZrqPNmysF4oz9xu7KYQKuOPqCr06c4o9reuYMEGCk6XVp5",
                    "headerImage": "https://lh3.googleusercontent.com/BIUuZ4RR60MQ4u7TB2v1KLQB4wz21HEaOniC2YjIRno1JX1rxtjpanyBZfSfjFP5NWK3",
                    "screenshots": [
                        "https://lh3.googleusercontent.com/zDw7BfKj45XsDP_YQdr8dZ-tG5F8wDzVby6YMseWjCUjpxFWrts_zw3NnkvjqskUVFf7",
                        "https://lh3.googleusercontent.com/xFfk1FqyvJPCy_IOtBpXrFHugpLmvIpwOUXOhKIOJPm0vA_V7VHCpn0bf8oL_67MCfw",
                        "https://lh3.googleusercontent.com/EtL6iR6AMEBZSDL4lsteWnMEa7qOm6IWey0j6uKAGMPWT0XE5crFKSfecJ1nTCiFr9rI",
                        "https://lh3.googleusercontent.com/lDReaf3FKokOK0EI8S3IIKsKq56SknQmHMaj-DkkGdzuMBqFYY5E8Po3Ixhs8QzeEMw",
                        "https://lh3.googleusercontent.com/cko2LxrBoaVRZTJYRdGSjW7l23i08_gb0MA8GWNHpIK8GFjyusTrpwucQHCOe60QGA",
                        "https://lh3.googleusercontent.com/TH8DzNzU4TTT-ulE8v7bPApC15ABz8moNPsh7ucWHgM8TNfQpd1wuE_wUjSgR3d3cA",
                        "https://lh3.googleusercontent.com/fG_o6yy-uzv1kQNCs2NEybjJpASwYk34c46AmJCxECvY4jQXHRFwZGm9gSx283UCgqs",
                        "https://lh3.googleusercontent.com/xt0qYy2zApGPhLeCTcImfm5e4IX7PO8oCxvhduNcu3ZFJ3-72CrGsn62AFzjwOxlf-k",
                        "https://lh3.googleusercontent.com/6hJODGPUin6npDYXUbyJK0cCKOPXIfRA9YBV-nbviD6rYrr0I6kS1IpCvZ9n1lcMndw",
                    ],
                    "video": None,
                    "videoImage": None,
                    "contentRating": "All ages",
                    "contentRatingDescription": None,
                    "adSupported": True,
                    "released": "Jun 25, 2019",
                    "updated": 1562692759,
                    "version": "1.0",
                    "recentChanges": None,
                    "recentChangesHTML": None,
                    "comments": [],
                },
                result,
            )

    def test_issue_17(self):
        """
        https://github.com/JoMingyu/google-play-scraper/issues/17

        - Try fetching com.instagram.igtv
        - occurs `AttributeError: 'NoneType' object has no attribute 'replace'`
        """

        with self._mock_urlopen("mocks/com.instagram.igtv.html"):
            result = app("com.instagram.igtv")

            self.assertDictEqual(
                {
                    "title": "IGTV",
                    "appId": "com.instagram.igtv",
                    "url": "https://play.google.com/store/apps/details?id=com.instagram.igtv&hl=en&gl=us",
                    "description": "IGTV now supports landscape video in addition to vertical.\r\n\r\nWatch long-form, video from your favorite Instagram creators. \r\n\r\nIGTV is different from your typical video experience. It’s built for how you actually use your phone and not limited to one minute, which means you can see more of your favorite content.\r\n\r\nFEATURES\r\n\r\n* Download and sign in with your Instagram account. You can start watching videos right away. \r\n* Watch videos from creators you already follow and others you might like. \r\n* Browse other videos or search for a specific creator’s channel as you watch.\r\n* Like or comment on videos and send them to your friends in Direct. \r\n* Discover creators and follow them right from IGTV to see more of who they are on Instagram.",
                    "descriptionHTML": "IGTV now supports landscape video in addition to vertical.<br><br>Watch long-form, video from your favorite Instagram creators. <br><br>IGTV is different from your typical video experience. It’s built for how you actually use your phone and not limited to one minute, which means you can see more of your favorite content.<br><br>FEATURES<br><br>* Download and sign in with your Instagram account. You can start watching videos right away. <br>* Watch videos from creators you already follow and others you might like. <br>* Browse other videos or search for a specific creator’s channel as you watch.<br>* Like or comment on videos and send them to your friends in Direct. <br>* Discover creators and follow them right from IGTV to see more of who they are on Instagram.",
                    "summary": "Watch long-form, vertical video from your favorite Instagram creators.",
                    "summaryHTML": "Watch long-form, vertical video from your favorite Instagram creators.",
                    "installs": "1,000,000+",
                    "minInstalls": 1000000,
                    "score": 3.778658,
                    "ratings": 21628,
                    "reviews": 9152,
                    "histogram": [4756, 967, 1330, 1824, 12749],
                    "price": 0,
                    "free": True,
                    "currency": "USD",
                    "offersIAP": None,
                    "size": "Varies with device",
                    "androidVersion": "4.4",
                    "androidVersionText": "4.4 and up",
                    "developer": "Instagram",
                    "developerId": "Instagram",
                    "developerEmail": "android-support@instagram.com",
                    "developerWebsite": "http://help.instagram.com/",
                    "developerAddress": None,
                    "privacyPolicy": "http://instagram.com/legal/privacy/",
                    "developerInternalID": "4809448487316591555",
                    "genre": "Social",
                    "genreId": "SOCIAL",
                    "familyGenre": None,
                    "familyGenreId": None,
                    "icon": "https://lh3.googleusercontent.com/l1wB4ZsDDt4XGAw_EKQxPxLnG3a1qt38G-w5_SBS2XYhWYds5NY3ryzjDticPHd457A",
                    "headerImage": "https://lh3.googleusercontent.com/FcpbIYOvhElXRSsosRI_5I1eM31sFesHeXLEcFhdrplix2UpNW-7AMPusmK6YCj2vXPp",
                    "screenshots": [
                        "https://lh3.googleusercontent.com/lyzX1TuapLM9OdFs4bKlnmD8g8rm9z1xCM71wVsuYG6J9dvEk67OX8GpYxlgzOBUuhg",
                        "https://lh3.googleusercontent.com/lB9DqSYRkTyjoQNcphoDilu4UMNVbKaOBaIqiehOBlSVqDgS7rxD10I-t9L6JFVmu4E",
                        "https://lh3.googleusercontent.com/vW7rNCGM5h4sfqLacVuByw3xFNVIoe1j5B3GbywSaWZCAM7_ES3kGZp5eoMAI0Z8nmI",
                    ],
                    "video": None,
                    "videoImage": None,
                    "contentRating": "Rated for 12+",
                    "contentRatingDescription": "Parental Guidance Recommended",
                    "adSupported": None,
                    "released": "Jun 20, 2018",
                    "updated": 1574361155,
                    "version": "120.0.0.29.118",
                    "recentChanges": "The latest version contains bug fixes and performance improvements",
                    "recentChangesHTML": "The latest version contains bug fixes and performance improvements",
                    "comments": [],
                },
                result,
            )

    def test_issue_18(self):
        """
        https://github.com/JoMingyu/google-play-scraper/issues/18

        - it crashed when comment is empty
        - Occurs
            > "comments": ElementSpec(15, [0], lambda container: [item[4] for item in container]),
            > TypeError: 'NoneType' object is not iterable
        """

        # with self._mock_urlopen("mocks/com.instagram.igtv.html"):
        #     result = app("com.instagram.igtv")
