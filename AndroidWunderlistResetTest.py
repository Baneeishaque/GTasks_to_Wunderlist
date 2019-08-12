import time
import unittest

from appium import webdriver


class AndroidWunderlistResetTestCase(unittest.TestCase):
    """Class to run tests against the Android Wunderlist app"""

    def setUp(self):
        """Setup for the test"""
        desired_caps = {'platformName': 'Android', 'platformVersion': '8.0', 'deviceName': 'LLD-AL10',
                        'appPackage': 'com.wunderkinder.wunderlistandroid',
                        'appActivity': '.activity.WLStartViewFragmentActivity'}
        # Since the app is already installed launching it using package and activity name
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def test_wunderlist(self):
        """Testing the Wunderlist app"""
        self.driver.implicitly_wait(30)
        time.sleep(5)

        sign_in = self.driver.find_element_by_id('com.wunderkinder.wunderlistandroid:id/login_textView_sign_in')
        sign_in.click()

        auto_complete_credentials = self.driver.find_element_by_id(
            "com.wunderkinder.wunderlistandroid:id/login_password_edittext")
        auto_complete_credentials.click()

        submit = self.driver.find_element_by_id('com.wunderkinder.wunderlistandroid:id/login_button')
        submit.click()
        time.sleep(60)

        # quick_add_fab = self.driver.find_element_by_xpath(
        #     "//android.widget.ImageButton[@resource-id='com.wunderkinder.wunderlistandroid:id/fab_quick_add']")
        # quick_add_fab.click()

        # From list of options available click on Rankings by finding element using uiautomator
        # rankings = self.driver.find_element_by_android_uiautomator('new UiSelector().text("Rankings")')
        # rankings.click()

        # Assert that Novak Djokovic is the top listed player
        # elmnt = self.driver.find_element_by_id('atpwta.live:id/Player1TV')
        # self.assertEqual('Novak Djokovic', elmnt.get_attribute('text'))
        # print elmnt.get_attribute('text')

        # Print the contents of Table listed for the top ranked player
        # table = self.driver.find_element_by_android_uiautomator("new UiSelector().className(android.widget.TableLayout)")
        # rows = table.find_elements_by_class_name('android.widget.TableRow')
        # for i in range(0, len(rows)):
        #     cols = rows[i].find_elements_by_class_name('android.widget.TextView')
        #     for j in range(0, len(cols)):
        #         print(cols[j].get_attribute('text')+" -- "),
        #     print("")

    def tearDown(self):
        """Tear down the test"""
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidWunderlistResetTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)
