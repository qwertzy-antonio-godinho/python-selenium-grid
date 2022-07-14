"""
asdsad
"""
from sys import path

path.append(path[0] + "/../..")

from src.webdriver_factory import WebDriverSetup
from src.pageobject.home import PageObjects as HomePOM
from src.pageobject.search_results import PageObjects as SearchResultsPOM
from src.pageobject.article import PageObjects as ArticlePOM


class TestComments(WebDriverSetup):
    """asdsdad"""

    def test_user_journey_comments_available_from_home_page_search(self):
        """asdsd"""
        driver = self.driver
        driver.get("https://www.osnews.com")

        home_page = HomePOM(driver)
        home_page.get_search_textbox().send_keys("Test")
        home_page.get_search_button().click()

        search_results_page = SearchResultsPOM(driver)
        search_results_page.get_search_results_box(1).click()

        article_page = ArticlePOM(driver)
        assert article_page.get_comments_div() is not None
