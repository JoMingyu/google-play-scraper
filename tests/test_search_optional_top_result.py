"""Regression coverage for a missing optional promoted search result."""
import importlib
import json
import unittest
from contextlib import ExitStack
from unittest.mock import patch
from types import SimpleNamespace

search_module = importlib.import_module("google_play_scraper.features.search")


class SearchOptionalTopResultTests(unittest.TestCase):
    def test_null_promoted_result_keeps_regular_results(self):
        # Google Play may return a null promoted-result slot for some locales.
        # The ordinary result list remains available at [22][0].
        first_section = [None] * 24
        first_section[23] = None
        first_section[22] = [[{"app_id": "com.example.first"}]]
        payload = [[None, [first_section]]]

        class AppIdSpec:
            def extract_content(self, item):
                return item["app_id"]

        with ExitStack() as stack:
            stack.enter_context(patch.object(search_module, "get", return_value="<html></html>"))
            stack.enter_context(patch.object(search_module.Regex, "SCRIPT", SimpleNamespace(findall=lambda _: ["script"])))
            stack.enter_context(patch.object(search_module.Regex, "KEY", SimpleNamespace(findall=lambda _: ["ds:4"])))
            stack.enter_context(patch.object(search_module.Regex, "VALUE", SimpleNamespace(findall=lambda _: [json.dumps(payload)])))
            stack.enter_context(patch.object(search_module.ElementSpecs, "SearchResult",
                         {"appId": AppIdSpec()}))
            stack.enter_context(patch.object(search_module.ElementSpecs, "SearchResultOnTop", {}))
            results = search_module.search(
                "bilancio familiare", country="it", lang="it", n_hits=50
            )

        self.assertEqual(results, [{"appId": "com.example.first"}])


if __name__ == "__main__":
    unittest.main()
