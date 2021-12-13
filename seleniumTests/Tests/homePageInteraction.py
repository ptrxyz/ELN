from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

import unittest

from seleniumTests.POM.homePage import HomePage
from seleniumTests.POM.signupPage import SignupPage
from seleniumTests.POM.topFrame import TopFrame

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
        
    def test_about_click(self):
        home_page = HomePage(self.driver)
        version_number = home_page.click_about()
        home_page.click_back()
        assert "1.0.3" in version_number
        assert "Chemotion" in self.driver.title

    def test_signup_click(self):
        home_page = HomePage(self.driver)
        home_page.click_signup()
        signup_page = SignupPage(self.driver)
        signup_page.click_back()
        assert "Chemotion" in self.driver.title

    def test_signup_user(self):
        home_page = HomePage(self.driver)
        home_page.click_signup()
        signup_page = SignupPage(self.driver)
        signup_page.enter_user_data("new.user@provider.edu", "asdasdasd", "new", "user", "neu")
        signup_page.click_signup()
        self.driver.implicitly_wait(5)
        top_frame = TopFrame(self.driver)
        try:
            top_frame.click_logout()
        except NoSuchElementException:
            signup_page.click_back()
        assert "Chemotion" in self.driver.title

    def test_eln_click(self):
        home_page = HomePage(self.driver)
        home_page.click_eln()
        assert "Chemotion" in self.driver.title

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()