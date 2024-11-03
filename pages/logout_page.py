from __future__ import annotations

from pages.base import WebPage, PageElement


class LogoutPage(WebPage):

    _page_uri = "/logout"

    logout_button = PageElement(xpath='//div[@data-testid="confirmationSheetConfirm"]')
