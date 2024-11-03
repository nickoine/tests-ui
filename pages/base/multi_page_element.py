from __future__ import annotations
from typing import TYPE_CHECKING

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pages.base import PageElement

if TYPE_CHECKING:
    from typing import List


class MultiPageElement(PageElement):
    """ Like `PageElement` but returns multiple results.

        >>> from pages.base import WebPage, MultiPageElement
        >>> class MyPage(WebPage):
        >>>     all_table_rows = MultiPageElement(tag='tr')
        >>>     elem2 = PageElement(id_='foo')
        >>>     elem_with_context = PageElement(tag='tr', context=True)

    """
    def find(self, context: WebDriver) -> List[WebElement]:
        try:
            return context.find_elements(*self.locator)
        except NoSuchElementException:
            return []

    def __set__(self, instance, value: str) -> None:
        if self.has_context:
            raise ValueError("Sorry, the set descriptor doesn't support elements with context.")
        elements = self.__get__(instance, instance.__class__)
        if not elements:
            raise ValueError("Can't set value, no elements found")
        [elem.send_keys(value) for elem in elements]
