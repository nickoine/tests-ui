from pages import HomePage
from tests.base_test import BaseTest


class TestLogin(BaseTest):

    def test_login_as_existing_user_by_username(self) -> None:

        # GIVEN
        home_page = HomePage(self.driver)

        # WHEN login as existing user in conftest.py and wait until redirected to the home page

        # THEN
        home_page.wait_title_contains()
        # Check that user auth_token cookie exist.
        assert bool(self.driver.get_cookie("auth_token"))
