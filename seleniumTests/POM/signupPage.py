from selenium.webdriver.common.by import By

class SignupPage():

    def __init__(self, driver):
        self.driver = driver

        self.back_link_text = "Back"
        self.signup_button_class_name = "btn-primary"

        self.email_textbox_id = "user_email"
        self.password_textbox_id = "user_password"
        self.passwordconfirmation_textbox_id = "user_password_confirmation"
        self.firstname_textbox_id = "user_first_name"
        self.lastname_textbox_id = "user_last_name"
        self.abbreviation_textbox_id = "user_name_abbreviation"
        self.organization_textbox_id = "organization-select"
        # country, department, group

    def click_back(self):
        elem = self.driver.find_element(By.LINK_TEXT, self.back_link_text)
        elem.click()

    def enter_user_data(self, email, password, firstname, lastname, abbreviation, organization="KIT"):
        elem = self.driver.find_element(By.ID, self.email_textbox_id)
        elem.clear()
        elem.send_keys(email)
        elem = self.driver.find_element(By.ID, self.password_textbox_id)
        elem.clear()
        elem.send_keys(password)
        elem = self.driver.find_element(By.ID, self.passwordconfirmation_textbox_id)
        elem.clear()
        elem.send_keys(password)
        elem = self.driver.find_element(By.ID, self.firstname_textbox_id)
        elem.clear()
        elem.send_keys(firstname)
        elem = self.driver.find_element(By.ID, self.lastname_textbox_id)
        elem.clear()
        elem.send_keys(lastname)
        elem = self.driver.find_element(By.ID, self.abbreviation_textbox_id)
        elem.clear()
        elem.send_keys(abbreviation)
        elem = self.driver.find_element(By.ID, self.organization_textbox_id)
        elem.clear()
        elem.send_keys(organization)
    
    def click_signup(self):
        elem = self.driver.find_element(By.CLASS_NAME, self.signup_button_class_name)
        elem.click()
        self.driver.implicitly_wait(5)