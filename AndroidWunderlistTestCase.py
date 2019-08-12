import time
import unittest

from AndroidWunderlistTestBase import AndroidWunderlistTestBase
from AppiumTestUtils import AppiumTestUtils


class AndroidWunderlistTestCase(unittest.TestCase):
    driver = None

    def setUp(self):
        # base = AndroidWunderlistTestBase()
        # print(base.desired_caps)

        desired_caps = AndroidWunderlistTestBase().desired_caps
        desired_caps['noReset'] = 'true'
        desired_caps['fullReset'] = 'false'
        desired_caps['appActivity'] = '.activity.WLMainFragmentActivity'
        # print(desired_caps)

        global driver
        driver = AppiumTestUtils.get_driver(desired_caps)
        print(driver)

    @staticmethod
    def test_wunderlist():
        """Testing the Wunderlist app"""
        driver.implicitly_wait(30)
        time.sleep(5)

        quick_add_fab = driver.find_element_by_id('com.wunderkinder.wunderlistandroid:id/fab_quick_add')
        quick_add_fab.click()
        pass

    def tearDown(self):
        # print(driver)
        AppiumTestUtils.tear_down(driver)


if __name__ == '__main__':
    AppiumTestUtils.run_suite(AndroidWunderlistTestCase)
