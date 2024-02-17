from selenium.webdriver.common.by import By


class SearchResultPage:
    def __init__(self, driver):
        self.driver = driver

    assertion_for_valid_searched_product_linktext = "HP LP3065"
    message_for_invalid_searched_product_xpath = "//input[@id='button-search']/following-sibling::p"

    def valid_product_displayed(self):
        return self.driver.find_element(By.LINK_TEXT, self.assertion_for_valid_searched_product_linktext).is_displayed()

    def retrieve_message_for_invalid_product(self):
        return self.driver.find_element(By.XPATH, self.message_for_invalid_searched_product_xpath).text
