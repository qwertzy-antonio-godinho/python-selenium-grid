"""
Page Object Model definition for Home page.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait


class PageLocators:
    """Identification of web elements to be found in the page."""

    element_search_textbox = "s"
    element_search_button = "search-image"
    element_topics_dropdown = "cat"


class PageObjects(PageLocators):
    """Create methods for using the web elements in the Tests."""

    def __init__(self, driver, timeout):
        """Initialization of POM using the web driver passed from the tests.
        Searches for elements in the page."""
        self.driver = driver
        self.timeout = timeout

        self.element_search_textbox = WebDriverWait(
            self.driver, self.timeout
        ).until(
            expected_conditions.presence_of_element_located(
                (By.ID, PageLocators.element_search_textbox)
            )
        )

        self.element_search_button = WebDriverWait(
            self.driver, self.timeout
        ).until(
            expected_conditions.presence_of_element_located(
                (By.ID, PageLocators.element_search_button)
            )
        )

        self.element_topics_dropdown_selection = Select(
            WebDriverWait(self.driver, self.timeout).until(
                expected_conditions.presence_of_element_located(
                    (By.ID, PageLocators.element_topics_dropdown)
                )
            )
        )

    def get_search_textbox(self):
        """Method to access and usage of element in the tests."""
        return self.element_search_textbox

    def get_search_button(self):
        """Method to access and usage of element in the tests."""
        return self.element_search_button

    def get_topics_dropdown(self):
        """Method to access and usage of element in the tests."""
        return self.element_topics_dropdown_selection
