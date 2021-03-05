from selenium import webdriver
import unittest

class Basic(unittest.TestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(options=chrome_options)
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
