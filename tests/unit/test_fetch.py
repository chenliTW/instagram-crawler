from datetime import datetime
from unittest import TestCase, mock
from inscrawler.fetch import fetch_datetime, fetch_hashtags, fetch_mentions


class TestFetchMentions(TestCase):

    @mock.patch("inscrawler.fetch.settings")
    def test_fetch_mentions(self, mock_settings):
        mock_settings.fetch_mentions = True

        post = {}
        fetch_mentions("""
            This is my new robot, called @inscrawler
        """, post)

        self.assertIn("mentions", post)
        self.assertIn("inscrawler", post["mentions"])

    @mock.patch("inscrawler.fetch.settings")
    def test_fetch_mentions_if_not_enabled_by_settings(self, mock_settings):
        mock_settings.fetch_mentions = False

        post = {}
        fetch_mentions("""
            This is my new robot, called @inscrawler
        """, post)

        self.assertNotIn("mentions", post)


class TestFetchHashtags(TestCase):

    @mock.patch("inscrawler.fetch.settings")
    def test_fetch_hashtags(self, mock_settings):
        mock_settings.fetch_hashtags = True

        post = {}
        fetch_hashtags("""
            This is my new robot, called #inscrawler
        """, post)

        self.assertIn("hashtags", post)
        self.assertIn("inscrawler", post["hashtags"])

    @mock.patch("inscrawler.fetch.settings")
    def test_fetch_hashtags_if_not_enabled_by_settings(self, mock_settings):
        mock_settings.fetch_hashtags = False

        post = {}
        fetch_hashtags("""
            This is my new robot, called #inscrawler
        """, post)

        self.assertNotIn("hashtags", post)


class TestFetchDatetime(TestCase):

    def test_fetch_datetime(self):
        mock_browser = mock.Mock()
        mock_browser.find_one.return_value \
            .get_attribute.return_value = datetime.now()

        post = {}
        fetch_datetime(mock_browser, post)

        self.assertIn("datetime", post)
