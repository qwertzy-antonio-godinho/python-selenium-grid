"""
Page Object Model definition for Home page.
"""
from dataclasses import dataclass

from selenium.webdriver.common.by import By


@dataclass
class PageLocators:
    """Identification of web elements to be found in the page."""

    element_search_textbox = "s"
    element_search_button = "search-image"


class PageObjects:
    """Create methods for using the web elements in the Tests."""

    def __init__(self, driver):
        """Initialization of POM using the web driver passed from the tests.
        Searches for elements in the page."""
        self.driver = driver

        self.element_search_textbox = driver.find_element(
            By.ID, PageLocators.element_search_textbox
        )
        self.element_search_button = driver.find_element(
            By.ID, PageLocators.element_search_button
        )

    def get_search_textbox(self):
        """Method to access and usage of element in the tests."""
        return self.element_search_textbox

    def get_search_button(self):
        """Method to access and usage of element in the tests."""
        return self.element_search_button
