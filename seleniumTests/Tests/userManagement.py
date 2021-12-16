from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

import unittest
import time
import os
import sys
file_path = os.path.abspath(os.path.join(os.path.dirname(__file__),'../..'))
sys.path.append(file_path)

from seleniumTests.POM.adminPage import AdminPage
from seleniumTests.POM.homePage import HomePage
from seleniumTests.POM.topFrame import TopFrame

class LoginTest(unittest.TestCase):

    email_address = "test.user@provider.edu"
    password = "asdasdasd"
    first_name = "test"
    last_name = "user"
    abbreviation = "teu"

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
         
        home_page = HomePage(self.driver)
        home_page.enter_username(self.email_address)
        home_page.enter_password(self.password)

    def enter_login_data_admin(self):
        assert "Chemotion" in self.driver.title

        home_page = HomePage(self.driver)
        home_page.enter_username("ADM")
        home_page.enter_password("PleaseChangeYourPassword")        

    def test_create_new_user(self):
        self.enter_login_data_admin()
        home_page = HomePage(self.driver)
        home_page.press_return_login()
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

    def test_login_valid_by_return_key(self):
        self.enter_login_data()
        home_page = HomePage(self.driver)
        home_page.press_return_login()
        assert "Chemotion" in self.driver.title

    def test_login_valid_by_button_click(self):
        self.enter_login_data()
        home_page = HomePage(self.driver)
        home_page.click_login()
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