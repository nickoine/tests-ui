from __future__ import annotations
from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from typing import Optional
    from selenium.webdriver.remote.webdriver import WebDriver


@pytest.mark.usefixtures("setup_for_tests")
class BaseTest:

    driver: Optional[WebDriver] = None
