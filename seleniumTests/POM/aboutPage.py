from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AboutPage():

    def __init__(self, driver):
        self.driver = driver

        self.back_link_text = "Back"

        self.version_text = "/html/body/div/div/h3[1]"

    def click_back(self):
        elem = self.driver.find_element(By.LINK_TEXT, self.back_link_text)
        elem.click()

    def read_version(self):
        elem = self.driver.find_element(By.XPATH, self.version_text)
        versionNumber = elem.text
        return versionNumber