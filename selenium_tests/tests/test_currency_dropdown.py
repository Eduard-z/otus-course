import pytest
import allure

from selenium_tests.page_objects.MainPage import MainPage


@allure.feature("Currency Dropdown")
@allure.story("Select currency from currency dropdown")
@allure.title("Select currency one-by-one from currency dropdown")
@pytest.mark.parametrize("currency", ["EUR", "GBP", "USD"])
def test_currency_dropdown(browser, currency):
    with allure.step("Open Main page"):
        main_page = MainPage(browser=browser)
        main_page.open_main_page()

    with allure.step(f"Select {currency} currency"):
        main_page \
            .expand_currency_dropdown() \
            .select_currency(currency)
