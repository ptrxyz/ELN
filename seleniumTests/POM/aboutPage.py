from selenium.webdriver.common.by import By
from seleniumTests.POM.locators import AboutPageLocators as APL

class AboutPage():

    def __init__(self, driver):
        self.driver = driver

        self.back_link_text = "Back"
        self.version_text_xpath = "/html/body/div/div/h3[1]"

    def click_back(self):
        self.driver.find_element(By.LINK_TEXT, APL.back_link_text).click()

    def read_version(self):
        return self.driver.find_element(By.XPATH, APL.version_text_xpath).text