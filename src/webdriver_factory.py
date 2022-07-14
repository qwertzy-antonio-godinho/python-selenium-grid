"""
asdasd
"""
from unittest import TestCase

from selenium import webdriver


class WebDriverSetup(TestCase):
    """sdasd"""

    def setUp(self):
        """sads"""
        chrome_options = webdriver.ChromeOptions()
        chrome_options.set_capability("browserName", "chrome")

        firefox_options = webdriver.FirefoxOptions()
        firefox_options.set_capability("browserName", "firefox")

        driver = webdriver.Remote(
            command_executor="http://localhost:4450", options=chrome_options
        )

        self.driver = driver

    def tearDown(self):
        """asdadsd"""
        if self.driver is not None:
            self.driver.quit()
