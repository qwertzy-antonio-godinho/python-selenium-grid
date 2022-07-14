"""
asdsad
"""
from dataclasses import dataclass

from sys import path

path.append(path[0] + "/..")

from selenium.webdriver.common.by import By


@dataclass
class PageLocators:
    """asdasd"""

    element_search_results_box = "content_box"
    element_search_results_article = "//article/header/h2/a"


class PageObjects:
    """sadsd"""

    def __init__(self, driver):
        """adsad"""
        self.driver = driver

        self.element_search_results_box = driver.find_element(
            By.ID, PageLocators.element_search_results_box
        )
        self.element_search_results_article = driver.find_elements(
            By.XPATH, PageLocators.element_search_results_article
        )

    def get_search_results_box(self, item):
        """sadsad"""
        for index, element_id in enumerate(
            self.element_search_results_article
        ):
            if index == item:
                return element_id
