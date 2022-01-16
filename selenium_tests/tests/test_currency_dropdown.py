from selenium_tests.page_objects.MainPage import MainPage
import pytest


@pytest.mark.parametrize("currency", ["EUR", "GBP", "USD"])
def test_currency_dropdown(browser, currency):
    main_page = MainPage(browser=browser)
    main_page.open_main_page()

    main_page \
        .expand_currency_dropdown() \
        .select_currency(currency)
