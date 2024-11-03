from __future__ import annotations
from typing import TYPE_CHECKING

from pages import FollowingPage
from pages import HomePage
from tests.base_test import BaseTest

if TYPE_CHECKING:
    from dto.user import User


class TestFollow(BaseTest):

    def test_follow_suggested_home_page(self, existing_user: User) -> None:

        # GIVEN
        home_page = HomePage(self.driver)
        following_page = FollowingPage(self.driver,
                                       page_uri=f"/{existing_user.username}/following",
                                       title_contains="People followed by")

        # WHEN
        home_page.wait_title_contains()
        assert bool(self.driver.get_cookie("auth_token"))

        # Unfollow all the followings as pre-condition
        following_page.open()
        following_page.wait_title_contains()
        following_page.unfollow_followings()

        # Follow 3 suggested users on a home page.
        home_page.open()
        home_page.wait_title_contains()
        home_page.follow_suggested()

        # THEN
        following_page.open()
        following_page.refresh()
        following_page.wait_title_contains()
        assert len(following_page.followings) == 3
