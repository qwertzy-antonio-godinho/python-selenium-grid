"""
Page Object Model definition for Search results page.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class PageLocators:
    """Identification of web elements to be found in the page."""

    element_search_results_box = "content_box"
    element_search_results_article = "//article/header/h2/a"


class PageObjects(PageLocators):
    """Create methods for using the web elements in the Tests."""

    def __init__(self, driver, timeout):
        """Initialization of POM using the web driver passed from the tests.
        Searches for elements in the page."""
        self.driver = driver
        self.timeout = timeout

        self.element_search_results_box = WebDriverWait(
            self.driver, self.timeout
        ).until(
            expected_conditions.presence_of_element_located(
                (By.ID, PageLocators.element_search_results_box)
            )
        )

        self.element_search_results_article = WebDriverWait(
            self.driver, self.timeout
        ).until(
            expected_conditions.presence_of_all_elements_located(
                (By.XPATH, PageLocators.element_search_results_article)
            )
        )

    def get_search_results_box(self, item):
        """Method to access and usage of element in the tests. Note, the item
        passed if not exists will return None."""
        for index, element_id in enumerate(
            self.element_search_results_article
        ):
            if index == item:
                return element_id
