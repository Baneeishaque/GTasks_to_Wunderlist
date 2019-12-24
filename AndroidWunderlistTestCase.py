import time
import unittest

from AndroidWunderlistTestBase import AndroidWunderlistTestBase
from AppiumTestUtils import AppiumTestUtils


class AndroidWunderlistTestCase(unittest.TestCase):
    desired_caps = AndroidWunderlistTestBase().desired_caps
    driver = None

    def setUp(self):
        self.prepare_desired_caps()
        global driver
        driver = AppiumTestUtils.get_driver(desired_caps)
        # print(driver)

    @staticmethod
    def prepare_desired_caps():
        global desired_caps
        desired_caps['noReset'] = 'true'
        desired_caps['fullReset'] = 'false'
        desired_caps['appActivity'] = '.activity.WLMainFragmentActivity'
        # print(desired_caps)

    @staticmethod
    def test_wunderlist():
        """Testing the Wunderlist app"""
        driver.implicitly_wait(30)
        time.sleep(5)

        quick_add_fab = driver.find_element_by_id('com.wunderkinder.wunderlistandroid:id/fab_quick_add')
        quick_add_fab.click()

    def tearDown(self):
        """Tear down the test"""
        # print(driver)
        driver.quit()


if __name__ == '__main__':
    AppiumTestUtils.run_suite(AndroidWunderlistTestCase)
