from __future__ import annotations
from typing import TYPE_CHECKING

from pages import FollowingPage
from pages import HomePage
from tests.base_test import BaseTest

if TYPE_CHECKING:
    from dto.user import User


class TestUnfollow(BaseTest):

    def test_unfollow_followings(self, existing_user: User) -> None:

        # GIVEN
        home_page = HomePage(self.driver)
        following_page = FollowingPage(self.driver,
                                       page_uri=f"/{existing_user.username}/following",
                                       title_contains="People followed by")

        # WHEN
        home_page.wait_title_contains()
        assert bool(self.driver.get_cookie("auth_token"))

        # THEN
        following_page.open()
        following_page.wait_title_contains()
        following_page.unfollow_followings()
        following_page.refresh()
        assert len(following_page.followings) == 0
