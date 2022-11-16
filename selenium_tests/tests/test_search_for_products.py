import allure

from allure_commons.types import Severity
from selenium_tests.page_objects.MainPage import MainPage
from ..page_objects.page_elements.ProductCardElement import ProductCardElement


@allure.feature("Search Bar")
@allure.title("Search for products via Search Bar")
@allure.severity(severity_level=Severity.NORMAL)
def test_search_for_products(browser, search_text="ipod"):

    with allure.step("Open Main page"):
        main_page = MainPage(browser=browser)
        main_page.open_main_page()

    with allure.step("Search for a product"):
        main_page.input_text_into_search_field(search_text)
        main_page.click_search_button()

    with allure.step("Check search results"):
        product_cards = ProductCardElement(browser=browser)
        assert product_cards.all_product_cards_elements, f"No {search_text} products found"
        assert all(search_text.lower() in i.lower() for i in product_cards.all_product_names), \
            f"Products displayed: {product_cards.all_product_names} -- do not match the search text: {search_text}"
