from selenium.webdriver.common.by import By
from seleniumTests.POM.locators import SignupPageLocators as SPL

class SignupPage():

    def __init__(self, driver):
        self.driver = driver

    def click_back(self):
        self.driver.find_element(By.LINK_TEXT, SPL.back_link_text).click()

    def enter_user_data(self, email, password, firstname, lastname, abbreviation, organization="KIT"):
        self.driver.find_element(By.ID, SPL.email_textbox_id).send_keys(email)
        self.driver.find_element(By.ID, SPL.password_textbox_id).send_keys(password)
        self.driver.find_element(By.ID, SPL.passwordconfirmation_textbox_id).send_keys(password)
        self.driver.find_element(By.ID, SPL.firstname_textbox_id).send_keys(firstname)
        self.driver.find_element(By.ID, SPL.lastname_textbox_id).send_keys(lastname)
        self.driver.find_element(By.ID, SPL.abbreviation_textbox_id).send_keys(abbreviation)
        self.driver.find_element(By.ID, SPL.organization_textbox_id).send_keys(organization)
    
    def click_signup(self):
        self.driver.find_element(By.CLASS_NAME, SPL.signup_button_class_name).click()
        self.driver.implicitly_wait(5)