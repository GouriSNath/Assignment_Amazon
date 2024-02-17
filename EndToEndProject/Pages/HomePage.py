from selenium.webdriver.common.by import Byfrom Pages.LoginPage import LoginPage
from Pages.RegisterPage import RegisterPage
from Pages.SearchResultPage import SearchResultPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    search_box_field_name = "search"
    search_button_xpath = "//button[contains(@class,'btn-default')]"
    my_account_drop_down_menu_xpath = "(//span[contains(@class,'hidden-xs')])[3]"
    login_option_linktext = "Login"
    register_option_linktext = "Register"

    def enter_product_into_search_box_field(self, product_name):
        self.driver.find_element(By.NAME, self.search_box_field_name).click()
        self.driver.find_element(By.NAME, self.search_box_field_name).clear()
        self.driver.find_element(By.NAME, self.search_box_field_name).send_keys(product_name)

    def click_on_search_button(self):
        self.driver.find_element(By.XPATH, self.search_button_xpath).click()
        return SearchResultPage(self.driver)

    #This following method "search_for_a_product" is created by merging the above two
    #"enter_product_into_search_box_field" & "click_on_search_button" methods.
    def search_for_a_product(self, product_name):
        self.enter_product_into_search_box_field(product_name)
        return self.click_on_search_button()

    def click_on_my_account_drop_down_menu(self):
        self.driver.find_element(By.XPATH, self.my_account_drop_down_menu_xpath).click()

    def select_login_option(self):
        self.driver.find_element(By.LINK_TEXT, self.login_option_linktext).click()
        return LoginPage(self.driver)

    def navigate_to_login_option(self):
        self.click_on_my_account_drop_down_menu()
        return self.select_login_option()

    def select_register_option(self):
        self.driver.find_element(By.LINK_TEXT, self.register_option_linktext).click()
        return RegisterPage(self.driver)

    def navigate_to_register_option(self):
        self.click_on_my_account_drop_down_menu()
        return self.select_register_option()
