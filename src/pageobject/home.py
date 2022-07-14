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

    element_search_textbox = "s"
    element_search_button = "search-image"


class PageObjects:
    """sadsd"""

    def __init__(self, driver):
        """adsad"""
        self.driver = driver

        self.element_search_textbox = driver.find_element(
            By.ID, PageLocators.element_search_textbox
        )
        self.element_search_button = driver.find_element(
            By.ID, PageLocators.element_search_button
        )

    def get_search_textbox(self):
        """sadsad"""
        return self.element_search_textbox

    def get_search_button(self):
        """asdsad"""
        return self.element_search_button
