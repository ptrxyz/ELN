from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.username_textbox_name = "user[login]"
        self.password_textbox_name = "user[password]"
        self.login_button_class_name = "glyphicon-log-in"
        self.dropdown_button_id = "bg-nested-dropdown-brand"
        self.about_button_xpath = '//*[@id="Home"]/div/div/div[1]/nav/div/div[1]/li/ul/li[7]/a'
        self.eln_button_xpath = '//*[@id="Home"]/div/div/div[1]/nav/div/div[1]/li/ul/li[5]/a'
        self.signup_button_xpath = '//*[@id="Home"]/div/div/div[1]/nav/div/div[2]/ul/li/a'
        self.back_link_text = "Back"

        # about
        self.version_text = "/html/body/div/div/h3[1]"

    def enter_username(self, username):
        elem = self.driver.find_element(By.NAME, self.username_textbox_name)
        elem.clear()
        elem.send_keys(username)

    def enter_password(self, password):
        elem = self.driver.find_element(By.NAME, self.password_textbox_name)
        elem.clear()
        elem.send_keys(password)

    def click_login(self):
        elem = self.driver.find_element(By.CLASS_NAME, self.login_button_class_name)
        elem.click()

    def press_return_login(self):
        elem = self.driver.find_element(By.NAME, self.password_textbox_name)
        elem.send_keys(Keys.RETURN)

    def click_about(self):
        elem = self.driver.find_element(By.ID, self.dropdown_button_id)
        elem.click()
        elem = self.driver.find_element(By.XPATH, self.about_button_xpath)
        elem.click()
        self.driver.implicitly_wait(5)
        elem = self.driver.find_element(By.XPATH, self.version_text)
        versionNumber = elem.text
        return versionNumber

    def click_signup(self):
        elem = self.driver.find_element(By.XPATH, self.signup_button_xpath)
        elem.click()
        self.driver.implicitly_wait(5)

    def click_eln(self):
        elem = self.driver.find_element(By.ID, self.dropdown_button_id)
        elem.click()
        elem = self.driver.find_element(By.XPATH, self.eln_button_xpath)
        elem.click()
        self.driver.implicitly_wait(5)

    def click_back(self):
        elem = self.driver.find_element(By.LINK_TEXT, self.back_link_text)
        elem.click()