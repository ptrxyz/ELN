from selenium.webdriver.common.by import By

class LoginPage():

    def __init__(self, driver):
        self.driver = driver

        self.sign_up_link_text = "Sign up"
        self.forgot_password_link_text = "Forgot your password?"
        self.missing_confirmation_link_text = "Didn't receive confirmation instructions?"
        self.back_link_text = "Back"
        self.login_button_class_name = "btn-primary"
        self.username_textbox_id = "user_login"
        self.password_textbox_id = "user_password"

    def enter_username(self, username):
        elem = self.driver.find_element(By.ID, self.username_textbox_id)
        elem.clear()
        elem.send_keys(username)

    def enter_password(self, password):
        elem = self.driver.find_element(By.ID, self.password_textbox_id)
        elem.clear()
        elem.send_keys(password)

    def click_login(self):
        elem = self.driver.find_element(By.CLASS_NAME, self.login_button_class_name)
        elem.click()        

    def click_sign_up(self):
        elem = self.driver.find_element(By.LINK_TEXT, self.sign_up_link_text)
        elem.click()

    def click_forgot_password(self):
        elem = self.driver.find_element(By.LINK_TEXT, self.forgot_password_link_text)
        elem.click()

    def click_missing_confirmation(self):
        elem = self.driver.find_element(By.LINK_TEXT, self.missing_confirmation_link_text)
        elem.click()

    def click_back(self):
        elem = self.driver.find_element(By.LINK_TEXT, self.back_link_text)
        elem.click()