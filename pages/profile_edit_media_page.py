from __future__ import annotations
from typing import TYPE_CHECKING

from pages.base import WebPage, PageElement
if TYPE_CHECKING:
    from dto.user import User


class EditMediaPage(WebPage):

    _page_uri = "/settings/profile"

    back_button = PageElement(xpath="//div[@data-testid='app-bar-back']")
    apply_button = PageElement(xpath="//div[@data-testid='applyButton']")
