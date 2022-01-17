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

    @classmethod
    def setUp(cls):
        home_page = MainFrame(cls.driver)
        home_page.click_my_data_button()
        home_page.click_sample_link()

    def test_0000_analyses_tab_in_sample(self):
        home_page = MainFrame(self.driver)
        home_page.click_analyses_tab()

    def test_0001_open_spectra_in_sample(self):
        home_page = MainFrame(self.driver)
        home_page.click_analyses_tab()
        home_page.click_spectra_editor_button()
        time.sleep(1)
        home_page.click_spectra_close_button()
        time.sleep(1)

    def test_0002_qc_tab_in_sample(self):
        home_page = MainFrame(self.driver)
        home_page.click_qc_tab()

    def test_0003_literature_tab_in_sample(self):
        home_page = MainFrame(self.driver)
        home_page.click_literature_tab()

    def test_0004_results_tab_in_sample(self):
        home_page = MainFrame(self.driver)
        home_page.click_results_tab()

    def test_0005_properties_tab_in_sample(self):
        home_page = MainFrame(self.driver)
        home_page.click_properties_tab()

    @classmethod
    def tearDown(cls):
        home_page = MainFrame(cls.driver)
        home_page.click_sample_close_button()

    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        top_frame = TopFrame(cls.driver)
        top_frame.click_logout()
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()