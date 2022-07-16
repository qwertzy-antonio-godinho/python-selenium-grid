"""
Tests to test User journey.
"""
from sys import path

path.append(path[0] + "/..")

from src.pageobject.article import PageObjects as ArticlePOM
from src.pageobject.home import PageObjects as HomePOM
from src.pageobject.search_results import PageObjects as SearchResultsPOM
from src.webdriver_factory import WebDriverSetup


class TestComments(WebDriverSetup):
    """Test User journey Home -> Search -> Select story from list -> Verify
    comments section is available."""

    def test_user_journey_comments_available_from_home_page_search(self):
        """Test implementation, navigate to site, instantiate the page
        POM objects, perform actions on them and assert test."""
        driver = self.driver
        driver.get("https://www.osnews.com")

        home_page = HomePOM(driver)
        home_page.get_search_textbox().send_keys("Test")
        home_page.get_search_button().click()

        search_results_page = SearchResultsPOM(driver)

        # Will raise exception and fail test if value doesn't exist
        # AttributeError: 'NoneType' object has no attribute 'click'
        search_results_page.get_search_results_box(1).click()

        article_page = ArticlePOM(driver)
        assert article_page.get_comments_div() is not None
