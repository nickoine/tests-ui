from __future__ import annotations
import json
import os
from pathlib import Path
import pytest
from typing import TYPE_CHECKING

from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService

from dto.user import User
from pages.base import WebPage
from pages.base import WebDriverFactory
from pages import LoginPage

if TYPE_CHECKING:
    from dto.user import User
    from _pytest.fixtures import SubRequest

_DATA_PATH = Path(__file__).parent / 'data'
_STATIC_PATH = _DATA_PATH / 'static'


@pytest.fixture()
def background_img() -> Path:
    return os.path.abspath(_STATIC_PATH / "background_pic.png")


@pytest.fixture()
def avatar_img() -> Path:
    return os.path.abspath(_STATIC_PATH / "avatar_pic.jpeg")


@pytest.fixture(scope="session")
def existing_user() -> User:
    """ Existing user credentials as dto."""
    path = _DATA_PATH / "existing_user.json"
    with open(path, 'rb') as content:
        json_string = json.dumps(json.load(content))
        return User.from_json(json_string)


@pytest.fixture(scope="session")
def web_driver(browser: str,
               chrome_service: Service,
               chrome_options: Options,
               firefox_service: FirefoxService,
               firefox_options: FirefoxOptions
               ) -> webdriver:
    """Cross browser web driver primary instance"""
    # WebDriverFactory is given a CLI parameter as value to match to an enumeration member
    wdf = WebDriverFactory(browser)
    driver = wdf.get_browser(webdriver,
                             chrome_service,
                             chrome_options,
                             firefox_service,
                             firefox_options)
    yield driver
    driver.close()


@pytest.fixture(scope="class")
def setup_for_tests(request: SubRequest, root_uri: str, existing_user: User, web_driver: webdriver):
    """ Base setup and login for test class."""
    # Set root uri for all page objects.
    WebPage.set_root_uri(root_uri)
    # Login as pre-condition
    login_page = LoginPage(web_driver)
    login_page.open()
    # Check that user auth_token is cookie doesn't exist.
    assert web_driver.get_cookie("auth_token") is None
    login_page.login(existing_user)
    # Set web driver instance to the test class.
    if request.cls is not None:
        request.cls.driver = web_driver
    yield


@pytest.fixture(scope="session")
def root_uri() -> str:
    """ Root uri for the page objects."""
    return os.getenv("BASE_URI", "https://twitter.com")


@pytest.fixture(scope="session")
def chrome_service() -> Service:
    """ Chrome driver manager."""
    return Service(ChromeDriverManager().install())


@pytest.fixture(scope="session")
def chrome_options() -> Options:
    """ Chrome driver options."""
    options = Options()
    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')
    # options.add_argument('--no-sandbox')
    return options


@pytest.fixture(scope="session")
def firefox_service() -> FirefoxService:
    """ Firefox driver manager."""
    return FirefoxService(GeckoDriverManager().install())


@pytest.fixture(scope="session")
def firefox_options() -> FirefoxOptions:
    """ Firefox driver options."""
    options = FirefoxOptions()
    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')
    # options.add_argument('--no-sandbox')
    return options


def pytest_addoption(parser) -> None:
    """Pytest hook that defines list of CLI arguments with descriptions and default values"""
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="my browser",
        choices=("firefox", "chrome", "phantomjs", "edge", "safari", "opera")
    )


@pytest.fixture(autouse=True, scope="session")
def browser(request) -> str:
    """Return command line option value"""
    return request.config.getoption("--browser")
