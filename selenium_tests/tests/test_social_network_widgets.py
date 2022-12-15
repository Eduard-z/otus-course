import allure

from allure_commons.types import Severity
from ..page_objects.MainPage import MainPage
from ..page_objects.ProductPage import ProductPage
from ..page_objects.page_elements.ProductCardElement import ProductCardElement


@allure.story("Social Network widgets")
@allure.title("FaceBook widget")
@allure.severity(severity_level=Severity.MINOR)
def test_facebook_widget(browser):
    with allure.step("Open Main page"):
        main_page = MainPage(browser=browser)
        main_page.open_main_page()
        main_page.check_main_page_title()

    with allure.step("Open first product card on Main page"):
        product_card_element = ProductCardElement(browser=browser)
        first_product_name = product_card_element.all_product_names[0]
        product_card_element.click_into_first_product_card()

    with allure.step("Check correct page is opened"):
        product_page = ProductPage(browser=browser)
        assert product_page.product_name == first_product_name

    with allure.step("Check FaceBook button colour"):
        product_page.check_facebook_button_colour("rgba(24, 119, 242, 1)")

    with allure.step("Click FaceBook button"):
        old_browsers_tabs = product_page.all_browser_windows
        product_page.click_facebook_like()

    with allure.step("Check new tab opened"):
        assert product_page.is_new_browser_tab_opened(old_browsers_tabs)
        product_page.switch_to_new_browser_tab(old_browsers_tabs, "Facebook")
        product_page.switch_to_main_browser_tab()


@allure.story("Social Network widgets")
@allure.title("Twitter widget")
@allure.severity(severity_level=Severity.MINOR)
def test_twitter_widget(browser):
    with allure.step("Open Main page"):
        main_page = MainPage(browser=browser)
        main_page.open_main_page()
        main_page.check_main_page_title()

    with allure.step("Open first product card on Main page"):
        product_card_element = ProductCardElement(browser=browser)
        first_product_name = product_card_element.all_product_names[0]
        product_card_element.click_into_first_product_card()

    with allure.step("Check correct page is opened"):
        product_page = ProductPage(browser=browser)
        assert product_page.product_name == first_product_name

    with allure.step("Check Twitter button colour"):
        product_page.check_twitter_button_colour("rgba(29, 155, 240, 1)")

    with allure.step("Click Twitter button"):
        old_browsers_tabs = product_page.all_browser_windows
        product_page.click_twitter_tweet()

    with allure.step("Check new tab opened"):
        assert product_page.is_new_browser_tab_opened(old_browsers_tabs)
        product_page.switch_to_new_browser_tab(old_browsers_tabs, "Твиттер")
        product_page.switch_to_main_browser_tab()
