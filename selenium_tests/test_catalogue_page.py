import allure

from allure_commons.types import Severity
from .page_objects.CataloguePage import CataloguePage


@allure.story("Elements validation")
@allure.title("Find elements on Catalogue page")
@allure.severity(severity_level=Severity.MINOR)
def test_catalogue_page(browser):
    catalogue_page = CataloguePage(browser=browser)
    catalogue_page.open_catalogue_page()

    catalogue_page.find_catalogue_item_card()
    catalogue_page.find_products_group_menu_active()
    catalogue_page.find_filter_sortby_label()
    catalogue_page.find_add_to_cart_product_button()
    catalogue_page.find_number_of_products_and_pages()