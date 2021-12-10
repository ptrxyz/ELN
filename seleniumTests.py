from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import unittest
import time

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    @classmethod
    def setUp(cls):
        cls.driver.get("http://localhost:4000/home")
        cls.driver.implicitly_wait(10)
        

    def enter_login_data(self):
        assert "Chemotion" in self.driver.title
        elem = self.driver.find_element(By.NAME,"user[login]")
        elem.clear()
        elem.send_keys("test.user@provider.edu")
        elem = self.driver.find_element(By.NAME,"user[password]")
        elem.clear()
        elem.send_keys("asdasdasd")       

    def enter_login_data_admin(self):
        assert "Chemotion" in self.driver.title
        elem = self.driver.find_element(By.NAME,"user[login]")
        elem.clear()
        elem.send_keys("ADM")
        elem = self.driver.find_element(By.NAME,"user[password]")
        elem.clear()
        elem.send_keys("PleaseChangeYourPassword")

    def test_create_new_user(self):
        self.enter_login_data_admin()
        elem = self.driver.find_element(By.NAME,"user[password]")
        elem.send_keys(Keys.RETURN)
        assert "Chemotion" in self.driver.title
        elem = self.driver.find_element(By.LINK_TEXT,"User Management")
        elem.click()
        elem = self.driver.find_element(By.CLASS_NAME,"btn-primary")
        elem.click()
        elem = self.driver.find_element(By.ID,"formControlEmail")
        elem.send_keys("test.user@provider.edu")
        elem = self.driver.find_element(By.ID,"formControlPassword")
        elem.send_keys("asdasdasd")
        elem = self.driver.find_element(By.ID,"formControlPasswordConfirmation")
        elem.send_keys("asdasdasd")
        elem = self.driver.find_element(By.ID,"formControlFirstName")
        elem.send_keys("test")
        elem = self.driver.find_element(By.ID,"formControlLastName")
        elem.send_keys("user")
        elem = self.driver.find_element(By.ID,"formControlAbbr")
        elem.send_keys("teu")
        elem = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div/div/div[2]/div/form/div[9]/div/button[1]")
        elem.click()
        elem = self.driver.find_element(By.CLASS_NAME,"close")
        elem.click()

    def test_login_valid_by_return_key(self):
        self.enter_login_data()
        elem = self.driver.find_element(By.NAME,"user[password]")
        elem.send_keys(Keys.RETURN)
        assert "Chemotion" in self.driver.title

    def test_login_valid_by_button_click(self):
        self.enter_login_data()
        elem = self.driver.find_element(By.CLASS_NAME,"glyphicon-log-in")
        elem.click()
        assert "Chemotion" in self.driver.title

    @classmethod
    def tearDown(cls):
        time.sleep(2)
        elem = cls.driver.find_element(By.CLASS_NAME,"glyphicon-log-out")
        try:
            wait = WebDriverWait(cls.driver, 10)
            wait.until(EC.element_to_be_clickable(elem))
        finally:
            elem.click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()