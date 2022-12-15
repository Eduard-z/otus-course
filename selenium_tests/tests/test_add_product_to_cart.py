import allure

from allure_commons.types import Severity
from selenium_tests.page_objects.MainPage import MainPage
from selenium_tests.page_objects.ProductSearchPage import ProductSearchPage
from ..page_objects.ShoppingCartPage import ShoppingCartPage
from ..page_objects.page_elements.AlertElement import AlertElement
from ..page_objects.page_elements.ProductCardElement import ProductCardElement
from ..page_objects.page_elements.OpencartHeaderElement import OpencartHeaderElement


@allure.feature("Add product to the cart")
@allure.title("Add 1 product to the cart from Search page")
@allure.severity(severity_level=Severity.CRITICAL)
def test_add_1_product_to_cart(browser, product1="ipod"):
    with allure.step("Open Main page"):
        main_page = MainPage(browser=browser)
        main_page.open_main_page()
        main_page.check_main_page_title()

    with allure.step("Search for a product"):
        header_element = OpencartHeaderElement(browser=browser)
        header_element.input_text_into_search_field(product1)
        header_element.click_search_button()

    with allure.step("Check search results"):
        ProductSearchPage(browser=browser).check_search_page_title(product1)

        product_cards = ProductCardElement(browser=browser)
        assert product_cards.all_product_cards_elements, f"No '{product1}' products found"

    with allure.step("Find the first product on the page and add it to the cart"):
        first_card = product_cards.all_product_cards_elements[0]
        first_card_name = product_cards.all_product_names[0]
        product_cards.click_add_to_cart_button(first_card)

        assert AlertElement(browser=browser).alert_text.removesuffix("\n×") == \
               f"Success: You have added {first_card_name} to your shopping cart!"

    with allure.step("Open Shopping Cart"):
        OpencartHeaderElement(browser=browser).click_cart_button()

        shopping_cart_page = ShoppingCartPage(browser=browser)
        shopping_cart_page.check_cart_page_title()

    with allure.step("Ensure name of product in the cart is equal to the product added earlier"):
        products_in_cart = shopping_cart_page.all_product_names
        assert products_in_cart == [first_card_name], \
            f"Product in the cart: {products_in_cart} does not match the added one: '{first_card_name}'"

    with allure.step("Post-condition: Remove added product from the cart"):
        shopping_cart_page.click_remove_button()
        shopping_cart_page.check_cart_empty_statement()
        assert not shopping_cart_page.all_products_in_cart, \
            f"Product '{first_card_name}' was not removed from the cart"


@allure.feature("Add product to the cart")
@allure.title("Add 2 products to the cart from Search page")
@allure.severity(severity_level=Severity.CRITICAL)
def test_add_2_products_to_cart(browser, product1="htc", product2="nikon"):
    with allure.step("Open Main page"):
        main_page = MainPage(browser=browser)
        main_page.open_main_page()
        main_page.check_main_page_title()

    with allure.step("Search for a product 1"):
        header_element = OpencartHeaderElement(browser=browser)
        header_element.input_text_into_search_field(product1)
        header_element.click_search_button()

    with allure.step("Check search results"):
        ProductSearchPage(browser=browser).check_search_page_title(product1)

        product_cards = ProductCardElement(browser=browser)
        assert product_cards.all_product_cards_elements, f"No '{product1}' products found"

    with allure.step("Find the first product on the page and add it to the cart"):
        first_card = product_cards.all_product_cards_elements[0]
        first_card_name1 = product_cards.all_product_names[0]
        product_cards.click_add_to_cart_button(first_card)

        assert AlertElement(browser=browser).alert_text.removesuffix("\n×") == \
               f"Success: You have added {first_card_name1} to your shopping cart!"

    with allure.step("Search for a product 2"):
        header_element = OpencartHeaderElement(browser=browser)
        header_element.input_text_into_search_field(product2)
        header_element.click_search_button()

    with allure.step("Check search results"):
        ProductSearchPage(browser=browser).check_search_page_title(product2)

        product_cards = ProductCardElement(browser=browser)
        assert product_cards.all_product_cards_elements, f"No '{product2}' products found"

    with allure.step("Find the first product on the page and add it to the cart"):
        first_card = product_cards.all_product_cards_elements[0]
        first_card_name2 = product_cards.all_product_names[0]
        product_cards.click_add_to_cart_button(first_card)

        assert AlertElement(browser=browser).alert_text.removesuffix("\n×") == \
               f"Success: You have added {first_card_name2} to your shopping cart!"

    with allure.step("Open Shopping Cart"):
        OpencartHeaderElement(browser=browser).click_cart_button()

        shopping_cart_page = ShoppingCartPage(browser=browser)
        shopping_cart_page.check_cart_page_title()

    with allure.step("Ensure names of products in the cart are equal to the products added earlier"):
        products_in_cart = shopping_cart_page.all_product_names
        assert products_in_cart == [first_card_name1, first_card_name2], \
            f"Products in the cart: {products_in_cart} do not match " \
            f"the added ones: '{first_card_name1}, {first_card_name2}'"
