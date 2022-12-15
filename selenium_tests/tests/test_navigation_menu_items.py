import allure
import pytest

from selenium_tests.page_objects.MainPage import MainPage
from selenium_tests.page_objects.ProductCategoryPage import ProductCategoryPage


@allure.feature("Navigation Menu")
@allure.story("Navigation Menu items")
@allure.title("Check the list of Navigation Menu items")
def test_navigation_menu_items(browser):
    with allure.step("Open Main page"):
        main_page = MainPage(browser=browser)
        main_page.open_main_page()
        main_page.check_main_page_title()

    with allure.step("Check names of Navigation Menu items"):
        main_page.check_navigation_menu_items_names()


@allure.feature("Navigation Menu")
@allure.story("Navigation Menu items")
@allure.title("Check links of Navigation Menu items")
@pytest.mark.parametrize("menu_items_names", MainPage.MENU_ITEMS_NAMES)
def test_navigation_menu_links(browser, menu_items_names):
    with allure.step("Open Main page"):
        main_page = MainPage(browser=browser)
        main_page.open_main_page()
        main_page.check_main_page_title()

    with allure.step("Check links: navigate to menu item pages"):
        if main_page.is_item_a_dropdown(menu_items_names):
            main_page.expand_navigation_menu_item_dropdown(menu_items_names)
            main_page.click_nav_menu_item_inside_dropdown(menu_items_names)
        else:
            main_page.click_nav_menu_item(menu_items_names)

        product_category_page = ProductCategoryPage(browser=browser)
        product_category_page.check_product_category_page_title(menu_items_names)
        product_category_page.check_product_category_page_header(menu_items_names)
