from datetime import datetime, timedelta
from unittest import TestCase
from unittest.mock import patch
from urllib.parse import urlparse

from google_play_scraper.features.permissions import permissions


class TestPermission(TestCase):

    def test_reply_data_all_types(self):
        result = permissions("com.spotify.music", lang="en", country="us")

        self.assertIn(('Other', 'run at startup'), result)
        self.assertIn(('Storage', 'modify or delete the contents of your USB storage'), result)
        self.assertIn(('Storage', 'read the contents of your USB storage'), result)
        self.assertIn(('Camera', 'take pictures and videos'), result)
        self.assertIn(('Photos/Media/Files', 'modify or delete the contents of your USB storage'), result)
        self.assertIn(('Photos/Media/Files', 'read the contents of your USB storage'), result)
        self.assertIn(('Device ID & call information', 'read phone status and identity'), result)
        self.assertIn(('Phone', 'read phone status and identity'), result)
        self.assertIn(('Contacts', 'find accounts on the device'), result)
        self.assertIn(('Microphone', 'record audio'), result)
        self.assertIn(('Identity', 'add or remove accounts'), result)
        self.assertIn(('Identity', 'find accounts on the device'), result)
        self.assertIn(('Wi-Fi connection information', 'view Wi-Fi connections'), result)
        self.assertIn(('Other', 'control vibration'), result)
        self.assertIn(('Other', 'full network access'), result)
        self.assertIn(('Other', 'change network connectivity'), result)
        self.assertIn(('Other', 'allow Wi-Fi Multicast reception'), result)
        self.assertIn(('Other', 'control Near Field Communication'), result)
        self.assertIn(('Other', 'change your audio settings'), result)
        self.assertIn(('Other', 'send sticky broadcast'), result)
        self.assertIn(('Other', 'access Bluetooth settings'), result)
        self.assertIn(('Other', 'use accounts on the device'), result)
        self.assertIn(('Other', 'install shortcuts'), result)
        self.assertIn(('Other', 'view network connections'), result)
        self.assertIn(('Other', 'pair with Bluetooth devices'), result)
        self.assertIn(('Other', 'prevent device from sleeping'), result)
        self.assertIn(('Other', 'run at startup'), result)
        self.assertIn(('Uncategorized', 'receive data from Internet'), result)

        self.assertEqual(len(result), 27)

    def test_reply_data_only_other_type(self):
        result = permissions("example.matharithmetics", lang="en", country="us")

        self.assertIn(('Other', 'full network access'), result)
        self.assertIn(('Other', 'run at startup'), result)
        self.assertIn(('Other', 'control vibration'), result)
        self.assertIn(('Other', 'view network connections'), result)
