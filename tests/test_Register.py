import time
from datetime import datetime
import pytest
from selenium.webdriver.common.by import By

from Pages.AccountSuccessPage import AccountSuccessPage
from Pages.HomePage import HomePage
from Pages.RegisterPage import RegisterPage
from tests.test_base import BaseTest


class Test_Register(BaseTest):
    def test_register_with_mandatory_fields(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_option()
        # home_page.click_on_my_account_drop_down_menu()
        # register_page = home_page.select_register_option()
        account_success_page = register_page.register_an_account("Nikunja", "Panigrahi", self.generate_email_with_time_stamp(), "735293820", "45678", "45678", "no", "select")
        expected_heading_text = "Your Account Has Been Created!"
        assert account_success_page.retrieve_success_message_for_account_registration().__eq__(expected_heading_text)

    def test_register_with_all_fields(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_option()
        account_success_page = register_page.register_an_account("Nikunja", "Panigrahi", self.generate_email_with_time_stamp(), "735293820", "45678", "45678", "yes", "select")
        expected_heading_text = "Your Account Has Been Created!"
        assert account_success_page.retrieve_success_message_for_account_registration().__eq__(expected_heading_text)

    def test_register_with_existing_email(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_option()
        register_page.register_an_account("Nitish", "Mishra", "nitishk44@gmail.com", "8658656446", "123456", "123456", "yes", "select")
        expected_duplicate_email_warning_message = "Warning: E-Mail Address is already registered!"
        assert register_page.retrieve_duplicate_warning_message().__contains__(expected_duplicate_email_warning_message)

    def test_register_without_any_fields(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_option()
        register_page.register_an_account("", "", "", "", "", "", "no", "no")
        assert register_page.verify_all_warning("Warning: You must agree to the Privacy Policy!", "First Name must be between 1 and 32 characters!", "Last Name must be between 1 and 32 characters!", "E-Mail Address does not appear to be valid!", "Telephone must be between 3 and 32 characters!", "Password must be between 4 and 20 characters!")
