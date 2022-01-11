from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

import unittest
import time
import os
import sys
file_path = os.path.abspath(os.path.join(os.path.dirname(__file__),'../..'))
sys.path.append(file_path)

from seleniumTests.POM.mainFrame import MainFrame
from seleniumTests.POM.topFrame import TopFrame

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get("http://localhost:4000/home")
        cls.driver.implicitly_wait(10)
        top_frame = TopFrame(cls.driver)
        top_frame.enter_username("test.user@provider.edu")
        top_frame.enter_password("asdasdasd")
        top_frame.click_login()

    def test_0000_analyses_tab_in_sample(self):
        home_page = MainFrame(self.driver)
        home_page.click_my_data_button()
        home_page.click_sample_link()
        home_page.click_analyses_tab()

    def test_0001_open_spectra_in_sample(self):
        home_page = MainFrame(self.driver)
        home_page.click_my_data_button()
        home_page.click_sample_link()
        home_page.click_analyses_tab()
        home_page.click_spectra_editor_button()
        time.sleep(2)
        home_page.click_spectra_close_button()

    @classmethod
    def tearDownClass(cls):
        time.sleep(15)
        top_frame = TopFrame(cls.driver)
        top_frame.click_logout()
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()