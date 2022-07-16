"""
Create a webdriver.remote factory to be used as base, extends
unittest TestCase class overwritting setUp and tearDown methods.
This class will be inherited by the tests.
"""
from unittest import TestCase

from selenium import webdriver


class WebDriverSetup(TestCase):
    """Define the WebDriverSetup"""

    def setUp(self):
        """Setup different browser's capabilities and options.
        Define the Grid connection URL and which browser to launch.
        Creates the base driver."""
        chrome_options = webdriver.ChromeOptions()
        chrome_options.set_capability("browserName", "chrome")

        firefox_options = webdriver.FirefoxOptions()
        firefox_options.set_capability("browserName", "firefox")

        driver = webdriver.Remote(
            command_executor="http://localhost:4450", options=chrome_options
        )

        self.driver = driver

    def tearDown(self):
        """Clean up after test execution finishes."""
        if self.driver is not None:
            self.driver.quit()
