from datetime import datetime
import pytest
from selenium.webdriver.common.by import By

from Pages.AccountPage import AccountPage
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from tests.test_base import BaseTest


class Test_Login(BaseTest):
    def test_login_with_valid_credentials(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_option()
        # home_page.click_on_my_account_drop_down_menu()
        # login_page = home_page.select_login_option()
        account_page = login_page.login_into_application("nitishkmishra44@gmail.com", "123456")
        # login_page.enter_email_address_text("nitishkmishra44@gmail.com")
        # login_page.enter_password_text("123456")
        # account_page = login_page.click_on_login_button()
        assert account_page.display_status_of_edit_your_account_information_option()

    def test_login_with_invalid_email_and_valid_password(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_option()
        login_page.login_into_application(self.generate_email_with_time_stamp(), "123456")
        expected_waring_message = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.retrieve_warning_message_for_invalid_email_or_password().__contains__(expected_waring_message)

    def test_login_with_valid_email_and_invalid_password(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_option()
        login_page.login_into_application("nitishkmishra44@gmail.com", "123456777")
        expected_waring_message = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.retrieve_warning_message_for_invalid_email_or_password().__contains__(expected_waring_message)

    def test_login_without_any_credentials(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_option()
        login_page.login_into_application("", "")
        expected_waring_message = "Warning: No match for E-Mail Address and/or Password."
        assert self.driver.find_element(By.XPATH, "//div[@id='account-login']/div").text.__contains__(expected_waring_message)



