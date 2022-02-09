from selenium.webdriver.common.by import By
from seleniumTests.POM.locators import PasswordNewPageLocators as PNPL

class PasswordNewPage():

    def __init__(self, driver):
        self.driver = driver

    def enter_email(self, email):
        self.driver.find_element(By.ID, PNPL.email_textbox_id).send_keys(email)

    def click_send(self):
        self.driver.find_element(By.NAME, PNPL.send_button_name).click()        

    def click_sign_up(self):
        self.driver.find_element(By.LINK_TEXT, PNPL.sign_up_link_text).click()

    def click_missing_confirmation(self):
        self.driver.find_element(By.LINK_TEXT, PNPL.missing_confirmation_link_text).click()

    def read_error_message(self):
        return self.driver.find_element(By.XPATH, PNPL.error_message_label_xpath).text