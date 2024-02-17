from selenium.webdriver.common.by import By

from Pages.AccountSuccessPage import AccountSuccessPage


class RegisterPage:
    def __init__(self, driver):
        self.driver = driver

    first_name_field_xpath = "//input[@id='input-firstname']"
    last_name_field_xpath = "//input[@id='input-lastname']"
    email_id_field_xpath = "//input[@id='input-email']"
    telephone_field_xpath = "//input[@id='input-telephone']"
    password_field_xpath = "//input[@id='input-password']"
    confirm_password_field_xpath = "//input[@id='input-confirm']"
    term_and_condition_check_box_name = "agree"
    continue_button_xpath = "//input[@class='btn btn-primary']"
    newsletter_radio_button_xpath = "(//input[@name='newsletter'])[1]"
    duplicate_warning_message_xpath = "//div[@id='account-register']/div[1]"
    privacy_policy_warning_message_xpath = "//div[@id='account-register']/div[1]"
    first_name_warning_message_xpath = "//input[@id='input-firstname']/following-sibling::div"
    last_name_warning_message_xpath = "//input[@id='input-lastname']/following-sibling::div"
    email_warning_message_xpath = "//input[@id='input-email']/following-sibling::div"
    telephone_warning_message_xpath = "//input[@id='input-telephone']/following-sibling::div"
    password_warning_message_xpath = "//input[@id='input-password']/following-sibling::div"

    def enter_first_name(self, first_name_text):
        self.driver.find_element(By.XPATH, self.first_name_field_xpath).clear()
        self.driver.find_element(By.XPATH, self.first_name_field_xpath).send_keys(first_name_text)

    def enter_last_name(self, last_name_text):
        self.driver.find_element(By.XPATH, self.last_name_field_xpath).clear()
        self.driver.find_element(By.XPATH, self.last_name_field_xpath).send_keys(last_name_text)

    def enter_email_id(self, email_id_text):
        self.driver.find_element(By.XPATH, self.email_id_field_xpath).clear()
        self.driver.find_element(By.XPATH, self.email_id_field_xpath).send_keys(email_id_text)

    def enter_telephone_number(self, telephone_text):
        self.driver.find_element(By.XPATH, self.telephone_field_xpath).clear()
        self.driver.find_element(By.XPATH, self.telephone_field_xpath).send_keys(telephone_text)

    def enter_password(self, password_text):
        self.driver.find_element(By.XPATH, self.password_field_xpath).clear()
        self.driver.find_element(By.XPATH, self.password_field_xpath).send_keys(password_text)

    def enter_confirm_password(self, confirm_password_text):
        self.driver.find_element(By.XPATH, self.confirm_password_field_xpath).clear()
        self.driver.find_element(By.XPATH, self.confirm_password_field_xpath).send_keys(confirm_password_text)

    def click_on_term_and_condition_check_box(self):
        self.driver.find_element(By.NAME, self.term_and_condition_check_box_name).click()

    def click_on_continue_button(self):
        self.driver.find_element(By.XPATH, self.continue_button_xpath).click()
        return AccountSuccessPage(self.driver)

    def click_on_newsletter_radio_button(self):
        self.driver.find_element(By.XPATH, self.newsletter_radio_button_xpath).click()

    def register_an_account(self, first_name_text, last_name_text, email_id_text, telephone_text, password_text, confirm_password_text, yes_or_no, privacy_policy):
        self.enter_first_name(first_name_text)
        self.enter_last_name(last_name_text)
        self.enter_email_id(email_id_text)
        self.enter_telephone_number(telephone_text)
        self.enter_password(password_text)
        self.enter_confirm_password(confirm_password_text)
        if yes_or_no.__eq__("yes"):
            self.click_on_newsletter_radio_button()
        if privacy_policy.__eq__("select"):
            self.click_on_term_and_condition_check_box()
        return self.click_on_continue_button()


    def retrieve_duplicate_warning_message(self):
        return self.driver.find_element(By.XPATH, self.duplicate_warning_message_xpath).text

    def retrieve_privacy_policy_warning_message(self):
        return self.driver.find_element(By.XPATH, self.privacy_policy_warning_message_xpath).text

    def retrieve_first_name_warning_message(self):
        return self.driver.find_element(By.XPATH, self.first_name_warning_message_xpath).text

    def retrieve_last_name_warning_message(self):
        return self.driver.find_element(By.XPATH, self.last_name_warning_message_xpath).text

    def retrieve_email_warning_message(self):
        return self.driver.find_element(By.XPATH, self.email_warning_message_xpath).text

    def retrieve_telephone_warning_message(self):
        return self.driver.find_element(By.XPATH, self.telephone_warning_message_xpath).text

    def retrieve_password_warning_message(self):
        return self.driver.find_element(By.XPATH, self.password_warning_message_xpath).text

    def verify_all_warning(self, expected_privacy_policy_warning_message, expected_first_name_warning_message, expected_last_name_warning_message, expected_email_warning_message, expected_telephone_warning_message, expected_password_warning_message):
        actual_privacy_policy_warning_message = self.retrieve_privacy_policy_warning_message()
        actual_first_name_warning_message = self.retrieve_first_name_warning_message()
        actual_last_name_warning_message = self.retrieve_last_name_warning_message()
        actual_email_warning_message = self.retrieve_email_warning_message()
        actual_telephone_warning_message = self.retrieve_telephone_warning_message()
        actual_password_warning_message = self.retrieve_password_warning_message()

        status = False

        if expected_privacy_policy_warning_message.__contains__(actual_privacy_policy_warning_message):
            if expected_first_name_warning_message.__eq__(actual_first_name_warning_message):
                if expected_last_name_warning_message.__eq__(actual_last_name_warning_message):
                    if expected_email_warning_message.__eq__(actual_email_warning_message):
                        if expected_telephone_warning_message.__eq__(actual_telephone_warning_message):
                            if expected_password_warning_message.__eq__(actual_password_warning_message):
                                status = True

        return status
