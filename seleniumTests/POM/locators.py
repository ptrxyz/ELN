class AboutPageLocators(object):
    back_link_text = "Back"
    version_text_xpath = "/html/body/div/div/h3[1]"

class AdminPageLocators(object):
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

class LoginPageLocators(object):
    sign_up_link_text = "Sign up"
    forgot_password_link_text = "Forgot your password?"
    missing_confirmation_link_text = "Didn't receive confirmation instructions?"
    back_link_text = "Back"
    login_button_class_name = "btn-primary"
    username_textbox_id = "user_login"
    password_textbox_id = "user_password"

class MainFrameLocators(object):
    close_button_classname = "close"
    export_dropdown_button_id = "export-dropdown"
    import_button_xpath = '//*[@id="app"]/div/div[1]/nav/div/ul/div[3]/div[1]/div[1]/ul/li[7]/a'
    import_file_select_button_xpath = '/html/body/div[2]/div[2]/div/div/div[2]/div/div[1]/input'
    import_import_button_xpath = '/html/body/div[2]/div[2]/div/div/div[2]/div/div[2]/button[2]'
    export_button_xpath = '//*[@id="app"]/div/div[1]/nav/div/ul/div[3]/div[1]/div[1]/ul/li[6]/a'
    export_checkbox_xpath = '/html/body/div[2]/div[2]/div/div/div[2]/div/div[2]/ul/li[1]/label'
    export_export_button_xpath = '//*[@id="md-export-dropdown"]/span'
    my_data_button_id = "tree-id-My Data"
    sample_link_xpath = '//*[@id="tabList-pane-0"]/div/div[2]/table/tbody[1]/tr[2]/td[2]'
    analyses_tab_id = "SampleDetailsXTab-tab-analyses"
    qc_tab_id = "SampleDetailsXTab-tab-qc_curation"
    references_tab_id = "SampleDetailsXTab-tab-references"
    literature_tab_id = "SampleDetailsXTab-tab-literature"
    results_tab_id = "SampleDetailsXTab-tab-results"
    properties_tab_id = "SampleDetailsXTab-tab-properties"
    spectra_editor_button_classname = "fa-area-chart"
    spectra_close_button_classname = "button-right.btn.btn-sm.btn-danger"
    sample_close_button_classname = "fa.fa-times"
    sample_edit_molecule_button_xpath = '//*[@id="SampleDetailsXTab-pane-properties"]/span[1]/div/table/tbody/tr[1]/td/div/div[1]/div[1]/span/span/button'
    sample_name_textbox_id = "txinput_name"
    sample_save_button_classname = "fa.fa-floppy-o"    
    sample_name_label_xpath = '//*[@id="tabList-pane-0"]/div/div[2]/table/tbody[1]/tr[2]/td[2]/span/span[2]'
    sample_boiling_temperature_textbox_xpath = '//*[@id="SampleDetailsXTab-pane-properties"]/span[1]/div/table/tbody/tr[2]/td/div/div[3]/div/span/input'
    sample_melting_temperature_textbox_xpath = '//*[@id="SampleDetailsXTab-pane-properties"]/span[1]/div/table/tbody/tr[2]/td/div/div[4]/div/span/input'
    
    save_sample_xpath = '//*[@id="elements-tabs-pane-0"]/div/div[1]/div/button[2]'
    sample_iupac_xpath = '//*[@id="elements-tabs-pane-0"]/div/div[2]/div[1]/div[1]/h4/div/p[1]/span/span/text()[6]'                         
    stereo_abs_div_xpath = '//*[@id="react-select-3--value"]/div[1]'    
    stereo_abs_xpath = '//*[@id="react-select-3--option-'
    iupac_span = '//*[@id="elements-tabs-pane-0"]/div/div[2]/div[1]/div[1]/h4/div/p[1]/span/span'
    
class PasswordNewPageLocators(object):
    log_in_link_text = "Log in"
    sign_up_link_text = "Sign up"
    missing_confirmation_link_text = "Didn't receive confirmation instructions?"
    send_button_name = "commit"
    email_textbox_id = "user_email"
    error_message_label_xpath = '//*[@id="error_explanation"]/ul/li'

class SignupPageLocators(object):
    back_link_text = "Back"
    signup_button_class_name = "btn-primary"
    email_textbox_id = "user_email"
    password_textbox_id = "user_password"
    passwordconfirmation_textbox_id = "user_password_confirmation"
    firstname_textbox_id = "user_first_name"
    lastname_textbox_id = "user_last_name"
    abbreviation_textbox_id = "user_name_abbreviation"
    organization_textbox_id = "organization-select"

class TopFrameLocators(object):
    username_textbox_name = "user[login]"
    password_textbox_name = "user[password]"
    login_button_class_name = "glyphicon-log-in"
    dropdown_button_id = "bg-nested-dropdown-brand"
    chemotion_repository_button_xpath = '//*[@id="Home"]/div/div/div[1]/nav/div/div[1]/li/ul/li[1]/a'
    complat_button_xpath              = '//*[@id="Home"]/div/div/div[1]/nav/div/div[1]/li/ul/li[2]/a'
    complat_on_github_button_xpath    = '//*[@id="Home"]/div/div/div[1]/nav/div/div[1]/li/ul/li[3]/a'
    eln_button_xpath                  = '//*[@id="Home"]/div/div/div[1]/nav/div/div[1]/li/ul/li[5]/a'
    about_button_xpath                = '//*[@id="Home"]/div/div/div[1]/nav/div/div[1]/li/ul/li[7]/a'
    signup_button_xpath               = '//*[@id="Home"]/div/div/div[1]/nav/div/div[2]/ul/li/a'
    edit_button_classname = "btn-primary"   #rename suggestion: structure_edit_btn
    close_button_classname = "close"        #rename suggestion: structure_edit_close_btn
    cancel_button_classname = "btn-warning" #rename suggestion: structure_edit_cancel_btn
    logout_button_classname = "glyphicon-log-out"