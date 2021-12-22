from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

import unittest
import os
import sys
import time
file_path = os.path.abspath(os.path.join(os.path.dirname(__file__),'../..'))
sys.path.append(file_path)

from seleniumTests.POM.aboutPage import AboutPage
from seleniumTests.POM.signupPage import SignupPage
from seleniumTests.POM.topFrame import TopFrame

class LoginTest(unittest.TestCase):

    email_address = "new.user@provider.edu"
    password = "asdasdasd"
    first_name = "new"
    last_name = "user"
    abbreviation = "neu"

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    @classmethod
    def setUp(cls):
        cls.driver.get("http://localhost:4000/home")
        cls.driver.implicitly_wait(10)
        
    def test_0000_about_click(self):
        top_frame = TopFrame(self.driver)
        top_frame.click_about()
        about_page = AboutPage(self.driver)
        version_number = about_page.read_version()
        about_page.click_back()
        assert "1.0.3" in version_number
        assert "Chemotion" in self.driver.title

    def test_0001_signup_click(self):
        top_frame = TopFrame(self.driver)
        top_frame.click_signup()
        signup_page = SignupPage(self.driver)
        signup_page.click_back()
        assert "Chemotion" in self.driver.title

    def test_0002_signup_user(self):
        top_frame = TopFrame(self.driver)
        top_frame.click_signup()
        signup_page = SignupPage(self.driver)
        signup_page.enter_user_data(self.email_address, self.password, self.first_name, self.last_name, self.abbreviation)
        signup_page.click_signup()
        self.driver.implicitly_wait(5)
        try:
            top_frame.click_logout()
        except NoSuchElementException:
            signup_page.click_back()
        assert "Chemotion" in self.driver.title

    def test_0003_eln_click(self):
        top_frame = TopFrame(self.driver)
        top_frame.click_eln()
        assert "Chemotion" in self.driver.title

    def test_0004_edit_close_click(self):
        top_frame = TopFrame(self.driver)
        top_frame.click_edit()
        top_frame.click_edit_close()

    def test_0005_edit_cancel_click(self):
        top_frame = TopFrame(self.driver)
        top_frame.click_edit()
        top_frame.click_edit_cancel()

    def test_0006_chemotion_repository_click(self):
        top_frame = TopFrame(self.driver)
        top_frame.click_chemotion_repository()
        assert "Chemotion" in self.driver.title
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(1)
        assert "Chemotion | Chemotion" in self.driver.title
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def test_0007_complat_click(self):
        top_frame = TopFrame(self.driver)
        top_frame.click_complat()
        assert "Chemotion" in self.driver.title
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(1)
        assert "KIT" in self.driver.title
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def test_0008_complat_on_github_click(self):
        top_frame = TopFrame(self.driver)
        top_frame.click_complat_on_github()
        assert "Chemotion" in self.driver.title
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(1)
        assert "ComPlat" in self.driver.title
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()