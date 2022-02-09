from selenium.webdriver.common.by import By
from seleniumTests.POM.locators import LoginPageLocators as LPL

class LoginPage():

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        elem = self.driver.find_element(By.ID, LPL.username_textbox_id)
        elem.clear()
        elem.send_keys(username)

    def enter_password(self, password):
        elem = self.driver.find_element(By.ID, LPL.password_textbox_id)
        elem.clear()
        elem.send_keys(password)

    def click_login(self):
        self.driver.find_element(By.CLASS_NAME, LPL.login_button_class_name).click()        

    def click_sign_up(self):
        self.driver.find_element(By.LINK_TEXT, LPL.sign_up_link_text).click()

    def click_forgot_password(self):
        self.driver.find_element(By.LINK_TEXT, LPL.forgot_password_link_text).click()

    def click_missing_confirmation(self):
        self.driver.find_element(By.LINK_TEXT, LPL.missing_confirmation_link_text).click()

    def click_back(self):
        self.driver.find_element(By.LINK_TEXT, LPL.back_link_text).click()