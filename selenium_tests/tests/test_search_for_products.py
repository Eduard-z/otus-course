import allure
import pytest

from allure_commons.types import Severity
from selenium_tests.page_objects.MainPage import MainPage
from selenium_tests.page_objects.ProductSearchPage import ProductSearchPage
from ..page_objects.page_elements.ProductCardElement import ProductCardElement
from ..page_objects.page_elements.OpencartHeaderElement import OpencartHeaderElement


@allure.feature("Search Bar")
@allure.title("Search for products via Search Bar")
@allure.severity(severity_level=Severity.NORMAL)
@pytest.mark.parametrize("search_text", ["iphone", "iPhone", "iPh", "D", "IPOD H", "u t htc", "htc t o u c h"])
def test_search_for_products(browser, search_text):

    with allure.step("Open Main page"):
        main_page = MainPage(browser=browser)
        main_page.open_main_page()
        main_page.check_main_page_title()

    with allure.step("Search for a product"):
        header_element = OpencartHeaderElement(browser=browser)
        header_element.input_text_into_search_field(search_text)
        header_element.click_search_button()

    with allure.step("Check search results"):
        ProductSearchPage(browser=browser).check_search_page_title(search_text)

        product_cards = ProductCardElement(browser=browser)
        assert product_cards.all_product_cards_elements, f"No '{search_text}' products found"
        assert product_cards.compare_card_names_to_search_text(search_text), \
            f"Products displayed: {product_cards.all_product_names} -- do not match the search text: '{search_text}'"


@allure.feature("Search Bar")
@allure.title("Search for products via Search Bar: invalid value")
@allure.severity(severity_level=Severity.NORMAL)
@pytest.mark.parametrize("search_text", ["iphone 00", "iPhone z", " 55  IPOD    H ", "D"*257,
                                         r"!@#$%^&*()_+-=~`[];':\,./<>?{}|", "ъхзщшг"])
def test_search_for_products_invalid_value(browser, search_text):

    with allure.step("Open Main page"):
        main_page = MainPage(browser=browser)
        main_page.open_main_page()
        main_page.check_main_page_title()

    with allure.step("Search for a product"):
        header_element = OpencartHeaderElement(browser=browser)
        header_element.input_text_into_search_field(search_text)
        header_element.click_search_button()

    with allure.step("Check search results"):
        product_search_page = ProductSearchPage(browser=browser)
        product_search_page.check_search_page_title(search_text)
        assert product_search_page.search_criteria_field_value == search_text
        assert product_search_page.no_product_statement == "There is no product that matches the search criteria."

        product_cards = ProductCardElement(browser=browser)
        assert not product_cards.all_product_cards_elements, f"No '{search_text}' products should be displayed"


@allure.feature("Search Bar")
@allure.title("Search for products via Search Bar: empty value")
@allure.severity(severity_level=Severity.MINOR)
@pytest.mark.parametrize("search_text", [""])
def test_search_for_products_empty_value(browser, search_text):

    with allure.step("Open Main page"):
        main_page = MainPage(browser=browser)
        main_page.open_main_page()
        main_page.check_main_page_title()

    with allure.step("Search for a product"):
        header_element = OpencartHeaderElement(browser=browser)
        header_element.input_text_into_search_field(search_text)
        header_element.click_search_button()

    with allure.step("Check search results"):
        product_search_page = ProductSearchPage(browser=browser)
        product_search_page.check_search_page_title("Search", title_prefix="")
        assert product_search_page.search_criteria_field_value == search_text
        assert product_search_page.no_product_statement == "There is no product that matches the search criteria."

        product_cards = ProductCardElement(browser=browser)
        assert not product_cards.all_product_cards_elements, f"No '{search_text}' products should be displayed"


@allure.feature("Search Bar")
@allure.title("Search for products via Search Bar: space value")
@allure.severity(severity_level=Severity.MINOR)
@pytest.mark.parametrize("search_text", [" "])
def test_search_for_products_space_value(browser, search_text):

    with allure.step("Open Main page"):
        main_page = MainPage(browser=browser)
        main_page.open_main_page()
        main_page.check_main_page_title()

    with allure.step("Search for a product"):
        header_element = OpencartHeaderElement(browser=browser)
        header_element.input_text_into_search_field(search_text)
        header_element.click_search_button()

    with allure.step("Check search results"):
        ProductSearchPage(browser=browser).check_search_page_title("Search - ", title_prefix="")

        product_cards = ProductCardElement(browser=browser)
        assert product_cards.all_product_cards_elements, f"No '{search_text}' products found"
        assert product_cards.compare_card_names_to_search_text(search_text), \
            f"Products displayed: {product_cards.all_product_names} -- do not match the search text: '{search_text}'"
