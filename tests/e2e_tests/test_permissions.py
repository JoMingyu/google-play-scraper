from unittest import TestCase

from google_play_scraper.features.permissions import permissions


class TestPermission(TestCase):
    def test_reply_data_all_types(self):
        result = permissions("com.spotify.music", lang="en", country="us")

        self.assertDictEqual(
            {
                "Device ID & call information": ["read phone status and identity"],
                "Identity": ["add or remove accounts", "find accounts on the device"],
                "Storage": [
                    "modify or delete the contents of your USB storage",
                    "read the contents of your USB storage",
                ],
                "Phone": ["read phone status and identity"],
                "Microphone": ["record audio"],
                "Wi-Fi connection information": ["view Wi-Fi connections"],
                "Contacts": ["find accounts on the device"],
                "Camera": ["take pictures and videos"],
                "Photos/Media/Files": [
                    "modify or delete the contents of your USB storage",
                    "read the contents of your USB storage",
                ],
                "Other": [
                    "access Bluetooth settings",
                    "allow Wi-Fi Multicast reception",
                    "change network connectivity",
                    "change your audio settings",
                    "control Near Field Communication",
                    "control vibration",
                    "full network access",
                    "install shortcuts",
                    "pair with Bluetooth devices",
                    "prevent device from sleeping",
                    "run at startup",
                    "send sticky broadcast",
                    "use accounts on the device",
                    "view network connections",
                ],
                "Uncategorized": ["receive data from Internet"],
            },
            result,
        )

    def test_reply_data_only_other_type(self):
        result = permissions("example.matharithmetics", lang="en", country="us")

        self.assertDictEqual(
            {
                "Other": [
                    "control vibration",
                    "full network access",
                    "run at startup",
                    "view network connections",
                ]
            },
            result,
        )
