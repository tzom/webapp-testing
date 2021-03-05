from selenium import webdriver
import unittest

class Basic(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor='http://selenium-hub:4444/wd/hub',
            desired_capabilities=getattr(webdriver.common.desired_capabilities.DesiredCapabilities, "CHROME")
        )
        self.driver.implicitly_wait(30)
    
    def test_basic(self):
        driver = self.driver
        driver.get("https://covradar.net/")
        driver.find_element_by_id("qsLoginBtn").click()
        driver.find_element_by_id("reportBtn").click() 

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
