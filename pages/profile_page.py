from __future__ import annotations
from pages.base import WebPage, PageElement


class ProfilePage(WebPage):

    edit_profile_button = PageElement(xpath="//a[@href='/settings/profile']")

    # Data used for assert check in tests. It needs full Xpath.
    user_first_last_name = PageElement(xpath="/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div[1]/div/div[1]/div/div/span[1]/span")
    user_bio = PageElement(xpath="/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div/div/div[3]/div/div[1]/span")
    user_location = PageElement(xpath="/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div/div/div[4]/div/span[1]/span/span")
    user_website = PageElement(xpath="/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div/div/div[4]/div/a/span")
