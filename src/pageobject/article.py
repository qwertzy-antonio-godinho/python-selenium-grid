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

    element_comments_div = "comments"


class PageObjects:
    """sadsd"""

    def __init__(self, driver):
        """adsad"""
        self.driver = driver

        self.element_comments_div = driver.find_element(
            By.ID, PageLocators.element_comments_div
        )

    def get_comments_div(self):
        """sadsad"""
        return self.element_comments_div
