from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TopFrame():

    def __init__(self, driver):
        self.driver = driver

        self.logout_button_classname = "glyphicon-log-out"

    def click_logout(self):
        elem = self.driver.find_element(By.CLASS_NAME, self.logout_button_classname)
        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.element_to_be_clickable(elem))
        finally:
            elem.click()