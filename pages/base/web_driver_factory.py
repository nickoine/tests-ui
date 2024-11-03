#!/usr/bin/python3
# -*- encoding=utf8 -*-
from __future__ import annotations
from enum import Enum
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from selenium import webdriver
    from selenium.webdriver.remote.webdriver import WebDriver
    from selenium.webdriver.chrome.options import Options as Chrome_Options
    from selenium.webdriver.chrome.service import Service as Chrome_Service
    from selenium.webdriver.firefox.options import Options as Fox_Options
    from selenium.webdriver.firefox.service import Service as Fox_Service


# todo: rest of the constants in the method
class WebDriverFactory(Enum):
    """
    WebDriver Factory pattern implementation with Python enum for various browsers depend on its
    configuration.
    """
    CHROME = "chrome"
    FIREFOX = "firefox"
    PHANTOMJS = "phantomjs"
    EDGE = "edge"
    SAFARI = "safari"
    OPERA = "opera"

    def __str__(self):
        return self.name

    def __eq__(self, b):
        return self.value == b

    def __hash__(self):
        return id(self)

    def get_browser(self,
                    driver: webdriver,
                    chrome_service: Chrome_Service,
                    chrome_options: Chrome_Options,
                    firefox_service: Fox_Service,
                    firefox_options: Fox_Options) -> WebDriver:
        """
        Get WebDriver Instance based on the browser configuration
        Returns: 'WebDriver Instance'
        """
        if self.value == self.FIREFOX.value:
            browser_driver = driver.Firefox(service=firefox_service, options=firefox_options)
        else:
            browser_driver = driver.Chrome(service=chrome_service, options=chrome_options)
        browser_driver.implicitly_wait(5)
        return browser_driver
