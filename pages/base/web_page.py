#!/usr/bin/python3
# -*- encoding=utf8 -*-
from __future__ import annotations
from typing import TYPE_CHECKING

from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

if TYPE_CHECKING:
    from typing import Optional, Any
    from selenium.webdriver.remote.webdriver import WebDriver


# todo: logger
class WebPage:
    """ Page Object pattern.

    _driver: `selenium.webdriver.WebDriver`
        Selenium web driver instance.

    _root_uri: `str`
        Root URI to base any calls to the ``WebPage.open`` method. If not defined
        in the constructor it will try and look it from the class variable '_root_uri'.

    _page_uri: `str`
        Page URI which will be added to the root
        and used by any calls to the ``WebPage.open`` method. If not defined
        in the constructor it will try and look it from the class variable '_page_uri'.

    _title_is: `str`
        Page title.

    _title_contains: `str`
        Substring of page title.

    All parameters(except 'driver') may be initialized in child classes as class attributes.
    """
    _driver = None
    _root_uri = None
    _page_uri = None
    _title_is = None
    _title_contains = None

    def __init__(self,
                 driver: WebDriver,
                 page_uri: Optional[str] = None,
                 title_contains: Optional[str] = None) -> None:

        self._driver = driver

        if not self._root_uri:
            raise ValueError(f"'_root_uri' doesn't specified for {self.__class__}.")

        if page_uri is not None:
            self._page_uri = page_uri
        elif not self._page_uri:
            raise ValueError(f"'_page_uri' doesn't specified for {self.__class__}.")

        if title_contains is not None:
            self._title_contains = title_contains

        self._full_url = self._root_uri + self._page_uri

    @classmethod
    def set_root_uri(cls, root_uri: str) -> None:
        """ Method for setting root uri for all page objects that will be extended from WebPage."""
        cls._root_uri = root_uri

    @property
    def driver(self) -> WebDriver:
        """ Web driver instance of the page object."""
        return self._driver

    @property
    def full_url(self) -> str:
        """ Page object full url."""
        return self._full_url

    def wait_title_contains(self) -> None:
        """ Wait until title of the web page contains '_title_contains' substring."""
        if not self._title_contains:
            raise ValueError(f"'_title_contains' doesn't specified for {self.__class__}.")
        WebDriverWait(self.driver, 10).until(ec.title_contains(self._title_contains))

    def wait_title_is(self) -> None:
        """ Wait until driver title contains page title."""
        if not self._title_is:
            raise ValueError(f"'_title_is' doesn't specified for {self.__class__}.")
        WebDriverWait(self.driver, 10).until(ec.title_is(self._title_is))

    def open(self) -> None:
        self._driver.get(self._full_url)
        self.driver.maximize_window()

    def go_back(self) -> None:
        self._driver.back()

    def refresh(self) -> None:
        self._driver.refresh()

    def scroll_down(self, offset: int = 0) -> None:
        """ Scroll the page down. """
        if offset:
            self._driver.execute_script('window.scrollTo(0, {0});'.format(offset))
        else:
            self._driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

    def scroll_up(self, offset: int = 0) -> None:
        """ Scroll the page up. """
        if offset:
            self._driver.execute_script('window.scrollTo(0, -{0});'.format(offset))
        else:
            self._driver.execute_script('window.scrollTo(0, -document.body.scrollHeight);')

    def switch_to_iframe(self, iframe: str) -> None:
        """ Switch to iframe by its name. """
        self._driver.switch_to.frame(iframe)

    def switch_out_iframe(self) -> None:
        """ Cancel iframe focus. """
        self._driver.switch_to.default_content()

    def find_element(self, *locator) -> Any:
        """ Find element by locator"""
        return self.driver.find_element(*locator)

    def hover(self, *locator) -> None:
        """ Hover onto element """
        element = self.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    # todo: refactor screenshot method
    #  https://github.com/DanSchon/page_objects_python_automation/blob/master/base/base_page.py
    def screenshot(self, file_name='screenshot.png'):
        self._driver.save_screenshot(file_name)
