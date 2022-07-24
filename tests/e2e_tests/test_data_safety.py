from unittest import TestCase

from google_play_scraper.features.data_safety import data_safety


class TestDataSafety(TestCase):
    def test_data_safety_complex(self):
        result = data_safety("com.spotify.music", lang="en", country="us")

        self.assertDictEqual(
            {
                "dataCollected": {
                    "Location": [
                        {
                            "name": "Approximate location",
                            "optional": False,
                            "usage": "App functionality, Analytics, Advertising or marketing, Fraud prevention, security, and compliance, Personalization",
                        }
                    ],
                    "Personal info": [
                        {
                            "name": "Email address",
                            "optional": False,
                            "usage": "App functionality, Developer communications, Advertising or marketing, Fraud prevention, security, and compliance, Account management",
                        },
                        {
                            "name": "User IDs",
                            "optional": False,
                            "usage": "App functionality, Analytics, Developer communications, Fraud prevention, security, and compliance, Account management",
                        },
                        {
                            "name": "Address",
                            "optional": True,
                            "usage": "App functionality, Fraud prevention, security, and compliance, Account management",
                        },
                        {
                            "name": "Phone number",
                            "optional": True,
                            "usage": "App functionality, Developer communications, Fraud prevention, security, and compliance, Account management",
                        },
                        {
                            "name": "Other info",
                            "optional": False,
                            "usage": "App functionality, Analytics, Advertising or marketing, Personalization, Account management",
                        },
                    ],
                    "Financial info": [
                        {
                            "name": "Purchase history",
                            "optional": True,
                            "usage": "App functionality, Analytics, Fraud prevention, security, and compliance",
                        }
                    ],
                    "Photos and videos": [
                        {
                            "name": "Photos",
                            "optional": True,
                            "usage": "App functionality, Fraud prevention, security, and compliance",
                        }
                    ],
                    "Audio": [
                        {
                            "name": "Voice or sound recordings",
                            "optional": True,
                            "usage": "App functionality, Fraud prevention, security, and compliance",
                        }
                    ],
                    "Contacts": [
                        {
                            "name": "Contacts",
                            "optional": True,
                            "usage": "App functionality, Fraud prevention, security, and compliance, Personalization",
                        }
                    ],
                    "App activity": [
                        {
                            "name": "App interactions",
                            "optional": False,
                            "usage": "App functionality, Analytics, Developer communications, Advertising or marketing, Fraud prevention, security, and compliance, Personalization",
                        },
                        {
                            "name": "In-app search history",
                            "optional": False,
                            "usage": "App functionality, Analytics, Fraud prevention, security, and compliance, Personalization",
                        },
                        {
                            "name": "Installed apps",
                            "optional": False,
                            "usage": "App functionality, Analytics, Fraud prevention, security, and compliance, Personalization, Account management",
                        },
                        {
                            "name": "Other user-generated content",
                            "optional": True,
                            "usage": "App functionality, Fraud prevention, security, and compliance, Personalization",
                        },
                        {
                            "name": "Other actions",
                            "optional": True,
                            "usage": "App functionality, Analytics, Advertising or marketing, Fraud prevention, security, and compliance, Personalization",
                        },
                    ],
                    "App info and performance": [
                        {
                            "name": "Crash logs",
                            "optional": False,
                            "usage": "Analytics, Fraud prevention, security, and compliance",
                        },
                        {
                            "name": "Diagnostics",
                            "optional": False,
                            "usage": "App functionality, Analytics, Fraud prevention, security, and compliance",
                        },
                        {
                            "name": "Other app performance data",
                            "optional": False,
                            "usage": "Analytics, Fraud prevention, security, and compliance",
                        },
                    ],
                    "Device or other IDs": [
                        {
                            "name": "Device or other IDs",
                            "optional": False,
                            "usage": "App functionality, Analytics, Developer communications, Advertising or marketing, Fraud prevention, security, and compliance, Personalization",
                        }
                    ],
                },
                "dataShared": {
                    "Location": [
                        {
                            "name": "Approximate location",
                            "optional": False,
                            "usage": "Analytics, Advertising or marketing",
                        }
                    ],
                    "Personal info": [
                        {"name": "Other info", "optional": False, "usage": "Analytics"}
                    ],
                    "Device or other IDs": [
                        {
                            "name": "Device or other IDs",
                            "optional": False,
                            "usage": "Advertising or marketing",
                        }
                    ],
                },
                "securityPractices": [
                    {
                        "name": "Data is encrypted in transit",
                        "description": "Your data is transferred over a secure connection",
                    },
                    {
                        "name": "You can request that data be deleted",
                        "description": "The developer provides a way for you to request that your data be deleted",
                    },
                ],
                "appId": "com.spotify.music",
                "url": "https://play.google.com/store/apps/datasafety?id=com.spotify.music&hl=en&gl=us",
            },
            result,
        )

    def test_data_safety_simple(self):
        result = data_safety("com.mattermost.rn", lang="en", country="us")

        self.assertDictEqual(
            {
                "dataCollected": {
                    "Personal info": [
                        {"name": "User IDs", "optional": True, "usage": "Analytics"}
                    ]
                },
                "dataShared": {},
                "securityPractices": [
                    {
                        "name": "Data is encrypted in transit",
                        "description": "Your data is transferred over a secure connection",
                    },
                    {
                        "name": "Data can’t be deleted",
                        "description": "The developer doesn’t provide a way for you to request that your data be deleted",
                    },
                ],
                "appId": "com.mattermost.rn",
                "url": "https://play.google.com/store/apps/datasafety?id=com.mattermost.rn&hl=en&gl=us",
            },
            result,
        )
