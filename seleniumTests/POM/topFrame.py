from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from seleniumTests.POM.locators import TopFrameLocators as TFL

import time

class TopFrame():

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.NAME, TFL.username_textbox_name).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.NAME, TFL.password_textbox_name).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.CLASS_NAME, TFL.login_button_class_name).click()

    def press_return_login(self):
        self.driver.find_element(By.NAME, TFL.password_textbox_name).send_keys(Keys.RETURN)

    def click_chemotion_repository(self):
        self.driver.find_element(By.ID, TFL.dropdown_button_id).click()
        self.driver.find_element(By.XPATH, TFL.chemotion_repository_button_xpath).click()
        self.driver.implicitly_wait(5)

    def click_complat(self):
        self.driver.find_element(By.ID, TFL.dropdown_button_id).click()
        self.driver.find_element(By.XPATH, TFL.complat_button_xpath).click()
        self.driver.implicitly_wait(5)

    def click_complat_on_github(self):
        self.driver.find_element(By.ID, TFL.dropdown_button_id).click()
        self.driver.find_element(By.XPATH, TFL.complat_on_github_button_xpath).click()
        self.driver.implicitly_wait(5)

    def click_eln(self):
        self.driver.find_element(By.ID, TFL.dropdown_button_id).click()
        self.driver.find_element(By.XPATH, TFL.eln_button_xpath).click()
        self.driver.implicitly_wait(5)

    def click_about(self):
        self.driver.find_element(By.ID, TFL.dropdown_button_id).click()
        self.driver.find_element(By.XPATH, TFL.about_button_xpath).click()
        self.driver.implicitly_wait(5)

    def click_signup(self):
        self.driver.find_element(By.XPATH, TFL.signup_button_xpath).click()
        self.driver.implicitly_wait(5)

    def click_edit(self):
        self.driver.find_element(By.CLASS_NAME, TFL.edit_button_classname).click()

    def click_edit_close(self):
        self.driver.find_element(By.CLASS_NAME, TFL.close_button_classname).click()

    def click_edit_cancel(self):
        self.driver.find_element(By.CLASS_NAME, TFL.cancel_button_classname).click()

    def click_logout(self):
        time.sleep(1)
        self.driver.find_element(By.CLASS_NAME, TFL.logout_button_classname).click()