import allure

from selenium_tests.page_objects.MainPage import MainPage


@allure.feature("Navigation Menu")
@allure.story("Navigation Menu items")
@allure.title("Check the list of Navigation Menu items")
def test_navigation_menu_items(browser):
    with allure.step("Open Main page"):
        main_page = MainPage(browser=browser)
        main_page.open_main_page()

    with allure.step("Check names of Navigation Menu items"):
        main_page.check_navigation_menu_items_names()
