from __future__ import annotations
from typing import TYPE_CHECKING

from pages.base import WebPage, PageElement, MultiPageElement
if TYPE_CHECKING:
    pass


class FollowingPage(WebPage):

    followings = MultiPageElement(xpath='//section//*[@data-testid="UserCell"]')
    unfollow_button = PageElement(xpath='//div[contains(@data-testid, "-unfollow")]', context=True)
    unfollow_confirm = PageElement(
        xpath='//div[contains(@data-testid, "confirmationSheetConfirm")]', context=True
    )
    unfollow_cancel = PageElement(
        xpath='//div[contains(@data-testid, "confirmationSheetCancel")]', context=True
    )

    user_cell = MultiPageElement(xpath='//div//*[@data-testid="UserCell"]')
    user_id = PageElement(xpath='//div[contains(@id, "id__")]', context=True)

    def unfollow_followings(self):
        for user_cell in self.followings:
            self.unfollow_button(user_cell)
            self.unfollow_button(user_cell).click()
            self.unfollow_confirm(user_cell).click()
