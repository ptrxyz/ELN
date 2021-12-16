from selenium.webdriver.common.by import By

class AdminPage():

    def __init__(self, driver):
        self.driver = driver

        self.usermanagement_link_text = "User Management"
        self.add_user_button_classname = "btn-primary"
        self.email_textbox_id = "formControlEmail"
        self.password_textbox_id = "formControlPassword"
        self.passwordconfirmation_textbox_id = "formControlPasswordConfirmation"
        self.firstname_textbox_id = "formControlFirstName"
        self.lastname_textbox_id = "formControlLastName"
        self.abbreviation_textbox_id = "formControlAbbr"
        self.create_button_old_xpath = "/html/body/div[2]/div[2]/div/div/div[2]/div/form/div[9]/div/button[1]"
        self.create_button_xpath = '//*[@id="createUserTabs-pane-singleUser"]/form/div[8]/div/button'
        self.close_button_classname = "close"

    def enter_user_data(self, email, password, firstname, lastname, abbreviation):
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

    def click_user_management_link(self):
        elem = self.driver.find_element(By.LINK_TEXT,self.usermanagement_link_text)
        elem.click()

    def click_add_user_button(self):
        elem = self.driver.find_element(By.CLASS_NAME,self.add_user_button_classname)
        elem.click()

    def click_create(self):
        elem = self.driver.find_element(By.XPATH, self.create_button_xpath)
        elem.click()

    def click_create_old(self):
        elem = self.driver.find_element(By.XPATH, self.create_button_old_xpath)
        elem.click()

    def click_close(self):
        elem = self.driver.find_element(By.CLASS_NAME, self.close_button_classname)
        elem.click()