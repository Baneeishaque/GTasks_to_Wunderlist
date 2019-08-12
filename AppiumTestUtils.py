import unittest

from appium import webdriver


class AppiumTestUtils:

    @staticmethod
    def get_driver(desired_caps, connection_url='http://localhost:4723/wd/hub'):
        return webdriver.Remote(connection_url, desired_caps)

    @staticmethod
    def tear_down(driver):
        """Tear down the test"""
        driver.quit()

    @staticmethod
    def run_suite(test_case):
        suite = unittest.TestLoader().loadTestsFromTestCase(test_case)
        unittest.TextTestRunner(verbosity=2).run(suite)
