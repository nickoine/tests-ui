from pages.home_page import HomePage
from tests.base_test import BaseTest


class TestTweet(BaseTest):

    def test_post_tweet(self, faker) -> None:

        # GIVEN
        home_page = HomePage(self.driver)
        faker.random.seed()
        tweet_text = faker.text()

        # WHEN
        home_page.wait_title_contains()
        # Check that user auth_token cookie exist.
        assert bool(self.driver.get_cookie("auth_token"))

        home_page.tweet_form = tweet_text
        home_page.create_tweet.click()

        # THEN check tweet appears on the home page.
        assert len(home_page.tweets) != 0
        assert home_page.is_tweet_exist(tweet_text)
