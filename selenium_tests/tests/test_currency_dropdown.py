import pytest
import allure

from selenium_tests.page_objects.MainPage import MainPage
from selenium_tests.page_objects.page_elements.OpencartHeaderElement import OpencartHeaderElement


@allure.feature("Currency Dropdown")
@allure.story("Select currency from currency dropdown")
@allure.title("Select currency one-by-one from currency dropdown")
@pytest.mark.parametrize("currency", ["EUR", "GBP", "USD"])
def test_currency_dropdown(browser, currency):
    with allure.step("Open Main page"):
        main_page = MainPage(browser=browser)
        main_page.open_main_page()
        main_page.check_main_page_title()

    with allure.step(f"Select {currency} currency"):
        OpencartHeaderElement(browser=browser) \
            .expand_currency_dropdown() \
            .select_currency(currency)
