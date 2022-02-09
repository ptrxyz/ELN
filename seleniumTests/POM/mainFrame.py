from selenium.webdriver.common.by import By
from seleniumTests.POM.locators import MainFrameLocators as MFL
import time
class MainFrame():

    def __init__(self, driver):
        self.driver = driver

    def click_import(self):
        self.driver.find_element(By.ID, MFL.export_dropdown_button_id).click()
        self.driver.find_element(By.XPATH, MFL.import_button_xpath).click()
    
    def enter_path_import_file_select(self, path):
        self.driver.find_element(By.XPATH, MFL.import_file_select_button_xpath).send_keys(path)

    def click_import_import(self):
        self.driver.find_element(By.XPATH, MFL.import_import_button_xpath).click()

    def click_import_close(self):
        self.driver.find_element(By.CLASS_NAME, MFL.close_button_classname).click()

    def click_export(self):
        self.driver.find_element(By.ID, MFL.export_dropdown_button_id).click()
        self.driver.find_element(By.XPATH, MFL.export_button_xpath).click() 

    def click_export_checkbox(self):
        self.driver.find_element(By.XPATH, MFL.export_checkbox_xpath).click()

    def click_export_export(self):
        self.driver.find_element(By.XPATH, MFL.export_export_button_xpath).click()

    def click_export_close(self):
        self.driver.find_element(By.CLASS_NAME, MFL.close_button_classname).click()

    def click_my_data_button(self):
        self.driver.find_element(By.ID, MFL.my_data_button_id).click()

    def click_sample_link(self):
        self.driver.find_element(By.XPATH, MFL.sample_link_xpath).click()

    def click_analyses_tab(self):
        self.driver.find_element(By.ID, MFL.analyses_tab_id).click()

    def click_qc_tab(self):
        self.driver.find_element(By.ID, MFL.qc_tab_id).click()

    def click_literature_tab(self):
        self.driver.find_element(By.ID, MFL.literature_tab_id).click()

    def click_references_tab(self):
        self.driver.find_element(By.ID, MFL.references_tab_id).click()

    def click_results_tab(self):
        self.driver.find_element(By.ID, MFL.results_tab_id).click()

    def click_properties_tab(self):
        self.driver.find_element(By.ID, MFL.properties_tab_id).click()

    def click_spectra_editor_button(self):
        self.driver.find_element(By.CLASS_NAME, MFL.spectra_editor_button_classname).click()

    def click_spectra_close_button(self):
        self.driver.find_element(By.CLASS_NAME, MFL.spectra_close_button_classname).click()

    def click_sample_close_button(self):
        self.driver.find_element(By.CLASS_NAME, MFL.sample_close_button_classname).click()

    def click_sample_edit_molecule_button(self):
        self.driver.find_element(By.XPATH, MFL.sample_edit_molecule_button_xpath).click()

    def click_sample_edit_molecule_close_button(self):
        self.driver.find_element(By.CLASS_NAME, MFL.close_button_classname).click()

    def enter_sample_name(self, name):
        elem = self.driver.find_element(By.ID, MFL.sample_name_textbox_id)
        elem.clear()
        elem.send_keys(name)

    def get_sample_name_from_label(self):
        return self.driver.find_element(By.XPATH, MFL.sample_name_label_xpath).text

    def save_sample(self):
        self.driver.find_element(By.CLASS_NAME, MFL.sample_save_button_classname).click()

    def enter_boiling_temperature(self, temperature):
        elem = self.driver.find_element(By.XPATH, MFL.sample_boiling_temperature_textbox_xpath)
        elem.clear()
        elem.send_keys(temperature)

    def enter_melting_temperature(self, temperature):
        elem = self.driver.find_element(By.XPATH, MFL.sample_melting_temperature_textbox_xpath)
        elem.clear()
        elem.send_keys(temperature)

    def get_boiling_temperature(self):
        return self.driver.find_element(By.XPATH, MFL.sample_boiling_temperature_textbox_xpath).get_attribute("value")

    def get_melting_temperature(self):
        return self.driver.find_element(By.XPATH, MFL.sample_melting_temperature_textbox_xpath).get_attribute("value")

    
    def get_iupac(self):
        elem = self.driver.find_element(By.XPATH, MFL.sample_iupac_xpath)

    def change_stereo_abs_value(self, value):
        elem = self.driver.find_element(By.XPATH, MFL.stereo_abs_div_xpath).click()
        elem = self.driver.find_element(By.XPATH, MFL.stereo_abs_xpath + value + '"]').click()

    def change_stereo_rel_value(self, value):
        elem = self.driver.find_element(By.XPATH, MFL.stereo_rel_div_xpath).click()
        elem = self.driver.find_element(By.XPATH, MFL.stereo_rel_xpath + value + '"]').click()    

    def save_sample_btn(self):
        elem = self.driver.find_element(By.XPATH, MFL.save_sample_xpath).click()
    
    def get_iupac_span(self):
        return self.driver.find_element(By.XPATH, MFL.iupac_span).text
    
    