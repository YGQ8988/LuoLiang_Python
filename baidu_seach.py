from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchAttributeException
from selenium.common.exceptions import NoAlertPresentException
import unittest
class BaiduTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = 'http://www.baidu.com/'
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_baidu(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id('kw').send_keys('selenium 自动化测试')
        driver.find_element_by_id('su').click()
    def is_element_preasent(self,how,what):
        try:
            self.driver.find_element(by=how,value=what)
        except NoSuchAttributeException:
            return False
        return True
    def is_alert_present(self):
        try:
            alert = self.driver.switch_to_alert()
        except NoAlertPresentException:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True
    def tearDown(self):
        self.driver.quit()
        self.assertAlmostEqual([],self.verificationErrors)
if __name__ == '__main__':
	unittest.main()
