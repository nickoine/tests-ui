from __future__ import annotations
from typing import TYPE_CHECKING

from pages.base import WebPage, PageElement
if TYPE_CHECKING:
    from dto.user import User


class EditProfilePage(WebPage):

    _page_uri = "/settings/profile"

    profile_save_button = PageElement(xpath="//div[@data-testid = 'Profile_Save_Button']")
    profile_close_button = PageElement(xpath="//div[@data - testid = 'app-bar-close']")

    background_form = PageElement(xpath="//div[1]/div/div/div[3]/div/input[@data-testid = 'fileInput']")
    avatar_form = PageElement(xpath="//div[2]/div/div/div[3]/div/input[@data-testid = 'fileInput']")
    name_form = PageElement(xpath="//input[@name='displayName']")
    bio_form = PageElement(xpath="//textarea[@name='description']")
    location_form = PageElement(xpath="//input[@name='location']")
    website_form = PageElement(xpath="//input[@name='url']")
    birth_date_edit_button = PageElement(xpath="//div[@data - testid = 'ProfileBirthdate']")
    switch_to_professional_button = PageElement(
        xpath="//a[@data - testid = 'ProfessionalButton_Switch_To_Professional']"
    )
