from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

import unittest
import time
import os
import sys
file_path = os.path.abspath(os.path.join(os.path.dirname(__file__),'../..'))
sys.path.append(file_path)

from seleniumTests.POM.adminPage import AdminPage
from seleniumTests.POM.topFrame import TopFrame
#from seleniumTests.POM.User import User

class LoginTest(unittest.TestCase):

    email_address = "chemotion_user_0001@chemotion.edu"
    password = "20b83105a867b20719e265839351f233"
    first_name = "chemotion_user"
    last_name = "0001"
    abbreviation = "cu1"

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    @classmethod
    def setUp(cls):
        cls.driver.get("http://localhost:4000/home")
        cls.driver.implicitly_wait(5)

    def enter_login_data(self):
        assert "Chemotion" in self.driver.title
         
        top_frame = TopFrame(self.driver)
        top_frame.enter_username(self.email_address)
        top_frame.enter_password(self.password)

    def enter_login_data_admin(self):
        assert "Chemotion" in self.driver.title

        top_frame = TopFrame(self.driver)
        top_frame.enter_username("ADM")
        top_frame.enter_password("PleaseChangeYourPassword")        

    def test_0000_create_new_user(self):
        self.enter_login_data_admin()
        top_frame = TopFrame(self.driver)
        top_frame.press_return_login()
        assert "Chemotion" in self.driver.title
        admin_page = AdminPage(self.driver)
        admin_page.click_user_management_link()
        admin_page.click_add_user_button()
        admin_page.enter_user_data(self.email_address, self.password, self.first_name, self.last_name, self.abbreviation)
        try:
            admin_page.click_create()
        except NoSuchElementException:
            admin_page.click_create_old()
        admin_page.click_close()

    def test_0001_login_valid_by_return_key(self):
        self.enter_login_data()
        top_frame = TopFrame(self.driver)
        top_frame.press_return_login()
        assert "Chemotion" in self.driver.title

    def test_0002_login_valid_by_button_click(self):
        self.enter_login_data()
        top_frame = TopFrame(self.driver)
        top_frame.click_login()
        assert "Chemotion" in self.driver.title

    @classmethod
    def tearDown(cls):
        time.sleep(2)
        top_frame = TopFrame(cls.driver)
        top_frame.click_logout()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
