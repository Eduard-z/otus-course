import allure

from allure_commons.types import Severity
from .page_objects.MainPage import MainPage


@allure.story("Elements validation")
@allure.title("Find elements on Main page")
@allure.severity(severity_level=Severity.MINOR)
def test_main_page(browser):
    main_page = MainPage(browser=browser)
    main_page.open_main_page()

    main_page.find_navigation_bar()
    main_page.find_search_field()
    main_page.find_cart_button()
    main_page.find_your_store_link()
    main_page.find_product_item_card()
    main_page.expand_my_account_dropdown()
    main_page.click_register_account()
