"""
Page Object Model definition for Articles page.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class PageLocators:
    """Identification of web elements to be found in the page."""

    element_comments_div = "comments"


class PageObjects:
    """Create methods for using the web elements in the Tests."""

    def __init__(self, driver, timeout):
        """Initialization of POM using the web driver passed from the tests.
        Searches for elements in the page."""
        self.driver = driver
        self.timeout = timeout

        self.element_comments_div = WebDriverWait(
            self.driver, self.timeout
        ).until(
            expected_conditions.presence_of_element_located(
                (By.ID, PageLocators.element_comments_div)
            )
        )

    def get_comments_div(self):
        """Method to access and usage of element in the tests."""
        return self.element_comments_div
