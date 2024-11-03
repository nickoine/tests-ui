from __future__ import annotations
from typing import TYPE_CHECKING

from pages.base import WebPage, PageElement, MultiPageElement
if TYPE_CHECKING:
    pass


class HomePage(WebPage):

    _page_uri = "/home"
    _title_contains = "Home / World"

    tweet = None
    tweet_form = PageElement(xpath="//div[@data-testid='tweetTextarea_0']")
    create_tweet = PageElement(xpath="//div[@data-testid='tweetButtonInline']")
    tweets = MultiPageElement(xpath="//article[@data-testid='tweet']")

    ####################
    # Left navbar links
    ####################
    twitter_logo_button = PageElement(link_text="/home")
    home_button = PageElement(xpath="//a[@data - testid='data-testid = AppTabBar_Home_Link']")
    explore_button = PageElement(xpath="//a[@data - testid='AppTabBar_Explore_Link']")
    notifications_button = PageElement(xpath="//a[@data - testid='AppTabBar_Notifications_Link']")
    messages_button = PageElement(xpath="//a[@data - testid='AppTabBar_DirectMessage_Link']")
    bookmarks_button = PageElement(link_text="/i/bookmarks")
    # lists_button = PageElement(link_text=f"/{existing_user.username}/lists")
    profile_button = PageElement(xpath="//a[@data-testid='AppTabBar_Profile_Link']")
    more_button = PageElement(xpath="//div[@data - testid='AppTabBar_More_Menu']")
    tweet_button = PageElement(xpath="//a[@data - testid='AppTabBar_Profile_Link']")

    account_menu_button = PageElement(xpath="//div[@data-testid='SideNav_AccountSwitcher_Button']")
    logout_button = PageElement(xpath="//a[@data-testid='AccountSwitcher_Logout_Button']")

    ####################
    # Right navbar links
    ####################
    sidebar_column = PageElement(xpath='//div[@data-testid="sidebarColumn"]')
    follow_button = PageElement(xpath='//div[contains(@data-testid, "-follow")]', context=True)
    who_to_follow = MultiPageElement(
        xpath='//aside[@role="complementary"]/div[2]/*[@data-testid="UserCell"]'
    )

    def is_tweet_exist(self, tweet_text: str) -> bool:
        self.tweet = PageElement(context=self.driver, xpath=f"//span[text()='{tweet_text}']")
        return bool(self.tweet.find(context=self.driver))

    def follow_suggested(self):
        """Get user follow-id and follow this user"""
        follow_id = set()
        for user_cell in self.who_to_follow:
            follow_id.add(self.follow_button(user_cell).get_attribute("data-testid"))
            self.follow_button(user_cell).click()
        # return [_id.strip("--follow") for _id in follow_id]
