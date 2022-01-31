class Locator(object):
    # User Management
    usermanagement_link_text = "User Management"
    add_user_button_classname = "btn-primary"
    email_textbox_id = "formControlEmail"
    password_textbox_id = "formControlPassword"
    passwordconfirmation_textbox_id = "formControlPasswordConfirmation"
    firstname_textbox_id = "formControlFirstName"
    lastname_textbox_id = "formControlLastName"
    abbreviation_textbox_id = "formControlAbbr"
    create_button_old_xpath = "/html/body/div[2]/div[2]/div/div/div[2]/div/form/div[9]/div/button[1]"                               
    create_button_xpath = '//*[@id="createUserTabs-pane-singleUser"]/form/div[8]/div/button'
    close_button_classname = "close"