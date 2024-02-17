import pytest
from Pages.HomePage import HomePage
from Pages.SearchResultPage import SearchResultPage
from tests.test_base import BaseTest


class Test_Search(BaseTest):
    def test_search_for_valid_product(self):
        home_page = HomePage(self.driver)
        search_result_page = home_page.search_for_a_product("HP")
        assert search_result_page.valid_product_displayed()

    def test_search_for_invalid_product(self):
        home_page = HomePage(self.driver)
        search_result_page = home_page.search_for_a_product("Honda")
        expected_text_invalid_product = "There is no product that matches the search criteria."
        assert search_result_page.retrieve_message_for_invalid_product().__eq__(expected_text_invalid_product)

    def test_search_without_entering_any_product(self):
        home_page = HomePage(self.driver)
        search_result_page = home_page.search_for_a_product("")
        expected_text_no_product = "There is no product that matches the search criteria."
        assert search_result_page.retrieve_message_for_invalid_product().__eq__(expected_text_no_product)
