from __future__ import annotations
from typing import TYPE_CHECKING

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

if TYPE_CHECKING:
    from typing import Optional, Any, Union, List
    from selenium.webdriver.remote.webelement import WebElement
    from selenium.webdriver.remote.webdriver import WebDriver


# Map PageElement constructor arguments to web driver locator enums
_LOCATOR_MAP = {
    'css': By.CSS_SELECTOR,
    'id_': By.ID,
    'name': By.NAME,
    'xpath': By.XPATH,
    'link_text': By.LINK_TEXT,
    'partial_link_text': By.PARTIAL_LINK_TEXT,
    'tag_name': By.TAG_NAME,
    'class_name': By.CLASS_NAME
}


class PageElement:
    """ Page Element descriptor.

    :param css:    `str`
        Use this css locator
    :param id_:    `str`
        Use this element ID locator
    :param name:    `str`
        Use this element name locator
    :param xpath:    `str`
        Use this xpath locator
    :param link_text:    `str`
        Use this link text locator
    :param partial_link_text:    `str`
        Use this partial link text locator
    :param tag_name:    `str`
        Use this tag name locator
    :param class_name:    `str`
        Use this class locator

    :param context: `bool`
        This element is expected to be called with context

    Page Elements are used to access elements on a page. They are constructed
    using this factory method to specify the locator for the element.

        >>> from pages.base import WebPage, PageElement
        >>> class MyPage(WebPage):
        >>>     elem1 = PageElement(css='div.myclass')
        >>>     elem2 = PageElement(id_='foo')
        >>>     elem_with_context = PageElement(name='bar', context=True)
        >>> page = MyPage()
        >>> page.elem1
        >>> page.elem1 = 'sdfds'

    Page Elements act as property descriptors for their Page Object, you can get
    and set them as normal attributes.
    """
    def __init__(self, context=False, **kwargs) -> None:
        if not kwargs:
            raise ValueError("Please specify a locator")
        if len(kwargs) > 1:
            raise ValueError("Please specify only one locator")
        k, v = next(iter(kwargs.items()))
        self.locator = (_LOCATOR_MAP[k], v)
        self.has_context = bool(context)

    def __set__(self, instance, value: str) -> None:
        """ Send keys to the element. """
        if self.has_context:
            raise ValueError("Sorry, the set descriptor doesn't support elements with context.")
        elem = self.__get__(instance, instance.__class__)
        if not elem:
            raise ValueError("Can't send keys. "
                             f"Element with locator {self.locator} not found on the page")
        elem.clear()
        elem.send_keys(value)

    def __get__(self, instance, owner, context=None) -> Optional[
            Union[WebElement, Any, List[WebElement]]]:
        if not instance:
            return None

        if not context and self.has_context:
            return lambda cnt: self.__get__(instance, owner, context=cnt)

        if not context:
            context = instance.driver

        return self.find(context)

    def find(self, context: WebDriver = None) -> Optional[WebElement]:
        """ Find element on the page. """
        element = None
        try:
            element = context.find_element(*self.locator)
            # element = WebDriverWait(context, 3).until(
            #     ec.presence_of_element_located(self.locator)
            # )
        except (NoSuchElementException, TimeoutException):
            pass
            # print(f'Element with locator {self.locator} not found on the page!')
        return element
