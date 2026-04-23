import pytest
import re
import random
from string import ascii_lowercase
from google_play_scraper.exceptions import NotFoundError
from google_play_scraper.features.data_safety import data_safety


class TestDataSafety:
    VALID_CATEGORIES = {
        "Location",
        "Personal info",
        "Financial info",
        "Health and fitness",
        "Messages",
        "Photos and videos",
        "Audio",
        "Files and docs",
        "Calendar",
        "Contacts",
        "App activity",
        "Web browsing",
        "App info and performance",
        "Device or other IDs",
    }

    VALID_PURPOSES = {
        "App functionality",
        "Analytics",
        "Developer communications",
        "Advertising or marketing",
        "Fraud prevention, security, and compliance",
        "Personalization",
        "Account management",
    }

    VALID_PRACTICES = {
        "Data is encrypted in transit",
        "You can request that data be deleted",
        "Data is encrypted at rest",
        "Third parties share data with app",
        "Data may be shared with third parties",
        "Users can control data sharing",
        "Data is not shared with third parties",
        "Data is shared with service providers",
        "Committed to follow the Play Families Policy",
        "Independent security review",
        "Data isn’t encrypted",
        "Data can’t be deleted",
    }

    def _assert_data(self, item: dict) -> None:
        assert isinstance(item, dict)
        assert "category" in item
        assert "items" in item
        assert isinstance(item["items"], list)
        # Validate category is from valid set
        assert (
            item["category"] in self.VALID_CATEGORIES
        ), f"Invalid category '{item['category']}'"

        for sub_item in item["items"]:
            assert "data" in sub_item
            assert "optional" in sub_item
            assert isinstance(sub_item["optional"], bool)
            assert "purpose" in sub_item
            # Validate purpose is from valid set
            purposes = "|".join(self.VALID_PURPOSES)
            pattern = r"^(" + purposes + r")(,\s(" + purposes + r"))*$"
            assert re.match(
                pattern, sub_item["purpose"]
            ), f"Invalid purpose '{sub_item['purpose']}'"

    android_apps = [
        "com.instagram.android",
        "com.zhiliaoapp.musically",
        "com.facebook.katana",
        "com.whatsapp",
        "com.whatsapp.w4b",
        "com.lemon.lvoverseas",
        "com.google.android.youtube",
        "com.google.android.gm",
        "com.google.android.apps.maps",
        "com.google.android.apps.photos",
        "com.google.android.googlequicksearchbox",
        "com.android.chrome",
        "com.snapchat.android",
        "com.microsoft.teams",
        "com.microsoft.office.outlook",
        "com.microsoft.skydrive",
        "com.spotify.music",
        "com.netflix.mediaclient",
        "com.amazon.mShop.android.shopping",
        "com.ebay.mobile",
        "com.disney.disneyplus",
        "com.twitter.android",
        "com.linkedin.android",
        "com.pinterest",
        "com.reddit.frontpage",
        "com.discord",
        "org.telegram.messenger",
        "com.viber.voip",
        "com.google.android.apps.tachyon",
        "com.ubercab",
        "com.ubercab.eats",
        "com.doordash.driverapp",
        "com.grubhub.android",
        "com.airbnb.android",
        "com.booking",
        "com.expedia.bookings",
        "com.tripadvisor.tripadvisor",
        "com.tinder",
        "com.badoo.mobile",
        "com.bumble.app",
        "com.okcupid.okcupid",
        "com.duolingo",
        "com.google.android.apps.translate",
        "com.microsoft.translator",
        "com.roblox.client",
        "com.king.candycrushsaga",
        "com.mojang.minecraftpe",
        "com.nianticlabs.pokemongo",
        "com.supercell.clashofclans",
        "com.supercell.clashroyale",
        "com.activision.callofduty.shooter",
        "com.garena.game.kgtw",
        "com.tencent.ig",
        "com.kiloo.subwaysurf",
        "com.playrix.gardenscapes",
        "com.playrix.homescapes",
        "com.moonactive.coinmaster",
        "com.shazam.android",
        "com.soundcloud.android",
        "com.pandora.android",
        "com.apple.android.music",
        "com.google.android.apps.subscriptions.red",
        "com.google.android.apps.walletnfcrel",
        "com.venmo",
        "com.squareup.cash",
        "com.paypal.android.p2pmobile",
        "com.chase.sig.android",
        "com.infonow.bofa",
        "com.wf.wellsfargomobile",
        "com.binance.dev",
        "com.coinbase.android",
        "com.robinhood.android",
        "com.etoro.openbook",
        "com.strava",
        "com.myfitnesspal.android",
        "com.calm.android",
        "com.adobe.reader",
        "com.adobe.lrmobile",
        "com.adobe.psmobile",
        "com.canva.editor",
        "com.picsart.studio",
        "com.dropbox.android",
        "com.box.android",
        "com.evernote",
        "com.microsoft.office.word",
        "com.microsoft.office.excel",
        "com.microsoft.office.powerpoint",
        "com.openai.chatgpt",
    ]

    def test_invalid_app_id_raises_NotFoundError(self):
        # Generate a random invalid app_id
        invalid_app_id = "com." + "".join(random.choices(ascii_lowercase, k=15))

        # Assert that NotFoundError is raised
        with pytest.raises(NotFoundError):
            data_safety(invalid_app_id, lang="en", country="us")

    @pytest.mark.parametrize("app_id", android_apps)
    def test_data_safety_structure(self, app_id: str) -> None:
        result = data_safety(app_id, lang="en", country="us")
        assert isinstance(result, dict)

        # Check that required top-level keys exist
        expected_keys = {
            "privacyPolicyUrl",
            "sharedData",
            "collectedData",
            "securityPractices",
        }
        assert (
            set(result.keys()) >= expected_keys
        ), f"Missing required keys for {app_id}. Got: {set(result.keys())}"

        # Validate privacyPolicyUrl
        assert isinstance(result["privacyPolicyUrl"], str)
        assert result["privacyPolicyUrl"].startswith("http")

        # Validate sharedData structure
        assert isinstance(result["sharedData"], list)
        for item in result["sharedData"]:
            assert isinstance(item, dict)
            self._assert_data(item)

        # Validate collectedData structure
        assert isinstance(result["collectedData"], list)
        for item in result["collectedData"]:
            assert isinstance(item, dict)
            self._assert_data(item)

        # Validate securityPractices structure
        assert isinstance(result["securityPractices"], list)
        for item in result["securityPractices"]:
            assert isinstance(item, dict)
            assert "practice" in item
            assert "description" in item
            assert isinstance(item["practice"], str)
            assert isinstance(item["description"], str)
            assert item["description"]
            # Validate practice is from valid set
            assert (
                item["practice"] in self.VALID_PRACTICES
            ), f"Invalid practice '{item['practice']}' for {app_id}"
