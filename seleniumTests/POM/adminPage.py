from selenium.webdriver.common.by import By
from seleniumTests.POM.locators import Locator

class AdminPage():

    def __init__(self, driver):
        self.driver = driver        

    def enter_user_data(self, email, password, firstname, lastname, abbreviation):
        self.driver.find_element(By.ID, Locator.email_textbox_id).send_keys(email)        
        self.driver.find_element(By.ID, Locator.password_textbox_id).send_keys(password)        
        self.driver.find_element(By.ID, Locator.passwordconfirmation_textbox_id).send_keys(password)        
        self.driver.find_element(By.ID, Locator.firstname_textbox_id).send_keys(firstname)        
        self.driver.find_element(By.ID, Locator.lastname_textbox_id).send_keys(lastname)        
        self.driver.find_element(By.ID, Locator.abbreviation_textbox_id).send_keys(abbreviation)        

    def click_user_management_link(self):
        self.driver.find_element(By.LINK_TEXT, Locator.usermanagement_link_text).click()        

    def click_add_user_button(self):
        self.driver.find_element(By.CLASS_NAME, Locator.add_user_button_classname).click()        

    def click_create(self):
        self.driver.find_element(By.XPATH, Locator.create_button_xpath).click()        

    def click_create_old(self):
        self.driver.find_element(By.XPATH, Locator.create_button_old_xpath).click()        

    def click_close(self):
        self.driver.find_element(By.CLASS_NAME, Locator.close_button_classname).click()