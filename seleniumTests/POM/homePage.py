from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.username_textbox_name = "user[login]"
        self.password_textbox_name = "user[password]"
        self.login_button_classname = "glyphicon-log-in"

    def enter_username(self, username):
        elem = self.driver.find_element(By.NAME, self.username_textbox_name)
        elem.clear()
        elem.send_keys(username)

    def enter_password(self, password):
        elem = self.driver.find_element(By.NAME, self.password_textbox_name)
        elem.clear()
        elem.send_keys(password)

    def click_login(self):
        elem = self.driver.find_element(By.CLASS_NAME, self.login_button_classname)
        elem.click()

    def press_return_login(self):
        elem = self.driver.find_element(By.NAME, self.password_textbox_name)
        elem.send_keys(Keys.RETURN)