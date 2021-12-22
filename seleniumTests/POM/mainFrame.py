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