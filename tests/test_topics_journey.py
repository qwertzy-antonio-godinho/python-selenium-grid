"""
Tests to test Topics journey.
"""
from sys import path

path.append(path[0] + "/..")

from assertpy import assert_that
from src.pageobject.home import PageObjects as HomePOM
from src.pageobject.topic import PageObjects as TopicPOM
from src.webdriver_factory import WebDriverSetup


class TestTopics(WebDriverSetup):
    """Test User journey Home -> Topics -> Verify
    number of topics per page."""

    def test_user_journey_number_of_topics_available_from_home_page(self):
        """Test implementation, navigate to site, instantiate the page
        POM objects, perform actions on them and assert test."""
        driver = self.driver
        driver.get("https://www.osnews.com")

        home_page = HomePOM(driver)
        home_page.get_topics_dropdown().select_by_visible_text("Gentoo")

        topic_page = TopicPOM(driver)
        assert_that(topic_page.get_topic_articles()).is_same_as(20)
