from pages import LogoutPage, MainPage, HomePage
from tests.base_test import BaseTest


class TestLogout(BaseTest):

    def test_logout(self) -> None:

        # GIVEN
        home_page = HomePage(self.driver)
        logout_page = LogoutPage(self.driver)
        main_page = MainPage(self.driver)

        # WHEN
        home_page.wait_title_contains()
        # Check that user auth_token cookie exist.
        assert bool(self.driver.get_cookie("auth_token"))

        # Logging out and wait until redirected to main page.
        home_page.account_menu_button.click()
        home_page.logout_button.click()
        logout_page.logout_button.click()

        # THEN
        main_page.wait_title_is()
        assert self.driver.get_cookie("auth_token") is None
