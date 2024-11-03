from __future__ import annotations
from typing import TYPE_CHECKING
import pytest

from pages.base import WebPage, PageElement

if TYPE_CHECKING:
    from dto.user import User


class LoginPage(WebPage):

    _page_uri = "/i/flow/login"

    username_form = PageElement(xpath="//input[@autocomplete='username']")
    password_form = PageElement(xpath="//input[@autocomplete='current-password']")
    phone_form = PageElement(xpath="//input[@autocomplete='tel']")
    next_button = PageElement(xpath="//span[text()='Next']")
    login_button = PageElement(xpath="//span[text()='Log in']")
    suspicious_login = PageElement(xpath="//span[text()='Suspicious login prevented']")

    def login(self, user: User):
        # Set username and password forms.
        self.username_form = user.username
        self.next_button.click()
        self.password_form = user.password
        self.login_button.click()

        # Twitter will block access account when attempting to log in too many times.
        if self.suspicious_login:
            pytest.skip("Login test skipped due suspicious login prevented")

        # At last step twitter may ask you for a phone number. If so - set it.
        if self.phone_form:
            self.phone_form = user.phone_number
            self.next_button.click()
