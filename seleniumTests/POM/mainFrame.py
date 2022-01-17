from selenium.webdriver.common.by import By

class MainFrame():

    def __init__(self, driver):
        self.driver = driver

        self.close_button_classname = "close"
        self.export_dropdown_button_id = "export-dropdown"
        self.import_button_xpath = '//*[@id="app"]/div/div[1]/nav/div/ul/div[3]/div[1]/div[1]/ul/li[7]/a'
        self.import_file_select_button_xpath = '/html/body/div[2]/div[2]/div/div/div[2]/div/div[1]/input'
        self.import_import_button_xpath = '/html/body/div[2]/div[2]/div/div/div[2]/div/div[2]/button[2]'
        self.export_button_xpath = '//*[@id="app"]/div/div[1]/nav/div/ul/div[3]/div[1]/div[1]/ul/li[6]/a'
        self.export_checkbox_xpath = '/html/body/div[2]/div[2]/div/div/div[2]/div/div[2]/ul/li[1]/label'
        self.export_export_button_xpath = '//*[@id="md-export-dropdown"]/span'
        self.my_data_button_id = "tree-id-My Data"
        self.sample_link_xpath = '//*[@id="tabList-pane-0"]/div/div[2]/table/tbody[1]/tr[2]/td[2]'
        self.analyses_tab_id = "SampleDetailsXTab-tab-analyses"
        self.qc_tab_id = "SampleDetailsXTab-tab-qc_curation"
        self.literature_tab_id = "SampleDetailsXTab-tab-literature"
        self.results_tab_id = "SampleDetailsXTab-tab-results"
        self.properties_tab_id = "SampleDetailsXTab-tab-properties"
        self.spectra_editor_button_classname = "fa-area-chart"
        self.spectra_close_button_classname = "button-right.btn.btn-sm.btn-danger"
        self.sample_close_button_classname = "fa.fa-times"

    def click_import(self):
        elem = self.driver.find_element(By.ID, self.export_dropdown_button_id)
        elem.click()
        elem = self.driver.find_element(By.XPATH, self.import_button_xpath)
        elem.click()
    
    def enter_path_import_file_select(self, path):
        elem = self.driver.find_element(By.XPATH, self.import_file_select_button_xpath)
        elem.send_keys(path)

    def click_import_import(self):
        elem = self.driver.find_element(By.XPATH, self.import_import_button_xpath)
        elem.click()

    def click_import_close(self):
        elem = self.driver.find_element(By.CLASS_NAME, self.close_button_classname)
        elem.click()

    def click_export(self):
        elem = self.driver.find_element(By.ID, self.export_dropdown_button_id)
        elem.click()
        elem = self.driver.find_element(By.XPATH, self.export_button_xpath)
        elem.click()

    def click_export_checkbox(self):
        elem = self.driver.find_element(By.XPATH, self.export_checkbox_xpath)
        elem.click()

    def click_export_export(self):
        elem = self.driver.find_element(By.XPATH, self.export_export_button_xpath)
        elem.click()

    def click_export_close(self):
        elem = self.driver.find_element(By.CLASS_NAME, self.close_button_classname)
        elem.click()

    def click_my_data_button(self):
        elem = self.driver.find_element(By.ID, self.my_data_button_id)
        elem.click()

    def click_sample_link(self):
        elem = self.driver.find_element(By.XPATH, self.sample_link_xpath)
        elem.click()

    def click_analyses_tab(self):
        elem = self.driver.find_element(By.ID, self.analyses_tab_id)
        elem.click()

    def click_qc_tab(self):
        elem = self.driver.find_element(By.ID, self.qc_tab_id)
        elem.click()

    def click_literature_tab(self):
        elem = self.driver.find_element(By.ID, self.literature_tab_id)
        elem.click()

    def click_results_tab(self):
        elem = self.driver.find_element(By.ID, self.results_tab_id)
        elem.click()

    def click_properties_tab(self):
        elem = self.driver.find_element(By.ID, self.properties_tab_id)
        elem.click()

    def click_spectra_editor_button(self):
        elem = self.driver.find_element(By.CLASS_NAME, self.spectra_editor_button_classname)
        elem.click()

    def click_spectra_close_button(self):
        elem = self.driver.find_element(By.CLASS_NAME, self.spectra_close_button_classname)
        elem.click()

    def click_sample_close_button(self):
        elem = self.driver.find_element(By.CLASS_NAME, self.sample_close_button_classname)
        elem.click()