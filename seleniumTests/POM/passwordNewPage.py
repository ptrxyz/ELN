from selenium.webdriver.common.by import By

class PasswordNewPage():

    def __init__(self, driver):
        self.driver = driver

        self.log_in_link_text = "Log in"
        self.sign_up_link_text = "Sign up"
        self.missing_confirmation_link_text = "Didn't receive confirmation instructions?"
        self.send_button_name = "commit"
        self.email_textbox_id = "user_email"
        self.error_message_label_xpath = '//*[@id="error_explanation"]/ul/li'

    def enter_email(self, email):
        elem = self.driver.find_element(By.ID, self.email_textbox_id)
        elem.clear()
        elem.send_keys(email)

    def click_send(self):
        elem = self.driver.find_element(By.NAME, self.send_button_name)
        elem.click()        

    def click_sign_up(self):
        elem = self.driver.find_element(By.LINK_TEXT, self.sign_up_link_text)
        elem.click()

    def click_missing_confirmation(self):
        elem = self.driver.find_element(By.LINK_TEXT, self.missing_confirmation_link_text)
        elem.click()

    def read_error_message(self):
        elem = self.driver.find_element(By.XPATH, self.error_message_label_xpath)
        error_message = elem.text
        return error_message