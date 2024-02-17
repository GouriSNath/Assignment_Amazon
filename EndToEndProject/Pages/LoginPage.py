from selenium.webdriver.common.by import By
from Pages.AccountPage import AccountPage


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    email_address_box_xpath = "//input[@id='input-email']"
    password_box_xpath = "//input[@id='input-password']"
    login_button_xpath = "//input[contains(@class,'btn')]"
    warning_message_for_invalid_email_or_password_xpath = "//div[@id='account-login']/div"

    def enter_email_address_text(self, email_address_text):
        self.driver.find_element(By.XPATH, self.email_address_box_xpath).clear()
        self.driver.find_element(By.XPATH, self.email_address_box_xpath).send_keys(email_address_text)

    def enter_password_text(self, password_text):
        self.driver.find_element(By.XPATH, self.password_box_xpath).clear()
        self.driver.find_element(By.XPATH, self.password_box_xpath).send_keys(password_text)

    def click_on_login_button(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()
        return AccountPage(self.driver)

    def login_into_application(self, email_address_text, password_text):
        self.enter_email_address_text(email_address_text)
        self.enter_password_text(password_text)
        return self.click_on_login_button()

    def retrieve_warning_message_for_invalid_email_or_password(self):
        return self.driver.find_element(By.XPATH, self.warning_message_for_invalid_email_or_password_xpath).text


