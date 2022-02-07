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
        try:
            home_page.click_literature_tab()
        except NoSuchElementException:
            home_page.click_references_tab()

    def test_0004_results_tab_in_sample(self):
        home_page = MainFrame(self.driver)
        home_page.click_results_tab()

    def test_0005_properties_tab_in_sample(self):
        home_page = MainFrame(self.driver)
        home_page.click_properties_tab()

    def test_0006_edit_molecule_in_sample(self):
        home_page = MainFrame(self.driver)
        home_page.click_sample_edit_molecule_button()
        time.sleep(1)
        home_page.click_sample_edit_molecule_close_button()
        time.sleep(1)

    def test_0007_enter_name_in_sample(self):
        home_page = MainFrame(self.driver)
        time_string = time.strftime("%Y%m%d-%H%M%S")
        home_page.enter_sample_name("TestSampleName" + time_string)
        home_page.save_sample()
        time.sleep(2)
        assert time_string in home_page.get_sample_name_from_label()    

    def test_0008_enter_temperatures_in_sample(self):
        home_page = MainFrame(self.driver)
        boiling_temperature = time.strftime("%M%S")
        melting_temperature = time.strftime("%S%M")
        home_page.enter_boiling_temperature(boiling_temperature)
        home_page.enter_melting_temperature(melting_temperature)
        home_page.save_sample()
        time.sleep(2)
        home_page.click_sample_link()
        assert boiling_temperature in home_page.get_boiling_temperature()
        assert melting_temperature in home_page.get_melting_temperature()

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