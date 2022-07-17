"""
Create a webdriver.remote factory to be used as base, extends
unittest TestCase class overwritting setUp and tearDown methods.
This class will be inherited by the tests.
"""
from unittest import TestCase

from selenium import webdriver

from src.configuration import Configuration
from src.settings import Settings


class WebDriverSetup(TestCase, Configuration):
    """Define the WebDriverSetup"""

    settings = Settings(Configuration.ENVIRONMENT)

    def setUp(self):
        """Setup different browser's capabilities and options.
        Gets the Grid connection URL from Settings, gets which browser to launch from Configuration.
        Creates the base driver exposing Configurations and Settings to be used in the Tests."""

        chrome_options = webdriver.ChromeOptions()
        chrome_options.set_capability("browserName", "chrome")

        firefox_options = webdriver.FirefoxOptions()
        firefox_options.set_capability("browserName", "firefox")

        if Configuration.BROWSER == "chrome":
            options = chrome_options
        elif Configuration.BROWSER == "firefox":
            options = firefox_options
        else:
            raise Exception(
                f"Issue with {Configuration.BROWSER=}, are you using an accepted value?"
            )

        driver = webdriver.Remote(
            command_executor=self.settings.get_grid_url(), options=options
        )

        self.driver = driver

    def tearDown(self):
        """Clean up after test execution finishes."""
        if self.driver is not None:
            self.driver.quit()
